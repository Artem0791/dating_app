FROM python:3.11

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry install --no-dev --no-interaction --no-ansi

COPY app ./app
COPY tests ./tests

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]