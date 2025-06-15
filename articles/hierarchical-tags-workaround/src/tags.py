from enum import Enum
from typing import Any


class Tags(str, Enum):
    customers = "Customers"
    customers_individual = "Customers · Individual"
    customers_business = "Customers · Business"
    customers_business_domestic = "Customers · Business · Domestic"
    customers_business_international = "Customers · Business · International"
    orders = "Orders"
    products = "Products"


# the order of the tags in the Enum class defines the order of the tags in the API documentation
tags_metadata: list[dict[str, Any]] = [{"name": tag.value} for tag in Tags]
