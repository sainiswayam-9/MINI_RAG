import math

def chunk_text(text: str, chunk_size: int, overlap_ratio: float):
    words = text.split()
    overlap = int(chunk_size * overlap_ratio)
    step = chunk_size - overlap

    chunks = []
    for i in range(0, len(words), step):
        chunk_words = words[i:i + chunk_size]
        chunks.append({
            "text": " ".join(chunk_words),
            "chunk_index": len(chunks),
            "start_word": i,
            "end_word": i + len(chunk_words)
        })
    return chunks
