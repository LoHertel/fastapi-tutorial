from enum import StrEnum
from typing import Any


class Tags(StrEnum):
    accounts = "Accounts"
    orders = "Orders"
    products = "Products"


# the order of the tags defines the order of the groups in the API documentation
tags_metadata: list[dict[str, Any]] = [
    {
        "name": Tags.accounts,
        "description": "An account allows a *customer* to **log in** and **manage their personal data**.",
        "externalDocs": {
            "description": "👤 User Management System",
            "url": "https://example.net/admin/users/",
        },
    },
    {
        "name": Tags.orders,
        "description": "An order is a **collection of products** that a *customer* has purchased.",
    },
    {
        "name": Tags.products,
        "description": "A product is an **item** that can be purchased by a *customer*.",
        "externalDocs": {
            "description": "📚 Product Catalog",
            "url": "https://example.net/products/",
        },
    },
]
