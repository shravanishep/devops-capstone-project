FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN useradd --create-home appuser
RUN mkdir /data && chown appuser:appuser /data
USER appuser
ENV DATABASE_URL=sqlite:////data/accounts.db
EXPOSE 8080
CMD ["python", "app.py"]
