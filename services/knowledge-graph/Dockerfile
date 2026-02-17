FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir networkx strawberry-graphql uvicorn

COPY . .

EXPOSE 8002

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
