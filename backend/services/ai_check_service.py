# services/ai_check_service.py
# =============================
# AI関連ライブラリが正しくインポートできるか確認するサービス層

import importlib

async def check_libraries():
    """
    Demucs / Basic Pitch / Tayuya がインポート可能かを確認する。
    エラーがあってもサーバーが落ちないように安全にチェックする。
    """
    libraries = ["demucs", "basic_pitch", "tayuya"]
    status = {}

    for lib in libraries:
        try:
            importlib.import_module(lib)
            status[lib] = "✅ 読み込み成功"
        except ModuleNotFoundError:
            status[lib] = "❌ 未インストール"
        except Exception as e:
            status[lib] = f"⚠️ 読み込みエラー: {type(e).__name__}"

    return status
