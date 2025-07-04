# FastAPI OpenAPI Tips and Tricks

[FastAPI](https://fastapi.tiangolo.com/features/#automatic-docs) auto-generates an OpenAPI documentation (`openapi.json`) for your API and renders the documentation with either [Swagger UI](https://github.com/swagger-api/swagger-ui) or [Redoc](https://github.com/Redocly/redoc) by default. For Swagger UI, FastAPI offers the built-in default route `/docs`, and for Redoc it provides the default route `/redoc`.

I'm on the journey to explore how to make the generated OpenAPI documentation as nice as possible with the configuration options FastAPI has to offer.
In this series I'm collecting helpful hints and tricks to make the most out of it. My aim is to create a clear and comprehensive auto-generated API documentation, which provides a good developer experience.

## Articles
> Note: Each linked article comes with a runnable code example.

* **[Reuse Project Version from `pyproject.toml` for FastAPI](./articles/fastapi-version-in-openapi/)**  
Explains, how the `version` key from the `pyproject.toml` file could be injected into FastAPI and shown as the version number of your backend application in the OpenAPI documentation.

* **[Use OpenAPI Tags to Document Groups of Endpoints in FastAPI](./articles/openapi-tag-metadata/)**  
Group FastAPI endpoints using OpenAPI tags to create clearer, more navigable API documentation — with the help of additional descriptions and external links.

* **[Workaround for Hierarchical Tags in FastAPI](./articles/hierarchical-tags-workaround/)**  
An approach for using a naming convention to visually represent nested structures in the generated OpenAPI documentation.


