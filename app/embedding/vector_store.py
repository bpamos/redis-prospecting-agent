from langchain_redis import RedisVectorStore

def store_chunks_in_redis(chunks, embedding_model, index_name, redis_url):
    """Stores chunks as vectors in Redis."""
    from langchain_core.documents import Document

    docs = [Document(page_content=chunk) for chunk in chunks]
    RedisVectorStore.from_documents(
        docs,
        embedding_model,
        redis_url=redis_url,
        index_name=index_name,
    )
