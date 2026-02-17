FROM python:3.10-slim

WORKDIR /app

COPY tools/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Environment variable for the orchestrator
ENV PYTHONPATH=/app

CMD ["python", "tools/orchestrator.py", "dashboard"]
