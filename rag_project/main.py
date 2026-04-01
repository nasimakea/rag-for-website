from src.scraping.scraper import scrape_website
from src.processing.cleaner import clean_text
from src.processing.splitter import split_text
from src.embedding.embedder import embed_chunks
from src.retrieval.retriever import VectorStore
from src.llm.groq_llm import generate_answer

url = "https://www.dancingnumbers.com/"

print("🔹 Starting RAG pipeline...")

# Step 1: Scrape
raw_text = scrape_website(url)
print("✅ Scraping done")

# Step 2: Clean
cleaned_text = clean_text(raw_text)
print("✅ Cleaning done")

# Step 3: Chunk
chunks = split_text(cleaned_text)
print(f"✅ Chunking done: {len(chunks)} chunks")

# Step 4: Embed
embeddings = embed_chunks(chunks)
print("✅ Embedding done")

print(f"Embedding shape: {len(embeddings)}")

# The number of chunks you processed
print(f"Total Chunks: {len(embeddings)}")

# The dimension of the first vector (the "shape" of the embedding)
if len(embeddings) > 0:
    print(f"Vector Dimension: {len(embeddings[0])}")



# Step 5: Create Vector Store
vector_store = VectorStore(embeddings, chunks)
print("✅ FAISS index created")

# Step 6: Test Query
query = "What services does this website provide?"

query_embedding = embed_chunks([query])[0]

results = vector_store.search(query_embedding, k=3)

print("\n🔍 Retrieved Chunks:\n")
for i, r in enumerate(results):
    print(f"\nResult {i+1}:\n{r[:300]}")


query = "What services does this website provide?"

query_embedding = embed_chunks([query])[0]
results = vector_store.search(query_embedding, k=3)

print("\n🔍 Retrieved Chunks Done")

# 🧠 LLM Answer
answer = generate_answer(query, results)

print("\n🤖 Final Answer:\n")
print(answer)