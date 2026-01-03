# main.py
# ==========================
from fastapi import FastAPI
from routers import test_ai  # ← 追加：新しいルーターを読み込む

app = FastAPI(title="Guitar Tab Generator API")

# ルーターを登録
app.include_router(test_ai.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI! (Backend is running)"}
