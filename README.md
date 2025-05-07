# redis-prospecting-agent
redis prospecting agent

The **Redis Prospecting Agent** is a Redis-powered agentic workflow application that scrapes a company’s public website, chunks and embeds its content, stores structured and vectorized memory in Redis, and analyzes where Redis fits into their technology stack using RAG over a Redis corpus.

Designed for GTM engineers, solution architects, and platform sellers, this agent generates Redis opportunity insights—fast, smart, and demo-ready.

---

## 🚀 Features

- ✅ Website scraping + embedding
- ✅ RedisVL vector search + hybrid retrieval
- ✅ RedisJSON for structured memory & metadata
- ✅ RedisChatMessageHistory for per-session short-term memory
- ✅ Semantic Routing + Semantic Caching
- ✅ RAG with Redis corpus (blogs, docs)
- ✅ Optional Gradio or Streamlit interface
- ✅ RAGAS evaluation scoring
- 🛠️ Extensible modules for scraping, embedding, routing, and memory
- 📊 [Coming Soon] Google Slides export of summary and fit report

---

## 🧱 Architecture Overview

[Website URL] → [Scraper] → [Chunk + Embed] → [Redis]

[Redis Vector Store] ←→ [Fit Analyzer / Redis RAG] ←→ [LLM]
↑ ↓
[Semantic Router / Cache] [JSON Memory & Chat Logs]

## 📁 Folder Structure

```bash
redis-prospecting-agent/
├── app/                  # Core logic: agents, memory, UI, embedding
├── data/                 # Redis docs, company snapshots
├── notebooks/            # Demos and exploration
├── tests/                # Unit tests
├── tools/                # Slides export, RAGAS runner
├── requirements.txt
├── .env.example
└── README.md
```

## 🛠️ Getting Started

1. Clone the repo
```bash
git clone https://github.com/your-org/redis-prospecting-agent.git
cd redis-prospecting-agent
# install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# setup your .evn
# create a .env file from the template:
cp .env.example .env
```
Fill in:
* REDIS_URL=redis://your-redis-url
* OPENAI_API_KEY=...
* COHERE_API_KEY=... (optional for reranking)

2. Run the app
```bash
#gradio ui
python app/main.py
```

## Built With
* LangChain
* RedisVL
* RedisJSON + RedisSearch
* Gradio
* FastAPI
* RAGAS