# 💊 약속 (Pill-Sok)
> **AI 및 IoT 기술을 접목한 개인 맞춤형 헬스케어 스마트 약통 & 에이전트**

**'약속'**은 "약(Pill) 복용 시간을 지키는 약속"이라는 의미를 담고 있습니다. AI 융합 기술을 활용하여 사용자의 복약 오남용을 방지하고, 24시간 맞춤형 건강 상담을 제공하는 차세대 헬스케어 솔루션입니다.

---

## 📂 Project Structure

프로젝트의 전체 구조와 각 폴더별 상세 역할입니다.


```text
AI-Healthcare/
├── app/                  # Flutter 모바일 애플리케이션 (사용자 UI/UX)
│   ├── lib/
│   │   ├── models/       # 데이터 모델 (Pill, User, History)
│   │   ├── screens/      # 홈화면, 챗봇상담, 카메라 인식, 복약일기 화면
│   │   ├── services/     # API 통신(Flask 연동) 및 푸시 알림 로직
│   │   └── widgets/      # 약 정보 시각화 및 UI 컴포넌트
│   └── pubspec.yaml      # 앱 패키지 관리 설정
├── server/               # Flask 백엔드 API 서버
│   ├── api/              # 기능별 엔드포인트 (인식 결과 처리, 재고 관리)
│   ├── core/             # DB 연동 및 LLM(GPT/Gemini) 에이전트 로직
│   ├── app.py            # Flask 메인 실행 파일
│   └── requirements.txt  # 서버 라이브러리 의존성 파일
├── ai/                   # AI 모델 개발 및 분석 (PyTorch 기반)
│   ├── models/           # 학습된 ViT / CLIP 커스텀 모델 가중치 (.pt)
│   ├── src/              # 이미지 전처리 및 모델 추론(Inference) 코드
│   └── notebooks/        # 데이터 분석 및 모델 학습 실험 기록
├── iot/                  # 라즈베리파이 하드웨어 제어부
│   ├── sensors/          # 진동 모듈, 카메라, 거리 센서 제어 코드
│   └── main_pi.py        # 라즈베리파이 하드웨어 메인 컨트롤러
├── database/             # 데이터베이스 관리
│   ├── schema.sql        # MySQL 테이블 구조 (Users, Pills, Inventory)
│   └── seed_data.sql     # 초기 약학 기초 데이터 및 상비약 데이터셋
└── README.md             # 프로젝트 소개 및 가이드