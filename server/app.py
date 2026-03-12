from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "message": "Hello World! Pill-Sok Server is Running!",
        "status": "success"
    }

if __name__ == '__main__':
    # 도커 환경에서는 반드시 host를 0.0.0.0으로 설정해야 외부(앱, 파이)에서 접속 가능합니다.
    app.run(host='0.0.0.0', port=5000)