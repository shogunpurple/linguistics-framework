FROM python3.8-slim

CMD ["poetry", "run", "python", "src/server.py"]