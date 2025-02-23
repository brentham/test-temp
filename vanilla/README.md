source .venv/bin/activate
uv run fastapi dev src/main.py
uvicorn src.main:app --reload