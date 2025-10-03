FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY predict.py .
COPY feature_engineering.py .
COPY models/ ./models/

ENTRYPOINT ["python", "predict.py"]