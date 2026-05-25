import os

import anthropic
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT, build_prompt

load_dotenv()

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 2048


def generate_diagnosis(data: dict) -> str:
    """
    Generuje diagnozę marketingową na podstawie danych z formularza.

    Args:
        data: słownik z danymi zebranymi przez formularz (wszystkie 5 kroków)

    Returns:
        Tekst diagnozy w markdown

    Raises:
        ValueError: gdy brak klucza API
        anthropic.APIError: gdy błąd po stronie API
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "Brak klucza ANTHROPIC_API_KEY. "
            "Ustaw go w pliku .env lub jako zmienną środowiskową."
        )

    client = anthropic.Anthropic(api_key=api_key)
    user_prompt = build_prompt(data)

    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
    )

    return message.content[0].text
