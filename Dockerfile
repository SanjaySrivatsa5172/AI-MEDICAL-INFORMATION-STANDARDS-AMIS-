FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PORT=8765 \
    HOST=0.0.0.0

COPY implementation/web/requirements.txt /app/implementation/web/requirements.txt
RUN pip install --no-cache-dir -r /app/implementation/web/requirements.txt

COPY standards /app/standards
COPY examples /app/examples
COPY implementation /app/implementation

EXPOSE 8765
CMD ["sh", "-c", "python -m uvicorn implementation.web.app:app --host 0.0.0.0 --port ${PORT:-8765}"]
