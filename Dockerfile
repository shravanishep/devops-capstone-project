# Step 1: Base image
FROM python:3.9-slim

# Step 2: Working directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application files
COPY accounts/ ./accounts/
COPY service/ ./service/
COPY app.py .

# Step 5: Switch to a non-root user
RUN useradd --uid 1000 --create-home appuser && \
    mkdir -p /data && \
    chown -R appuser:appuser /data /app

USER appuser

ENV DATABASE_URL=sqlite:////data/accounts.db
ENV PORT=8080

EXPOSE 8080

# Step 6: Run the service
CMD ["gunicorn", "--log-level=info", "--bind=0.0.0.0:8080", "service:app"]
