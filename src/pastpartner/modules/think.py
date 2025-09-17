import os
from openai import OpenAI

BASE_PROMPT = """
    Repond a mon message avec un francais soutenu et des phrases completes.
    garde ta reponse bref, maximum 3 phrases. Tu es un assistant robot.
    Mon message:
    """


def think(message: str) -> str | None:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
    )

    prompt = BASE_PROMPT + message

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
