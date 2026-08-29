def build_movie_prompt(
    question: str,
    context: str
) -> str:

    prompt = f"""
You are a helpful movie recommendation assistant.

Your job is to answer the user's question
using ONLY the movie information provided
in the context.

Rules:

1. Do not invent movie information.
2. Do not use information outside the context.
3. If the context does not contain enough
   information, clearly say so.
4. Keep the answer concise and useful.
5. When listing movies, include the title
   and year when available.

Context:
----------------
{context}
----------------

User Question:
{question}

Answer:
"""

    return prompt