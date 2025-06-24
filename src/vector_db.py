import logging
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from src import config

def load_vector_db():
    """
    Ładuje istniejącą bazę wektorową FAISS z dysku.

    Returns:
        FAISS: Załadowany obiekt bazy wektorowej.
    """
    logging.info("Ładowanie modelu embeddingów...")
    embeddings = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'}
    )
    logging.info(f"Ładowanie bazy wektorowej z: {config.FAISS_INDEX_PATH}")
    db = FAISS.load_local(config.FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return db