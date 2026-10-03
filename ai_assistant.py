import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is not set. "
        "Create a .env file and add your API key."
    )

client = OpenAI(api_key=api_key)


def generate_product_description(
    product_name: str,
    category: str,
    features: str,
) -> str:
    prompt = f"""
Create a professional e-commerce product description.

Product: {product_name}
Category: {category}
Features: {features}

Write:
1. A short product description
2. 5 key selling points
3. A clear call to action

Keep the language natural and suitable for an online store.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt,
    )

    return response.output_text


if __name__ == "__main__":
    result = generate_product_description(
        "Smart Wireless Earbuds",
        "Audio",
        "Bluetooth, long battery life, compact design",
    )

    print(result)
