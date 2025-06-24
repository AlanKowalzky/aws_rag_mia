import os
from pathlib import Path

# Główny katalog projektu
ROOT_DIR = Path(__file__).parent.parent

# Ścieżka do katalogu z danymi JSON
DATA_PATH = ROOT_DIR / "data" / "collection" / "objects"

# Ścieżka do zapisu indeksu wektorowego FAISS
FAISS_INDEX_PATH = str(ROOT_DIR / "faiss_index")

# Konfiguracja modelu do tworzenia embeddingów
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Konfiguracja dzielenia tekstu na fragmenty (chunki)
CHUNK_SIZE = 750
CHUNK_OVERLAP = 75

# Konfiguracja modelu LLM
LLM_MODEL_NAME = "gemini-1.5-flash"
# Konfiguracja dzielenia tekstu na fragmenty (chunki)
CHUNK_SIZE = 750 
CHUNK_OVERLAP = 75