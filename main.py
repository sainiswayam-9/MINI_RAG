from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    INITIAL_TOP_K,
    FINAL_TOP_K
)
from chunking import chunk_text
from embeddings import embed_texts
from vector_store import upsert_chunks, similarity_search
from retriever import mmr
from reranker import rerank
from prompt import build_prompt
from llm import generate_answer

app = FastAPI(title="Mini RAG")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<html><body><h1>Mini RAG</h1><p>Use <a href='/docs'>/docs</a> to explore the API.</p></body></html>"


@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)

class IndexRequest(BaseModel):
    doc_id: str
    title: str
    text: str

class QueryRequest(BaseModel):
    query: str


@app.post("/index")
def index_doc(req: IndexRequest):
    # 1. Chunk document
    chunks = chunk_text(req.text, CHUNK_SIZE, CHUNK_OVERLAP)

    # 2. Embed chunks
    embeddings = embed_texts([c["content"] for c in chunks])

    # 3. Store in vector DB
    upsert_chunks(
        req.doc_id,
        chunks,
        embeddings,
        metadata={
            "title": req.title,
            "source": req.doc_id
        }
    )

    return {
        "status": "indexed",
        "chunks": len(chunks)
    }


@app.post("/query")
def query_rag(req: QueryRequest):
    # 1. Embed query
    query_embedding = embed_texts([req.query])[0]

    # 2. Retrieve top-N from vector DB
    retrieved = similarity_search(query_embedding, INITIAL_TOP_K)

    # 3. Apply MMR (diversity)
    mmr_docs = mmr(
        query_embedding,
        retrieved,
        FINAL_TOP_K * 2
    )

    # 4. Rerank and select final top-K
    final_docs = rerank(
        req.query,
        mmr_docs,
        FINAL_TOP_K
    )

    # 5. Build prompt + generate answer
    prompt = build_prompt(req.query, final_docs)
    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "sources": [
            {
                "doc_id": d["doc_id"],
                "chunk_index": d["chunk_index"],
                "metadata": d["metadata"]
            }
            for d in final_docs
        ]
    }
