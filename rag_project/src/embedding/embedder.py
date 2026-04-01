

from huggingface_hub import InferenceClient

# ❌ Not needed in deployment (Streamlit Cloud)
# from dotenv import load_dotenv
# import os
# load_dotenv()
# api_key = os.getenv("embedding_api_key")

import streamlit as st
import time

# ✅ Correct way (use Streamlit secrets)
client = InferenceClient(api_key=st.secrets["HUGGINGFACE_API_KEY"])


def embed_chunks(chunks, batch_size=16):
    all_embeddings = []
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        try:
            # ✅ Send batch for embedding
            batch_embeddings = client.feature_extraction(
                batch,
                model="BAAI/bge-m3"
            )
            
            all_embeddings.extend(batch_embeddings)
            
            # Optional: avoid rate limits
            time.sleep(0.1)

        except Exception as e:
            print(f"Error at batch {i}: {e}")
            # You can add retry logic here if needed
            
    return all_embeddings