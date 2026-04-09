FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.5.9 AS uv
FROM --platform=linux/amd64 python:3.13-slim-bookworm
COPY --from=uv /uv /uvx /bin/

WORKDIR /simple-service
COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --frozen
COPY ./app ./app

ENV PYTHONPATH=app
CMD [ "uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
EXPOSE 10000
