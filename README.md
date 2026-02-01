RC - Python GUI Application
PyQt5와 SQLite를 활용한 사용자 관리 시스템 프로젝트입니다. 회원가입, 로그인 및 관리자용 데이터 조회/수정 기능을 제공합니다.

🚀 주요 기능
회원 관리: 아이디, 비밀번호, 이름, 이메일, 성별 정보를 포함한 회원가입 기능.

사용자 로그인: SQLite 연동을 통한 사용자 인증.

관리자 모드:

사용자 조회 (Select): 등록된 사용자 목록을 테이블 형태로 조회.

사용자 수정 (Update): 실시간 또는 수동 제출 방식으로 사용자 정보 수정.

보안 설정: QRegExpValidator를 이용한 입력값 제한 및 비밀번호 마스킹 처리.

📂 프로젝트 구조
Plaintext
GUIAPP/
├── app_main.py # 애플리케이션 메인 엔트리 포인트 (QStackedWidget 관리)
├── db/ # 데이터베이스 파일 폴더
│ └── Rc.db # SQLite 데이터베이스 파일
├── models/ # 데이터 처리 및 연결 모듈
│ └── db_connect.py # QSqlDatabase 연결 설정
├── screens/ # 화면별 비즈니스 로직 클래스
│ ├── admin_screen.py # 관리자 메인 화면
│ ├── login_screen.py # 로그인 화면
│ ├── select_screen.py # 사용자 조회 화면
│ ├── signup_screen.py # 회원가입 화면
│ └── update_screen.py # 사용자 수정 화면
├── ui/ # Qt Designer로 제작한 .ui 파일
├── widgets/ # 공통 설정 및 위젯 관리
│ ├── gui_setup.py # .ui 파일 로드 유틸리티
│ └── widget_manager.py # 전역 위젯 인스턴스 관리
└── README.md # 프로젝트 설명 파일
🛠 설치 및 실행 방법
의존성 라이브러리 설치

Bash
pip install PyQt5
애플리케이션 실행

Bash
python GUIAPP/app_main.py
📝 개발 노트
UI 로딩: uic.loadUiType을 사용하여 .ui 파일을 동적으로 로드합니다.

화면 전환: QStackedWidget을 사용하여 여러 화면을 하나의 윈도우에서 전환하며 관리합니다.

데이터베이스: PyQt5.QtSql 모듈의 QSqlTableModel과 QSqlQuery를 활용하여 DB 작업을 수행합니다.

👨‍💻 관리자 계정 (개발용)
ID: admin

PW: 1234

로그인 화면의 Dev ONLY 버튼을 클릭하여 빠르게 입력할 수 있습니다.
