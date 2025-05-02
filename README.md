# Rc
first Project by Python PYQT5, sqlite


git status      # 변경 확인
git add .       # 변경 파일 스테이지에 올림
git commit -m "변경 내용 메시지"  # 커밋
git push        # 원격 저장소로 푸시 (필요시)

P2/
├── .venv/                    # 가상 환경
├── Rc/                       # 메인 패키지 폴더
│   ├── __init__.py           # 패키지 초기화 파일
│   ├── gui_setup.py          # UI 로딩 및 설정
│   ├── database_connect.py   # 데이터베이스 연결 관련 모듈
│   ├── ui/                   # UI 파일들이 위치하는 폴더
│   │   ├── login.ui          # 로그인 화면 UI
│   │   ├── main.ui           # 메인 화면 UI
│   │   └── admin.ui          # 관리자 화면 UI
│   ├── screens/              # 화면 클래스를 위한 폴더
│   │   ├── login_screen.py   # 로그인 화면 클래스
│   │   ├── main_screen.py    # 메인 화면 클래스
│   │   └── admin_screen.py   # 관리자 화면 클래스
│   ├── widgets/              # 위젯 클래스를 위한 폴더
│   │   ├── custom_widget.py  # 커스텀 위젯 클래스
│   │   ├── menu_widget.py    # 메뉴 위젯 클래스
│   │   └── ...               # 추가 위젯 클래스
│   ├── models/               # 모델 관련 파일 (데이터베이스 처리 등)
│   │   ├── user_model.py     # 사용자 모델
│   │   ├── transaction_model.py # 거래 모델
│   │   └── ...               # 추가 모델 클래스
│   ├── Readme.txt            # 프로젝트 설명 파일
│   ├── Rc.db                 # 데이터베이스 파일
├── app_main.py               # 애플리케이션의 메인 엔트리 포인트
├── requirements.txt          # 의존성 관리 파일
├── .gitignore                # Git에서 제외할 파일/폴더 설정
├── README.md                 # 프로젝트 설명 파일 (GitHub용)
└── setup.py                  # 패키지 설치 및 배포 설정 파일 (옵션)
