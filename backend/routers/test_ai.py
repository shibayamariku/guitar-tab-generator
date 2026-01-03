# routers/test_ai.py
# ======================
# AIライブラリの動作確認APIのルーター定義

from fastapi import APIRouter
from services import ai_check_service  # サービス層をインポート
from services import ai_poc_demucs  # Demucs PoCサービスをインポート
from fastapi import UploadFile, File
from services.ai_poc_demucs import separate_audio_test
import shutil

# APIRouter：FastAPIで複数のAPIルートをまとめる仕組み
router = APIRouter(prefix="/test", tags=["AIチェック"])

@router.get("/ai-status")
async def check_ai_status():
    """
    AI関連ライブラリ（Demucs, BasicPitch, Tayuya）の
    読み込み状態を確認するテスト用エンドポイント。
    """
    result = await ai_check_service.check_libraries()
    return {"status": result}

@router.post("/demucs")
async def run_demucs(file: UploadFile = File(...)):
    """
    アップロードされた音声ファイルに対してDemucsによる音源分離を実行するテスト用エンドポイント。
    """
    # 一時的にファイルを保存
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Demucsによる音源分離を実行
    separated_files = await ai_poc_demucs.separate_audio_test(temp_file_path)
    
    return {"separated_files": separated_files}