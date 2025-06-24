import logging
from operator import itemgetter

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from src import config
from src.vector_db import load_vector_db

# Ładowanie zmiennych środowiskowych (GOOGLE_API_KEY)
load_dotenv()

# Szablon promptu
template = """
Jesteś pomocnym asystentem AI dla Minneapolis Institute of Art.
Odpowiedz na pytanie bazując wyłącznie na poniższym kontekście.
Jeśli informacje nie znajdują się w kontekście, odpowiedz: "Niestety, nie znalazłem informacji na ten temat w mojej bazie wiedzy."

Kontekst:
{context}

Pytanie:
{question}

Odpowiedź:
"""
PROMPT = PromptTemplate.from_template(template)

def format_docs(docs):
    """Łączy zawartość dokumentów w jeden string."""
    return "\n\n".join(doc.page_content for doc in docs)

def get_rag_chain():
    """
    Tworzy i zwraca kompletny łańcuch RAG (Retrieval-Augmented Generation).
    """
    logging.info("Inicjalizacja łańcucha RAG...")
    vector_db = load_vector_db()
    retriever = vector_db.as_retriever()
    llm = ChatGoogleGenerativeAI(model=config.LLM_MODEL_NAME, temperature=0.1)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | PROMPT
        | llm
        | StrOutputParser()
    )
    logging.info("Łańcuch RAG został pomyślnie zainicjalizowany.")
    return rag_chain, retriever