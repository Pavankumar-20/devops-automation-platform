
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade setuptools wheel

COPY app/ ./app/

CMD ["python", "app/metrics_server.py"]



