import streamlit as st
from src.pipeline.rag_pipeline import RAGPipeline

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("🤖 Website RAG Chatbot")

# Initialize pipeline
if "pipeline" not in st.session_state:
    pipeline = RAGPipeline("https://www.dancingnumbers.com/")
    pipeline.build_index()
    st.session_state.pipeline = pipeline

# User input
query = st.text_input("Ask your question:")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            answer = st.session_state.pipeline.query(query)

        st.success("Answer:")
        st.write(answer)