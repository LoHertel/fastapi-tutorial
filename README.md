# FastAPI OpenAPI Tips and Tricks

[FastAPI](https://fastapi.tiangolo.com/features/#automatic-docs) auto-generates an OpenAPI documentation (`openapi.json`) for your API and renders the documentation with either [Swagger UI](https://github.com/swagger-api/swagger-ui) or [Redoc](https://github.com/Redocly/redoc) by default. For Swagger UI, FastAPI offers the built-in default route `/docs`, and for Redoc it provides the default route `/redoc`.

I'm on the journey of making the generated OpenAPI documentation as nice as possible with the configuration options FastAPI has to offer.
In this series I'm collecting helpful hints and tricks to make the most out of it. My aim is to create a clear and comprehensive auto-generated API documentation, which provides a good developer experience.

## Articles
> Note: Each linked article comes with a runnable code example.
