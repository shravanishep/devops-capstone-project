FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY accounts/ ./accounts/
COPY app.py .

# Create non-root user and prepare data directory
RUN useradd --create-home appuser && \
    mkdir -p /data && \
    chown -R appuser:appuser /data /app

USER appuser

ENV DATABASE_URL=sqlite:////data/accounts.db
ENV PORT=8080

EXPOSE 8080

CMD ["python", "app.py"]

