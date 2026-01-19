from openai import OpenAI
from config import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(prompt: str):
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
