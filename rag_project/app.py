import streamlit as st
from src.pipeline.rag_pipeline import RAGPipeline

# Page config
st.set_page_config(
    page_title=" Website RAG Chatbot",
    layout="centered"
)

st.title(" Website RAG Chatbot")

# --------------------------
# SESSION STATE
# --------------------------
if "pipeline" not in st.session_state:
    st.session_state.pipeline = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------------------------
# INPUT: URL
# --------------------------
url = st.text_input(" Enter Website URL")

if st.button(" Build Index"):
    if not url:
        st.warning("Please enter a valid URL")
    else:
        with st.spinner("Building index... "):
            try:
                pipeline = RAGPipeline(url)
                pipeline.build_index()
                st.session_state.pipeline = pipeline
                st.success(" Index built successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

# --------------------------
# CHAT UI
# --------------------------
st.divider()
st.subheader(" Ask Questions")

query = st.text_input("Your question")

if st.button("Get Answer"):
    if not st.session_state.pipeline:
        st.warning(" Please build index first!")
    elif not query:
        st.warning(" Enter a question")
    else:
        with st.spinner("Thinking... "):
            answer = st.session_state.pipeline.query(query)

            # Save chat history
            st.session_state.chat_history.append(("You", query))
            st.session_state.chat_history.append(("Bot", answer))

# --------------------------
# DISPLAY CHAT
# --------------------------
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"** You:** {message}")
    else:
        st.markdown(f"** Bot:** {message}")