FROM python:3.9-slim

# 시스템 라이브러리 설치 (패키지명을 libgl1으로 수정)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]