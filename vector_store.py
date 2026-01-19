from supabase import create_client
from config import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, VECTOR_TABLE
import uuid

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def upsert_chunks(doc_id: str, chunks: list, embeddings: list, metadata: dict):
    rows = []
    for chunk, embedding in zip(chunks, embeddings):
        rows.append({
            "id": str(uuid.uuid4()),
            "doc_id": doc_id,
            "chunk_index": chunk["chunk_index"],
            "content": chunk["text"],
            "embedding": embedding,
            "metadata": {
                **metadata,
                "start_word": chunk["start_word"],
                "end_word": chunk["end_word"]
            }
        })

    supabase.table(VECTOR_TABLE).upsert(rows).execute()

def similarity_search(query_embedding, top_k: int):
    response = supabase.rpc(
        "match_documents",
        {
            "query_embedding": query_embedding,
            "match_count": top_k   # ✅ MUST MATCH SQL FUNCTION
        }
    ).execute()

    return response.data

