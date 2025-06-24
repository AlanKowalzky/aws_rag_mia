import logging
from fastapi import FastAPI, HTTPException

from src.api.schemas import QueryRequest, QueryResponse
from src.rag_pipeline import get_rag_chain

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(
    title="MIA RAG API",
    description="API do zadawania pytań na temat kolekcji Minneapolis Institute of Art.",
    version="1.0.0"
)

# Inicjalizacja łańcucha RAG przy starcie aplikacji.
# Dzięki temu modele i baza danych ładują się tylko raz.
try:
    rag_chain, retriever = get_rag_chain()
except Exception as e:
    logging.error(f"Krytyczny błąd podczas inicjalizacji RAG chain: {e}")
    rag_chain, retriever = None, None

@app.post("/query", response_model=QueryResponse)
def answer_question(request: QueryRequest):
    """
    Przyjmuje pytanie użytkownika i zwraca odpowiedź wygenerowaną przez system RAG
    wraz z dokumentami źródłowymi.
    """
    if not rag_chain or not retriever:
        raise HTTPException(status_code=503, detail="System RAG nie jest dostępny. Sprawdź logi serwera.")
    
    answer = rag_chain.invoke(request.question)
    source_documents = retriever.invoke(request.question)
    
    return QueryResponse(answer=answer, sources=source_documents)