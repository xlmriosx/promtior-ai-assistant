# Introduction

![Build Status](https://github.com/xlmriosx/promtior-ai-assistant/actions/workflows/cicd.yaml/badge.svg)
[![Documentation](https://img.shields.io/badge/docs-online-success)](https://docs-chat-promtior.shuhariko.com)

[![Backend](https://img.shields.io/badge/artifacts-latest-blue)](https://github.com/xlmriosx/promtior-ai-assistant/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/shuhariko/rag-promtior-shuhariko-com)](https://hub.docker.com/r/shuhariko/rag-promtior-shuhariko-com)

[![Frontend](https://img.shields.io/badge/artifacts-latest-blue)](https://github.com/xlmriosx/promtior-ai-assistant/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/shuhariko/chat-promtior-shuhariko-com)](https://hub.docker.com/r/shuhariko/chat-promtior-shuhariko-com)

[![Documentation](https://img.shields.io/badge/artifacts-latest-blue)](https://github.com/xlmriosx/promtior-ai-assistant/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/shuhariko/docs-promtior-shuhariko-com)](https://hub.docker.com/r/shuhariko/docs-promtior-shuhariko-com)


promtior-ai-assistant is a chat developed with Python using FastAPI, Pydantic, uvicorn, LangChain, LangServe and 
TypeScript using React, lucide-react, axios.

The infrastructure used was Azure and a VPS. To deploy it on Azure, manifests were created in Terraform and Ollama
server was deploy it using Helm to be used from the VPS.

# Relevant links

| Description    | Link |
|-----------|------|
| Ollama Server      | [ollama-llama2.shuhariko.com](https://ollama-llama2.shuhariko.com)   |
| Documentation      | [docs-chat-promtior.shuhariko.com](https://docs-chat-promtior.shuhariko.com)   |
| Backend     |  [rag-promtior.shuhariko.com](https://rag-promtior.shuhariko.com)  |
| Frontend     |  [chat-promtior.shuhariko.com](https://chat-promtior.shuhariko.com)   |

I recommend go to documentation to take a look of a detailed view of entire project.

# Instructions

To continue developing or test locally.

1. Clone the repo and later enter project folder.

- `git clone https://github.com/xlmriosx/promtior-ai-assistant.git`

- `cd promtior-ai-assistant`

2. Run docker compose.

- `docker compose up`

## Backend

1. Enter backend folder.

- `cd backend`

2. Create virtual env python.

- `python -m venv ve`

3. Install dependencies.

- `pip install -r requirements.txt`

4. Run the app.

- `uvicorn app.main:app --host 0.0.0.0 --port 8000`

5. Check in the browser in `localhost:8000`

## Frontend

1. Enter frontend folder.

- `cd frontend`

2. Install dependecies.

- `npm i`

3. Run the app.

- `npm start`

4. Check in the browser in `localhost:3000`

## Documentation

1. Enter backend folder.

- `cd docs`

2. Create virtual env python.

- `python -m venv ve`

3. Install dependencies.

- `pip install -r requirements.txt`

4. Run the app.

- `mkdocs serve`

5. Check in the browser in `localhost:8000`
