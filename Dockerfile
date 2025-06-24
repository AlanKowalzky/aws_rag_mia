# Użyj oficjalnego obrazu Python jako bazowego
FROM python:3.11-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Zainstaluj zależności systemowe, jeśli są potrzebne (np. git do pobierania danych)
RUN apt-get update && apt-get install -y git curl unzip && rm -rf /var/lib/apt/lists/*

# Skopiuj plik z zależnościami i zainstaluj je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę kodu aplikacji do katalogu roboczego
COPY . .

# Domyślna komenda, która zostanie wykonana (możemy ją nadpisać w GitHub Actions)
CMD ["python", "-m", "src.scripts.ingest"]