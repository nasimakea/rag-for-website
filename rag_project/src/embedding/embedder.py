from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("embedding_api_key")



client = InferenceClient(api_key=api_key)

import time

def embed_chunks(chunks, batch_size=16):
    all_embeddings = []
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        try:
            # Send the entire batch at once
            batch_embeddings = client.feature_extraction(batch, model="BAAI/bge-m3")
            all_embeddings.extend(batch_embeddings)
            
            # Optional: Short sleep to avoid rate limits
            time.sleep(0.1) 
        except Exception as e:
            print(f"Error at batch {i}: {e}")
            # Consider a retry logic here
            
    return all_embeddings