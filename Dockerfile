FROM python:3.11

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy the poetry lock and project files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy application and test directories
COPY app ./app
COPY tests ./tests

# Correct CMD syntax
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]