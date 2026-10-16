"""AI Sentiment Analyzer — Gemini API integration demo.

Part of python-portfolio. Demonstrates environment-based API key
management, structured (JSON) prompt engineering and error handling.
"""

import os
import sys

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

PROMPT_TEMPLATE = (
    "Classify the sentiment of the text below as POSITIVE, NEGATIVE or NEUTRAL. "
    'Respond ONLY with valid JSON: '
    '{{"sentiment": "<label>", "confidence": <0-1>, "reason": "<one sentence>"}}\n\n'
    "Text: {text}"
)


def build_client() -> genai.Client:
    if not API_KEY:
        sys.exit(
            "ERROR: GEMINI_API_KEY not found. Set it in a .env file "
            "(see README) or as an environment variable."
        )
    return genai.Client(api_key=API_KEY)


def analyze_sentiment(client: genai.Client, text: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT_TEMPLATE.format(text=text),
    )
    return response.text.strip()


def main() -> None:
    print("--- AI Sentiment Analyzer ---")
    print(f"Python: {sys.version.split()[0]} | Model: {MODEL}")

    text = input("\nEnter text to analyze: ").strip()
    if not text:
        print("No text provided. Exiting.")
        return

    client = build_client()
    try:
        print(f"\nAI Result: {analyze_sentiment(client, text)}")
    except Exception as exc:
        print(f"\nERROR: request failed -> {exc!r}")
        print("Check: (1) API key validity, (2) model name, (3) network.")


if __name__ == "__main__":
    main()