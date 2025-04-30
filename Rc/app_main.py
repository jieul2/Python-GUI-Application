#==========메인 윈도우==========#



import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
import sqlite3
from gui_setup import loadUi
from database_connect import *
from login_window import LoginWindow 
from admin_menu import AdminMenu
from widget_manager import widget as shared_widget
import widget_manager

# 메인 ui겸 메인 윈도우
class MainWindow(QMainWindow, loadUi('Rc/ui/main.ui')):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionLogin.triggered.connect(self.login_action)       # 로그인 액션
        self.actionCreate_Account.triggered.connect(self.create_account_action) # 계정 생성 액션
    

        self.loginbutton.clicked.connect(self.login_action)  # 로그인 버튼 클릭 시 동작하는 함수
        self.regbutton.clicked.connect(self.create_account_action)  # 계정 생성 버튼 클릭 시 동작하는 함수

        self.pushbutton.clicked.connect(self.pushButtonClicked) # 버튼 클릭 시 동작하는 함수
        self.dial.valueChanged.connect(self.dialValueChanged) # 다이얼 값 변경 시 동작하는 함수

    def login_action(self):
            # 로그인 버튼 클릭 시 동작하는 함수
            print(f"Login Action Triggered")
            widget.setCurrentIndex(widget.indexOf(LoginWindow))
            # widget.setCurrentIndex(0)  # MainWindow로 돌아가기
            # widget.setCurrentIndex(1)  # LoginWindow로 이동
            

    def create_account_action(self):
            # 계정 생성 버튼 클릭 시 동작하는 함수
            print(f"Create Account Action Triggered")
            widget.setCurrentIndex(widget.indexOf(MainWindow))  #
            # widget.setCurrentIndex(0)  # MainWindow로 돌아가기
            # widget.setCurrentIndex(1)  # LoginWindow로 이동

    def dialValueChanged(self):
        # 다이얼 값 변경 시 동작하는 함수=
        self.lcdNumber.display(self.dial.value())

    def pushButtonClicked(self):
        QMessageBox.information(self, "Info", f"다이얼은 = {int(self.lcdNumber.value())} 입니다.")






#---------------------------------#
#---------------메인--------------#
#---------------------------------#

connection = connect_db() # 데이터베이스 연결
app = QApplication(sys.argv)
widget_manager.widget = QtWidgets.QStackedWidget()  # 스택 위젯 생성
widget = widget_manager.widget  # 위젯 매니저에서 위젯 가져오기

MainWindow = MainWindow()   # 메인 윈도우 호출
LoginWindow = LoginWindow(widget)  # 로그인 윈도우 호출
AdminMenu = AdminMenu(widget)  # 관리자 메뉴 호출



widget.addWidget(MainWindow)  # 메인 윈도우 추가
widget.addWidget(LoginWindow)  # 로그인 윈도우 추가
widget.addWidget(AdminMenu)  # 관리자 메뉴 추가
widget.setFixedSize(800, 600)  # 고정 크기 설정
widget.setWindowTitle("DH First Project RC")
widget.show()   # 메인 윈도우를 보여줌

# 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
app.exec_()

# 프로그램 종료
connection.close()
sys.exit()