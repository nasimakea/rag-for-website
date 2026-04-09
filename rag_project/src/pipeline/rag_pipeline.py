from src.utils.logger import logging
from src.scraping.scraper import scrape_website
from src.processing.cleaner import clean_text
from src.processing.splitter import split_text
from src.embedding.embedder import embed_chunks
from src.retrieval.retriever import VectorStore
from src.llm.groq_llm import generate_answer

logging.basicConfig(level=logging.INFO)


class RAGPipeline:
    def __init__(self, url: str):
        self.url = url
        self.vector_store = None

    def build_index(self):
        try:
            logging.info(" Building RAG index...")

            raw_text = scrape_website(self.url)
            cleaned_text = clean_text(raw_text)
            chunks = split_text(cleaned_text)
            embeddings = embed_chunks(chunks)

            self.vector_store = VectorStore(embeddings, chunks)

            logging.info(" RAG index ready!")

        except Exception as e:
            logging.error(f"  Error building index: {e}")
            raise

    def query(self, question: str):
        try:
            if not self.vector_store:
                raise ValueError("Vector store not initialized")

            query_embedding = embed_chunks([question])[0]
            results = self.vector_store.search(query_embedding, k=3)

            answer = generate_answer(question, results)

            return answer

        except Exception as e:
            logging.error(f"  Query failed: {e}")
            return "Something went wrong while generating answer."