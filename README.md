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

📅 Daily Workflow (출근 및 협업 루틴)
👥 팀원들이 출근해서 해야 할 일
최신 코드 가져오기: git pull origin main으로 어제 업데이트된 내용을 반영합니다.

도커 환경 동기화: requirements.txt가 바뀌었을 수 있으니 docker-compose up --build -d를 실행합니다.

작업 브랜치 확인: 현재 자신의 기능 브랜치(feat/기능이름)에 있는지 확인하고 작업을 시작합니다.

퇴근 전 Push: 오늘 작업한 내용은 반드시 본인의 브랜치에 push하고 퇴근합니다. (내 PC가 고장 나도 코드는 살려야 합니다!)

👑 팀장(나)이 체크해야 할 일
PR 코드 리뷰 및 머지: 팀원들이 올린 Pull Request를 확인하고 main 브랜치에 합칩니다.

라이브러리 통합 관리: 팀원들이 추가하고 싶어 하는 패키지가 있다면 server/requirements.txt에 직접 추가하여 배포합니다.

모델 가중치 업데이트: AI 학습 결과가 새로 나오면 구글 드라이브에 올리고 팀원들에게 공지합니다.

환경 설정 오류 지원: 팀원들의 도커나 깃이 꼬였을 때 위 가이드를 바탕으로 해결해 줍니다.

⚠️ 필수 주의사항 (Project Ground Rules)
1. 깃허브에 절대 올리지 말 것 (Security & Size)
AI 모델 파일 (.pt, .h5): 100MB가 넘으면 깃이 터집니다. 반드시 구글 드라이브를 이용하세요.

API Key / DB 비밀번호: Gemini나 OpenAI 키를 깃허브에 올리면 전 세계에서 내 카드를 결제하게 됩니다. .env 파일을 활용하세요.

학습용 데이터셋: 수천 장의 약 사진은 개인 PC나 드라이브에만 보관하세요.

2. 코딩 시 약속
경로(Path) 설정 주의: 파일 경로는 항상 os.path.join()을 사용하여 윈도우와 리눅스(도커) 환경 모두에서 동작하게 짭니다.

하드코딩 금지: IP 주소나 포트 번호 등을 코드 안에 직접 적지 말고 설정 파일로 관리합니다.

3. 도커 관련
DB 데이터 삭제 주의: docker-compose down 명령어는 컨테이너를 삭제합니다. 데이터베이스에 저장한 테스트 데이터가 사라질 수 있으니 중요 데이터는 백업해 두세요.

도커를 켠 채로 테스트: 가상환경(venv)을 켜지 말고, 항상 도커가 돌아가고 있는 상태에서 localhost:5000으로 접속해 기능을 테스트합니다.

🛠️ 팀원용 서버 개발 세팅 가이드
팀장님이 이미 모든 환경을 도커 박스에 담아두었습니다. 여러분은 아래 순서대로 실행만 하면 즉시 코딩이 가능합니다.

1단계: 프로그램 설치 (최초 1회)
Docker Desktop 설치: 공식 홈페이지에서 다운로드 후 설치하세요.

WSL 2 업데이트 (Windows 사용자만): 터미널(PowerShell)을 관리자 권한으로 열고 아래 명령어를 입력하세요.

Bash
wsl --update
Docker Desktop 실행: 설치 후 프로그램을 실행하고 로그인이 뜨면 넘어가도 좋습니다. 설정에서 Use the WSL 2 based engine이 켜져 있는지 확인하세요.

2단계: 코드 가져오기 및 실행
저장소 클론:

Bash
git clone [우리팀-레포지토리-주소]
cd AI-Healthcare
도커 컨테이너 실행: (프로젝트 루트 폴더에서 입력)

Bash
docker-compose up --build
참고: 첫 실행 시에는 파이썬과 라이브러리를 다운로드하느라 2~3분 정도 걸립니다. 완료 후 Done이 뜨면 성공입니다!

3단계: 확인
브라우저를 열고 http://localhost:5000에 접속합니다.

화면에 **"💊 Pill-Sok 서버가 도커에서 정상 작동 중입니다!"**라는 문구가 뜨면 세팅 끝입니다.

✍️ 앞으로 코딩할 때 규칙
가상환경(venv) 만들지 마세요: 도커가 이미 가상환경입니다.

라이브러리 직접 설치 금지: pip install 하지 마세요. 대신 server/requirements.txt에 필요한 라이브러리 이름을 적고 파일을 저장하세요. 그다음 터미널에서 Ctrl+C로 껐다가 다시 docker-compose up --build를 하면 도커가 알아서 설치해 줍니다.

실시간 반영: server/app.py 코드를 수정하고 저장하면, 도커를 껐다 켤 필요 없이 즉시 반영됩니다. (Volumes 설정 덕분!)