from fastapi import FastAPI
# 開発中のため、相対パスでルーターをインポートします
from .routers import tab_generator

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# ルーター（コントローラー群）の登録
# tab_generator.pyで定義されたルートが有効になります
app.include_router(tab_generator.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI! (Backend is running)"}