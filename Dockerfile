FROM python:3.8-slim

RUN pip install poetry

EXPOSE 3001

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
# copy frontend to static dir
COPY ui/public/build/* /app/static/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY src /app/

CMD ["poetry", "run", "python", "server.py"]