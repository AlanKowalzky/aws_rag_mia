import logging

from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from src import config
from src.data_loader import load_mia_documents

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Główna funkcja orkiestrująca proces wczytywania, dzielenia,
    tworzenia embeddingów i zapisywania danych w bazie wektorowej FAISS.
    """
    load_dotenv()
    logging.info("Rozpoczynanie procesu przetwarzania danych...")

    # 1. Wczytaj dokumenty
    documents = load_mia_documents()
    if not documents:
        logging.warning("Nie znaleziono żadnych dokumentów do przetworzenia. Zakończono.")
        return

    # 2. Podziel dokumenty na chunki
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(documents)
    logging.info(f"Podzielono {len(documents)} dokumentów na {len(chunks)} chunków.")

    # 3. Zainicjuj model do tworzenia embeddingów
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

    # 4. Stwórz bazę wektorową FAISS i zapisz ją lokalnie
    logging.info("Tworzenie embeddingów i budowanie indeksu FAISS. To może potrwać kilka minut...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(config.FAISS_INDEX_PATH)
    logging.info(f"Baza wektorowa została pomyślnie zapisana w folderze: {config.FAISS_INDEX_PATH}")

if __name__ == "__main__":
    main()