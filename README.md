



# 🤖 Website RAG Chatbot

## 🚀 Project Overview

This project is an end-to-end **Retrieval-Augmented Generation (RAG) based chatbot** that can answer user queries from any given website.

The system automatically scrapes website content, processes and splits the text into chunks, converts them into vector embeddings, and stores them in a vector database. When a user asks a question, the system retrieves the most relevant information and uses a Large Language Model (LLM) to generate accurate and context-aware responses.

The application is deployed using **Streamlit**, providing an interactive interface for users to chat with website data in real time.

---

## 🔥 Key Features

* 🌐 Works with any website URL
* 🧠 Context-aware answers using RAG architecture
* ⚡ Fast inference using LLM (Groq API)
* 📦 Modular pipeline design
* 💬 Interactive chatbot UI with Streamlit

---

## 🏗️ Project Structure

```bash
rag_project/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── config/
│
├── src/
│   ├── scraping/
│   │   └── scraper.py
│   │
│   ├── processing/
│   │   ├── cleaner.py
│   │   └── splitter.py
│   │
│   ├── embedding/
│   │   └── embedder.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── llm/
│   │   └── groq_llm.py
│   │
│   ├── pipeline/
│   │   └── rag_pipeline.py
│
└── README.md
```

---

## ⚙️ RAG Pipeline Workflow

```
Website URL
   ↓
Web Scraping
   ↓
Text Cleaning
   ↓
Text Splitting
   ↓
Embedding Generation
   ↓
Vector Store (FAISS)
   ↓
User Query
   ↓
Similarity Search
   ↓
LLM (Groq)
   ↓
Final Answer
```

---

## 🌐 Web Scraping

Extracts clean text from a given website URL.

* Uses `requests` and `BeautifulSoup`
* Removes unwanted HTML tags
* Returns structured clean text

**Function:**
`scrape_website(url: str) -> str`

---

## 🧹 Text Cleaning

Cleans and normalizes scraped text.

* Removes empty lines and extra spaces
* Ensures consistent formatting

**Function:**
`clean_text(text: str) -> str`

---

## ✂️ Text Splitting

Splits text into smaller chunks for better retrieval.

* Uses `RecursiveCharacterTextSplitter`
* Chunk size: 500
* Overlap: 100

**Function:**
`split_text(text: str) -> List[str]`

---

## 🔗 Embedding Generation

Converts text into vector embeddings.

* Uses Hugging Face model `BAAI/bge-m3`
* Batch processing for efficiency

**Function:**
`embed_chunks(chunks: List[str]) -> List[List[float]]`

---

## 🔍 Vector Store & Retrieval

Stores and retrieves embeddings using similarity search.

* Uses FAISS
* Retrieves top-k relevant chunks

**Class:** `VectorStore`

* `search(query_embedding, k=3)`

---

## 🤖 Answer Generation (LLM)

Generates answers using retrieved context.

* Uses Groq API (`llama-3.1-8b-instant`)
* Prevents hallucination with strict prompting

**Function:**
`generate_answer(query, context_chunks) -> str`

---

## ⚙️ Pipeline Orchestration

Handles complete RAG workflow.

**Class:** `RAGPipeline`

* `build_index()` → prepares vector database
* `query(question)` → returns final answer

---

## 🛠️ Installation

```bash
git clone <your-repo-url>
cd rag_project
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
embedding_api_key=your_huggingface_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Example Usage

1. Enter a website URL
2. Ask any question
3. Get context-aware answers instantly

---

## 🚀 Future Improvements

* 🔍 Add hybrid search (BM25 + vector search)
* 📄 Support PDF and document uploads
* 🧠 Use advanced reranking models
* 🌍 Multi-language support
* 📊 Add answer confidence scoring

---

## 🧠 Tech Stack

* Python
* Streamlit
* FAISS
* Hugging Face
* Groq LLM
* BeautifulSoup

---

## 📌 Conclusion

This project demonstrates a complete production-style implementation of a **RAG-based AI system**, combining web scraping, NLP, vector search, and LLMs into a scalable and modular pipeline.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!


