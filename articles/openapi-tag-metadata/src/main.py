from fastapi import FastAPI, status

from tags import Tags, tags_metadata

app = FastAPI(
    title="Example Backend",
    openapi_tags=tags_metadata,
)


@app.get(path="/v1/product/{product_id}", tags=[Tags.products])
async def get_product(product_id: int) -> None:
    """Returns the product with the given ID."""


@app.get(path="/v1/product/search", tags=[Tags.products])
async def search_for_products() -> None:
    """Returns list of products that match the search criteria."""


@app.get(path="/v1/order/{order_id}", tags=[Tags.orders])
async def get_order(order_id: int) -> None:
    """Returns the order with the given ID.

    The currently logged in user is only able to retrieve the details of an order they placed.
    """


@app.post(path="/v1/account/password/change", status_code=status.HTTP_204_NO_CONTENT, tags=[Tags.accounts])
async def change_password() -> None:
    """The currently logged in user is able to change the password for it's own user account."""


@app.post(path="/v1/account/password/request-reset", status_code=status.HTTP_202_ACCEPTED, tags=[Tags.accounts])
async def request_password_reset() -> None:
    """Starts a password reset flow for a user account.

    The user will receive an email with a link to reset the password.
    By receiving the email and clicking the link, the user proves to be the legimitate owner of the account.
    The link will be valid for 30 minutes and opens a page where the user can set a new password.
    """


@app.post(path="/v1/account/password/reset", status_code=status.HTTP_204_NO_CONTENT, tags=[Tags.accounts])
async def reset_password() -> None:
    """Finishes a password reset flow for a user account.

    The user has clicked the reset link in the email and set a new password, which is received in the request body.
    """
