import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from widgets.gui_setup import load_ui
from screens.admin_screen import AdminScreen
from widgets.widget_manager import widget
from PyQt5.QtSql import QSqlQuery
from models.db_connect import connect_to_db

form_class, base_class = load_ui("Rc/ui/login.ui")

class LoginScreen(base_class, form_class):
    def __init__(self, widget): 
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        self.db = connect_to_db()

        # objects 생성 모듈
        self.setWindowTitle("RC Login")
        

        self.loginButton.clicked.connect(self.loginButtonClicked)
        self.devButton.clicked.connect(self.devButtonClicked)
        #self.adminCheck.stateChanged.connect(self.loginButtonClicked)
        self.idText.returnPressed.connect(self.loginButtonClicked)
        self.pwText.returnPressed.connect(self.loginButtonClicked)

    def devButtonClicked(self):
        self.idText.setText("admin")
        self.pwText.setText("1234")
        self.adminCheck.setCheckState(2)


    def try_login(self, input_id, input_pw):
        query = QSqlQuery()
        query.prepare("SELECT * FROM user WHERE user_id = :id AND password = :pw")
        query.bindValue(":id", input_id)
        query.bindValue(":pw", input_pw)

        print(query.exec())
        print(query.next())

        if query.exec() and query.next():
            print("로그인 성공")
            return True
        else:
            print("로그인 실패")
            return False

    def loginButtonClicked(self):
    # 로그인 버튼 클릭 시 동작하는 함수


        input_id = self.idText.text()
        input_pw = self.pwText.text()
        user_id = ""
        print(f"Login button clicked   Id = {input_id} Password = {input_pw}")
        if self.try_login(input_id, input_pw):

            query = QSqlQuery()
            query.prepare("SELECT name FROM user WHERE user_id = :user_id")
            query.bindValue(":user_id", input_id)
            if query.exec() and query.next():
                user_name = query.value(0)
                QMessageBox.information(self, "로그인", f"로그인 성공! 사용자 : {user_name}")
            else:
                QMessageBox.warning(self, "오류", "사용자 이름을 가져올 수 없습니다.")
        elif self.idText.text() == "admin" and self.pwText.text() == "1234" and self.adminCheck.isChecked() == True:
            if QMessageBox.question(self, "Admin", "Admin으로 로그인 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes):
                self.widget.setCurrentWidget(self.widget.admin_screen)
                QMessageBox.information(self, "Login", "Login Success")
        elif self.idText.text() != "admin" and self.pwText.text() != "1234" and self.adminCheck.isChecked() == True:
            QMessageBox.warning(self, "오류", "어드민 계정이 아닙니다.")