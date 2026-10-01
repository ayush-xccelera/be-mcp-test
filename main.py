"""Minimal FastAPI service exposing health endpoints."""

import logging
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

logger = logging.getLogger(__name__)

app = FastAPI(title="Service Health API")


class HealthResponse(BaseModel):
    """Response schema returned by service health endpoints."""

    status: Literal["ok"]


def get_healthy_response() -> HealthResponse:
    """Return the service health response."""
    return HealthResponse(status="ok")


@app.get("/ok", response_model=HealthResponse)
def ok() -> HealthResponse:
    """Return the specified service health status."""
    logger.info("Health status requested at /ok")
    return get_healthy_response()


@app.get("/health", response_model=HealthResponse, include_in_schema=True)
def health() -> HealthResponse:
    """Provide the deployment-required unauthenticated health probe."""
    logger.info("Health status requested at /health")
    return get_healthy_response()
