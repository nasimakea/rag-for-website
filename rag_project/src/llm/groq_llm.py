from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)


def generate_answer(query, context_chunks):
    if not context_chunks:
        return "No relevant context found."

    context = "\n\n".join(context_chunks)[:3000]

    prompt = f"""
Answer the question ONLY using the provided context.
Do NOT use prior knowledge.

Context:
{context}

Question:
{query}

If the answer is not explicitly in the context, say "I don't know".
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"