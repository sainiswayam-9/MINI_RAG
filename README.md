# 🚀 Mini RAG — AI Engineer Assessment (Track B)

A production-style **Retrieval-Augmented Generation (RAG)** system built with **FastAPI**, **Supabase (pgvector)**, and modern **LLM tooling**.  
This project demonstrates how unstructured text can be indexed, retrieved, reranked, and used to generate **grounded answers with citations**.

---

## ✨ Key Highlights

- Cloud-hosted **vector database** (Supabase pgvector)
- Chunk-level indexing with overlap for better recall
- Semantic retrieval + **MMR diversification**
- Optional **cross-encoder reranking**
- LLM-generated answers with **explicit source attribution**
- Secure, server-side API key management
- Clean, modular backend architecture

---

## 🧠 What This Project Does

1. Accepts raw text documents via an API
2. Splits documents into overlapping chunks
3. Generates embeddings for each chunk
4. Stores embeddings in a hosted vector database
5. Retrieves the most relevant chunks for a user query
6. Reranks results for higher precision
7. Generates a **grounded answer** using an LLM
8. Returns answers along with **source metadata**

This mirrors real-world RAG systems used in search, Q&A, and enterprise knowledge assistants.

---

## 🏗️ Architecture Overview

User
├── POST /index (document text)
│ ├── Chunking (1000 tokens, 15% overlap)
│ ├── Embedding generation
│ └── Supabase pgvector (documents table)
│
└── POST /query (user question)
├── Query embedding
├── Vector similarity search (cosine)
├── MMR (diversity optimization)
├── Reranking (optional)
└── LLM answer + citations


---

## 🛠️ Tech Stack

### Backend
- **FastAPI** (Python)
- **Uvicorn** (ASGI server)

### Vector Database
- **Supabase (PostgreSQL + pgvector)**
- Fully hosted cloud solution

### Embeddings
- **OpenAI `text-embedding-3-small`**
- Dimensionality: **1536**

### Retrieval & Ranking
- Cosine similarity search (pgvector)
- **MMR (Maximal Marginal Relevance)**
- **Cohere Rerank** (optional)

### LLM
- **OpenAI GPT-4o-mini**
- Context-restricted prompting for grounded answers

---

## 🗄️ Vector Database Design

### Table: `documents`

Each row represents **one document chunk**.

| Column | Description |
|------|------------|
| `id` | Unique chunk UUID |
| `doc_id` | Document identifier |
| `chunk_index` | Position within document |
| `content` | Chunk text |
| `embedding` | Vector embedding |
| `metadata` | Source, title, etc. |
| `created_at` | Timestamp |

A SQL function `match_documents()` performs efficient vector similarity search via RPC.

---

## ✂️ Chunking Strategy

- **Chunk size**: ~1000 tokens  
- **Overlap**: 15%  
- **Granularity**: Chunk-level indexing  

This improves semantic recall while preserving contextual continuity.

---

## 🔍 Retrieval Pipeline

1. Embed user query
2. Retrieve top-N chunks from vector DB
3. Apply **MMR** to balance relevance and diversity
4. Rerank candidates using a cross-encoder
5. Select final top-K chunks for generation

---

## 🧾 Grounded Answering & Citations

The LLM is prompted to:
- Use **only retrieved context**
- Produce concise, factual answers
- Attach inline citations (e.g. `[1]`, `[2]`)
- Return structured source metadata

This reduces hallucinations and improves answer trustworthiness.

---

## 🔌 API Endpoints

### `POST /index` — Index Document
```json
{
  "doc_id": "example_doc",
  "title": "RAG Overview",
  "text": "Document text goes here"
}

'POST /query' — Query RAG
{
  "query": "What is Retrieval Augmented Generation?"
}

---


## 🔐 Environment Variables

Secrets are managed using environment variables and excluded from version control.

SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
OPENAI_API_KEY=
COHERE_API_KEY=

.env is ignored via .gitignore
.env.example is provided as a template


▶️ Running Locally
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Swagger UI:

http://127.0.0.1:8000/docs



☁️ Deployment

-  Backend: Render / Railway (free tier)
-  Database: Supabase cloud
-  Secrets: Platform environment variables


⚠️ Remarks & Tradeoffs

-  Reranker usage may be limited by free-tier quotas
-  Chunking is token-approximate for simplicity
-  Cost estimates are approximate and provider-dependent
-  Designed for clarity and correctness over large-scale optimization


🔮 Future Enhancements

-  File uploads (PDF / DOCX)
-  Frontend UI (Next.js)
-  Streaming responses
-  Hybrid search (BM25 + vectors)
-  Detailed token and cost analytics


👤 Author

Swayam Saini
Aspiring AI Engineer | Data Science Undergraduate
Mini RAG Assessment

contact : +91-7009570187
mail : sainiswayam7@gmail.com
