# 1. Pythonの公式イメージ（buster は EOL → slim の最新を使う）
FROM python:3.10-slim

# 2. 必要なシステム依存パッケージ
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libsndfile1 \
    build-essential \
    libmp3lame-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. 作業ディレクトリ
WORKDIR /app

# 4. Python依存ライブラリ
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. アプリコード
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
