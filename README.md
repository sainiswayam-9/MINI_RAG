# 🚀 Mini RAG — AI Engineer Assessment (Track B)

A production-oriented **Retrieval-Augmented Generation (RAG)** system built using **FastAPI**, **Supabase (pgvector)**, and modern **LLM tooling**.  
This project demonstrates how unstructured text can be indexed, retrieved, reranked, and used to generate **grounded answers with clear source attribution**.

---

## ✨ Key Highlights

- Cloud-hosted **vector database** using Supabase pgvector  
- Chunk-level document indexing with overlap for improved recall  
- Semantic retrieval combined with **MMR (Maximal Marginal Relevance)**  
- Optional **cross-encoder reranking** for higher precision  
- LLM-generated answers with **explicit citations and sources**  
- Secure, server-side API key management  
- Clean, modular, and extensible backend architecture  

---

## 🧠 What This Project Does

1. Accepts raw text documents through an API  
2. Splits documents into overlapping semantic chunks  
3. Generates embeddings for each chunk  
4. Stores embeddings in a hosted vector database  
5. Retrieves the most relevant chunks for a user query  
6. Applies reranking for improved answer quality  
7. Generates a **grounded response** using an LLM  
8. Returns answers along with **source metadata**  

This mirrors real-world RAG systems used in search engines, knowledge assistants, and enterprise Q&A platforms.

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
├── MMR diversification
├── Reranking (optional)
└── LLM answer with citations


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
- Cosine similarity search using pgvector  
- **MMR (Maximal Marginal Relevance)**  
- **Cohere Rerank** (optional)

### LLM
- **OpenAI GPT-4o-mini**  
- Context-restricted prompting for grounded answers

---

## 🗄️ Vector Database Design

### Table: `documents`

Each row represents **one document chunk**.

| Column        | Description |
|--------------|------------|
| `id`         | Unique chunk UUID |
| `doc_id`     | Document identifier |
| `chunk_index`| Position within the document |
| `content`    | Chunk text |
| `embedding`  | Vector embedding |
| `metadata`   | Source, title, section info |
| `created_at` | Timestamp |

A SQL function `match_documents()` is used for efficient vector similarity search via Supabase RPC.

---

## ✂️ Chunking Strategy

- **Chunk size**: ~1000 tokens  
- **Overlap**: 15%  
- **Granularity**: Chunk-level indexing  

This balances retrieval accuracy with contextual continuity.

---

## 🔍 Retrieval Pipeline

1. Embed the user query  
2. Retrieve top-N chunks from the vector database  
3. Apply **MMR** to balance relevance and diversity  
4. Rerank candidates using a cross-encoder (optional)  
5. Select final top-K chunks for generation  

---

## 🧾 Grounded Answering & Citations

The LLM is explicitly instructed to:
- Use **only the retrieved context**
- Produce concise and factual answers
- Attach inline citations (e.g. `[1]`, `[2]`)
- Return structured source metadata  

This significantly reduces hallucinations and improves answer trustworthiness.

---

## 🔌 API Endpoints

### `POST /index` — Index Document
```json
{
  "doc_id": "example_doc",
  "title": "RAG Overview",
  "text": "Document text goes here"
}
```
### 'POST /query' — Query RAG
```json
{
  "query": "What is Retrieval Augmented Generation?"
}
```


🔐 Environment Variables

Secrets are managed using environment variables and are excluded from version control.

*  SUPABASE_URL=
*  SUPABASE_SERVICE_ROLE_KEY=
*  OPENAI_API_KEY=
*  COHERE_API_KEY=

.env is ignored via .gitignore
.env.example is provided as a template


▶️ Running Locally
# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Swagger UI
http://127.0.0.1:8000/docs


☁️ Deployment

*  Backend: Render
        🔗 https://mini-rag-ox04.onrender.com/docs
*  Database: Supabase Cloud
*  Secrets: Managed via platform environment variables


⚠️ Remarks & Tradeoffs

*  Reranker usage may be limited by free-tier quotas
*  Chunking uses approximate token sizing for simplicity
*  Cost estimates are provider-dependent and approximate
*  Designed for clarity and correctness over large-scale optimization

  
🔮 Future Enhancements

*  File uploads (PDF / DOCX)
*  Frontend UI (Next.js)
*  Streaming responses
*  Hybrid search (BM25 + vectors)
*  Detailed token and cost analytics


👤 Author

Swayam Saini
Aspiring AI Engineer | Data Science Undergraduate
📧 Email: sainiswayam7@gmail.com
📞 Contact: +91-7009570187


## 🏗️ Architecture Overview

