import json
import logging
from pathlib import Path
from typing import List

from langchain_core.documents import Document
from tqdm import tqdm

from src import config

# Konfiguracja logowania, aby widzieć postęp i ewentualne błędy
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_mia_documents() -> List[Document]:
    """
    Wczytuje dane o dziełach sztuki z plików JSON z kolekcji Minneapolis Institute of Art,
    przetwarza je i zwraca jako listę obiektów `Document` z biblioteki LangChain.

    Treść każdego dokumentu to połączone najważniejsze pola tekstowe.
    Metadane zawierają źródło (URL), tytuł i numer inwentarzowy do cytowania.
    """
    json_files = list(config.DATA_PATH.rglob("*.json"))
    logging.info(f"Znaleziono {len(json_files)} plików JSON do przetworzenia.")

    documents = []
    for file_path in tqdm(json_files, desc="Wczytywanie dokumentów"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Sprawdzenie, czy wczytane dane są słownikiem (obiektem JSON)
            if not isinstance(data, dict):
                logging.warning(f"Plik {file_path} nie zawiera obiektu JSON (słownika). Pomijanie.")
                continue

            # Łączymy najważniejsze pola tekstowe w jeden spójny tekst
            content_parts = [
                data.get("title", ""),
                data.get("artist", ""),
                data.get("description", ""),
                data.get("text", ""),
                data.get("culture", ""),
                data.get("country", ""),
                data.get("dated", ""),
                data.get("medium", ""),
                data.get("style", "")
            ]
            page_content = ". ".join(part for part in content_parts if part and part.strip())

            # Zapisujemy kluczowe informacje do cytowania w metadanych
            metadata = {
                "source": f"https://collections.artsmia.org/art/{data.get('_id')}",
                "title": data.get("title", "Brak tytułu"),
                "accession_number": data.get("accession_number", "Brak numeru"),
                "artist": data.get("artist", "Artysta nieznany")
            }
            
            if page_content:
                documents.append(Document(page_content=page_content, metadata=metadata))

        except (json.JSONDecodeError, IOError) as e:
            logging.warning(f"Nie można wczytać lub zdekodować pliku {file_path}: {e}")

    logging.info(f"Pomyślnie wczytano i przetworzono {len(documents)} dokumentów.")
    return documents