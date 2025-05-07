from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from config import settings

def get_fit_suggestion_chain():
    prompt = ChatPromptTemplate.from_template("""
You are a solution architect at Redis. Given the following company context, suggest where Redis could fit in their stack or how it might improve their architecture.

Company Website Context:
{context}

Respond in bullet points.
""")
    llm = ChatOpenAI(model_name=settings.OPENAI_MODEL, temperature=0, api_key=settings.OPENAI_API_KEY)
    return prompt | llm  # RunnableSequence
