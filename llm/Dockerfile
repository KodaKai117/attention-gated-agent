FROM python:3.11-slim

WORKDIR /app
RUN pip install fastapi uvicorn

COPY wrapper.py .

CMD ["uvicorn", "wrapper:app", "--host", "0.0.0.0", "--port", "8000"]
