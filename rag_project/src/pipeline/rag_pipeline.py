from src.scraping.scraper import scrape_website
from src.processing.cleaner import clean_text
from src.processing.splitter import split_text
from src.embedding.embedder import embed_chunks
from src.retrieval.retriever import VectorStore
from src.llm.groq_llm import generate_answer


class RAGPipeline:
    def __init__(self, url):
        self.url = url
        self.vector_store = None

    def build_index(self):
        print("🔄 Building RAG index...")

        raw_text = scrape_website(self.url)
        cleaned_text = clean_text(raw_text)
        chunks = split_text(cleaned_text)
        embeddings = embed_chunks(chunks)

        self.vector_store = VectorStore(embeddings, chunks)

        print("✅ RAG index ready!")

    def query(self, question):
        query_embedding = embed_chunks([question])[0]
        results = self.vector_store.search(query_embedding, k=3)

        answer = generate_answer(question, results)

        return answer