def build_prompt(question: str, chunks: list):
    context = ""
    for i, c in enumerate(chunks, start=1):
        context += f"[{i}] {c['content']}\n\n"

    return f"""
You are a grounded AI assistant.
Answer ONLY using the context below.
Add inline citations like [1], [2].

Question:
{question}

Context:
{context}

Answer:
"""
