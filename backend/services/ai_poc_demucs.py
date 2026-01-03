# services/ai_poc_demucs.py
# ======================
# Demucsによる音源分離のPoC（概念実証）用サービス

import os
import shutil
from pathlib import Path
from typing import List


# 必要なライブラリのインポート
from demucs.api import Separator 

# 処理結果を保存するディレクトリを定義（コンテナのルートから見たパス）
OUTPUT_DIR = Path("poc_outputs/demucs") 
# 注: このディレクトリはdocker-compose.ymlでボリュームマウントされていることが前提です。

async def separate_audio_test(audio_file_path: str) -> List[str]:
    """
    指定された音声ファイルから音源を分離し、ファイルを保存します。
    
    Args:
        audio_file_path: 入力となる音声ファイルへのパス (例: "test_audio.wav")
    
    Returns:
        生成された全出力ファイルのパスリスト
    """
    
    print(f"Demucs PoC: 処理結果ディレクトリ {OUTPUT_DIR} の準備を開始。")
    # 以前の残骸を削除し、新しいディレクトリを作成
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True) 
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True) 
    
    print(f"Demucsによる音源分離を開始します: {audio_file_path}")
    
    try:
        # Separator: Demucsの処理を行うクラス
        # モデル名は省略するとデフォルト（通常 htdemucs）が使われます。
        # 初回実行時、モデルファイルがダウンロードされます。（数GBあり時間がかかる）
        separator = Separator()
        
        # 音源分離を実行
        # [audio_file_path] のリストを渡し、処理結果を output_dir に保存
        separator.separate_files(
            [audio_file_path], 
            output_dir=OUTPUT_DIR
        )
        
        # 処理結果のファイルパスを取得し、リストで返す
        input_file_name_stem = Path(audio_file_path).stem
        output_sub_dir = OUTPUT_DIR / input_file_name_stem
        
        # 出力されたすべての.wavファイルのパスを取得
        separated_files = [str(p) for p in output_sub_dir.glob("*.wav")]
        return separated_files
        
    except Exception as e:
        print(f"Demucsの実行中にエラーが発生しました: {e}")
        return [f"ERROR: Demucs実行失敗 - {e}"]

# ----------------------------------------------------
# 外部からの呼び出し（routers/test_ai.py）から利用されます。
# ----------------------------------------------------