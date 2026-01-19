import os
from dotenv import load_dotenv

load_dotenv()

# ========================
# API KEYS
# ========================
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ========================
# RAG CONFIG
# ========================
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 0.15

INITIAL_TOP_K = 40
FINAL_TOP_K = 6
MMR_LAMBDA = 0.7

VECTOR_TABLE = "documents"
