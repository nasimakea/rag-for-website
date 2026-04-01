import streamlit as st
from groq import Groq


def get_groq_client():
    api_key = st.secrets.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError("❌ GROQ_API_KEY not found in Streamlit secrets")

    return Groq(api_key=api_key)


def generate_answer(query, context_chunks):
    client = get_groq_client()  # ✅ initialize safely

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an AI assistant. Answer ONLY from the given context.

Context:
{context}

Question:
{query}

If answer is not in context, say "I don't know".
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2  # ✅ more controlled answers
    )

    return response.choices[0].message.content.strip()