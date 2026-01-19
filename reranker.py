import cohere
from config import COHERE_API_KEY

co = cohere.Client(COHERE_API_KEY)

def rerank(query: str, docs: list, top_k: int):
    texts = [d["content"] for d in docs]

    response = co.rerank(
        model="rerank-english-v2.0",
        query=query,
        documents=texts,
        top_n=top_k
    )

    reranked = []
    for r in response.results:
        reranked.append(docs[r.index])

    return reranked
