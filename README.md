```
├── .github/
│   └── workflows/
│       └── cicd.yaml
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── rag_chain.py
│   │   └── utils.py
│   ├── data/
│   │   └── AI Engineer.pdf
│   ├── chroma_db/ (temp and not must be uploaded)
│   ├── .dockerignore
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── logo.png
│   │   └── robots.txt
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── Header.tsx
│   │   │   ├── InputBox.tsx
│   │   │   └── MessageBubble.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   │   └── chat.ts
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── index.tsx
│   ├── .dockerignore
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── tailwind.config.js
│   └── tsconfig.json
├── manifests/
│   ├── ollama-helm/ (helm manifest to deploy ollama server)
│   └── virtualmachine/ (terraform manifests to deploy virtualmachine in Azure)
├── compose.yml
└── README.md
```