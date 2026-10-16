FROM python:3.11-slim

WORKDIR /app

# Instala curl para testes de conexão e saúde
RUN apt-get update && apt-get install -y --no-install-recommends curl libpq5 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5680

CMD ["python", "-u", "main.py"]
