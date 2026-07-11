# Architecture

## Local-first path

1. DuckDB stores local corpus, metadata, and experiments.
2. Ibis provides a portable query layer for analytics and transformations.
3. RAGLite can later use DuckDB locally or PostgreSQL remotely.
4. Ollama serves local language models.
5. n8n can be added for ingestion and workflow automation.

## Enterprise path

- Replace `DB_URL` with PostgreSQL connection string.
- Keep application code mostly unchanged.
- Add pgVector and operational services behind Docker Compose or Kubernetes.
