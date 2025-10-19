# 1. Pythonの公式イメージを指定
FROM python:3.11-slim-buster

# 2. コンテナ内部の作業ディレクトリを設定
WORKDIR /app

# 3. requirements.txtをコピーしてライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. アプリケーション本体のコードをコピー
COPY . .

# 5. アプリケーション実行コマンド (docker composeで上書きされるが記述)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
