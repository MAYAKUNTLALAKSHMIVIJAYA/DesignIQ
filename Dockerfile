FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask fastapi uvicorn numpy pandas

CMD ["python", "inference.py"]