# Service Health API

A minimal unauthenticated FastAPI service.

## Run locally

```sh
pip install -r requirements.txt
./start.sh
```

The service listens on port 8000.

- `GET /ok` returns `{"status":"ok"}`.
- `GET /health` is the deployment health probe.
- `GET /docs` serves FastAPI's Swagger UI.
- `GET /openapi.json` serves the OpenAPI schema.

## Test

```sh
pytest -q
```

## Container

```sh
docker compose up --build
```
