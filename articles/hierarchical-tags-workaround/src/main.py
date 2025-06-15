from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from tags import Tags, tags_metadata

app = FastAPI(
    title="Example Backend",
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"docExpansion": "none"},  # collapse all tags
)


class B2CCustomer(BaseModel):
    """B2C Customer response model."""

    id: int
    name: str
    email: str


b2c_customers = {
    1: B2CCustomer(id=1, name="Alice", email=""),
    2: B2CCustomer(id=2, name="Bob", email=""),
}


@app.get("/v1/customer/b2c", tags=[Tags.customers_individual])
async def list_b2c_customers() -> list[B2CCustomer]:
    """List all private customers (B2C)."""
    return list(b2c_customers.values())


@app.get(path="/v1/customer/b2c/{customer_id}", tags=[Tags.customers_individual])
async def get_b2c_customer(customer_id: int) -> B2CCustomer:
    """Get private customer (B2C)."""
    customer = b2c_customers.get(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
