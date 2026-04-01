import streamlit as st
import time
from huggingface_hub import InferenceClient


def get_embedding_client():
    api_key = st.secrets.get("embedding_api_key")

    if not api_key:
        raise ValueError("❌ embedding_api_key not found in Streamlit secrets")

    return InferenceClient(api_key=api_key)


def embed_chunks(chunks, batch_size=16):
    client = get_embedding_client()  # ✅ safe initialization

    all_embeddings = []

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i: i + batch_size]

        try:
            batch_embeddings = client.feature_extraction(
                batch,
                model="BAAI/bge-m3"
            )

            all_embeddings.extend(batch_embeddings)

            # ✅ small delay to avoid rate limit
            time.sleep(0.1)

        except Exception as e:
            print(f"❌ Error at batch {i}: {e}")

            # 🔁 simple retry once
            try:
                time.sleep(1)
                batch_embeddings = client.feature_extraction(
                    batch,
                    model="BAAI/bge-m3"
                )
                all_embeddings.extend(batch_embeddings)
            except Exception as retry_error:
                print(f"❌ Retry failed at batch {i}: {retry_error}")

    return all_embeddings