import numpy as np
from config import MMR_LAMBDA

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def mmr(query_emb, docs, k):
    selected = []
    candidates = docs.copy()

    while len(selected) < k and candidates:
        scores = []
        for d in candidates:
            relevance = cosine_sim(query_emb, d["embedding"])
            diversity = max(
                [cosine_sim(d["embedding"], s["embedding"]) for s in selected],
                default=0
            )
            score = MMR_LAMBDA * relevance - (1 - MMR_LAMBDA) * diversity
            scores.append(score)

        best_idx = scores.index(max(scores))
        selected.append(candidates.pop(best_idx))

    return selected
