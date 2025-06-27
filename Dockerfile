FROM python:3.12-slim

WORKDIR /app

# _________

# RUN pip install poetry

# COPY pyproject.toml poetry.lock ./

# RUN poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi --no-root

# RUN apt-get update && apt-get upgrade -y && apt-get clean

# RUN poetry cache clear pypi --all && \
#     rm -rf /root/.cache/pip

# _________ 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]



