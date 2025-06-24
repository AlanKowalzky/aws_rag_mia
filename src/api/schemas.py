from typing import List, Dict, Any
from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    """Schemat zapytania przychodzącego do API."""
    question: str = Field(
        ...,
        min_length=3,
        description="Pytanie użytkownika dotyczące kolekcji muzeum."
    )

class SourceDocument(BaseModel):
    """Schemat pojedynczego dokumentu źródłowego."""
    page_content: str
    metadata: Dict[str, Any]

class QueryResponse(BaseModel):
    """Schemat odpowiedzi zwracanej przez API."""
    answer: str
    sources: List[SourceDocument]