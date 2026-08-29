import os

from llm.prompt import build_movie_prompt
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY is missing from .env"
    )


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)


MODEL_NAME = "openai/gpt-oss-20b"


def generate_answer(
    question: str,
    context: str
) -> str:

    prompt = build_movie_prompt(
        question,
        context
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content