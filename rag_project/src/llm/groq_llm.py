from groq import Groq

# ❌ Not needed in deployment
# import os
# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from groq import Groq

# ✅ Correct way (use Streamlit secrets)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ❌ This overrides above and breaks deployment
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, context_chunks):
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
        ]
    )

    return response.choices[0].message.content