"""
AI E-Commerce Assistant
An open-source toolkit for common e-commerce content workflows.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    name: str
    category: str
    price: float
    features: List[str]


def generate_product_description(product: Product) -> str:
    features = ", ".join(product.features)

    return (
        f"{product.name} is a practical {product.category} designed for "
        f"customers who value quality and everyday usability. "
        f"Key features include {features}. "
        f"With a price of ${product.price:.2f}, it offers a clear value "
        f"for customers looking for a reliable {product.category}."
    )


def generate_faq(product: Product) -> List[str]:
    return [
        f"What is {product.name}?",
        f"What are the main features of {product.name}?",
        f"How much does {product.name} cost?",
        f"Who is {product.name} suitable for?",
    ]


def recommend_products(
    products: List[Product],
    category: str,
    max_price: float
) -> List[Product]:
    return [
        product
        for product in products
        if product.category.lower() == category.lower()
        and product.price <= max_price
    ]


def main():
    products = [
        Product(
            name="Smart Wireless Earbuds",
            category="audio",
            price=39.99,
            features=[
                "Bluetooth connectivity",
                "compact design",
                "long battery life"
            ],
        ),
        Product(
            name="Portable Power Bank",
            category="accessories",
            price=29.99,
            features=[
                "fast charging",
                "USB-C support",
                "portable design"
            ],
        ),
    ]

    product = products[0]

    print("=" * 50)
    print("AI E-COMMERCE ASSISTANT")
    print("=" * 50)

    print("\nPRODUCT DESCRIPTION")
    print(generate_product_description(product))

    print("\nFAQ")
    for question in generate_faq(product):
        print(f"- {question}")

    print("\nRECOMMENDATIONS")
    recommendations = recommend_products(products, "audio", 50)

    for item in recommendations:
        print(f"- {item.name}: ${item.price:.2f}")


if __name__ == "__main__":
    main()
