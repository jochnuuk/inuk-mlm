# InukMLM

InukMLM is a local-first multilingual language technology workspace for Greenlandic-Danish retrieval, document processing, and RAG workflows.

## Stack

- DuckDB for local development
- PostgreSQL/pgVector for server or enterprise deployment
- RAGLite for retrieval and MCP/Chainlit interfaces
- Ibis for portable dataframe and SQL workflows
- n8n for orchestration and automation
- bge-m3 for multilingual embeddings
- Ollama for local LLM inference

## Goals

- Build Greenlandic-Danish parallel corpus workflows
- Support local-first and offline-capable development
- Keep migration path from laptop to server simple
- Enable civic-tech and language technology projects for Greenland

## Structure

- `app/` application code
- `data/` local DuckDB and sample corpus files
- `notebooks/` experiments and evaluation
- `infra/` Docker Compose and environment templates
- `docs/` architecture and ingestion notes

## Quick start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
```
