"""Entrypoint for the FastAPI application.

This module provides:
- app: FastAPI application instance.
"""

from fastapi import FastAPI

from settings import AppSettings

settings = AppSettings()  # type: ignore[call-arg]

app = FastAPI(
    title="Example Backend",
    version=settings.project.version,
)
