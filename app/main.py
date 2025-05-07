from ingestion.website_scraper import crawl_website
from embedding.chunker import chunk_text
from embedding.embedder import get_embedding_model
from embedding.vector_store import store_chunks_in_redis
from agents.fit_analyzer import get_fit_suggestion_chain
from config import settings
import uuid

def run(url: str):
    print(f"🔍 Scraping {url}...")
    raw_text = crawl_website(url)

    print("✂️ Chunking...")
    chunks = chunk_text(raw_text)

    print("🔢 Embedding and storing in Redis...")
    embedding_model = get_embedding_model()
    index_name = f"company:{uuid.uuid4().hex[:8]}"
    store_chunks_in_redis(chunks, embedding_model, index_name, settings.REDIS_URL)

    print("🧠 Analyzing Redis Fit...")
    chain = get_fit_suggestion_chain()
    response = chain.invoke({"context": "\n".join(chunks[:5])})
    print("\n=== Redis Fit Suggestions ===")
    print(response)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python app/main.py https://company.com")
        exit(1)

    run(sys.argv[1])
