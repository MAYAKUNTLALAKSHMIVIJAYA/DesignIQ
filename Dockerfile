# Stage 1: Build the Frontend
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build the Backend & Environment (HF Compliant)
FROM python:3.11-slim

# Set up a new user named "user" with user ID 1000 per HF requirements
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Install system dependencies (need to be root for this)
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt-lists/*
USER user

# Copy backend requirements and install
COPY --chown=user backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy everything else
COPY --chown=user . .

# Copy built frontend from Stage 1
COPY --from=frontend-builder --chown=user /app/frontend/dist /app/frontend/dist

# Set environment variables for OpenEnv
ENV PORT=7860
ENV API_BASE_URL=http://localhost:7860

# Expose the mandatory HF port
EXPOSE 7860

# Run the server on port 7860
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "7860"]
