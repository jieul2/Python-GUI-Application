import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QButtonGroup
from PyQt5.QtCore import QTimer
from PyQt5.QtSql import QSqlQuery
from widgets.gui_setup import load_ui
from screens.admin_screen import AdminScreen
from widgets.widget_manager import widget
from models.db_connect import connect_to_db

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


form_class, base_class = load_ui("Rc/ui/signup.ui")

class SignupScreen(base_class, form_class):
    def __init__(self, widget): 
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        # objects 생성 모듈
        self.setWindowTitle("RC Signup")
        self.db = connect_to_db()
        if not self.db or not self.db.isOpen():
            QMessageBox.critical(self, "DB 오류", "데이터베이스가 열려 있지 않습니다.")
            return

        # QSqlQuery에 연결된 DB를 지정
        query = QSqlQuery(self.db)

        self.genderGroup = QButtonGroup(self)
        self.genderGroup.addButton(self.maleButton)
        self.genderGroup.addButton(self.femaleButton)


        self.menuButton.clicked.connect(self.show_menu_page)
        self.signupButton.clicked.connect(self.submitPushed)

        self.emailCombo.currentIndexChanged.connect(self.on_combobox_changed)


        # 코드에서 Validator 설정
        reg_exp = QRegExp(r"^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]*$")  # 텍스트라인 입력통제
        validator = QRegExpValidator(reg_exp)

        # Qt Designer에서 만든 QLineEdit에 적용
        self.idText.setValidator(validator)
        self.pwText.setValidator(validator)
        self.confirmPwText.setValidator(validator)
        self.emailFirstText.setValidator(validator)
        self.emailSecondText.setValidator(validator)



    def on_combobox_changed(self, index):
        if index == 0:  # 직접입력
            self.emailSecondText.setText("")
            self.emailSecondText.setReadOnly(False)
        elif index == 1:
            self.emailSecondText.setText("naver.com")
            self.emailSecondText.setReadOnly(True)
        elif index == 2:
            self.emailSecondText.setText("kakao.com")
            self.emailSecondText.setReadOnly(True)
        elif index == 3:
            self.emailSecondText.setText("google.com")
            self.emailSecondText.setReadOnly(True)
        elif index == 4:
            self.emailSecondText.setText("nate.com")
            self.emailSecondText.setReadOnly(True)


    def submitPushed(self):
        fields = {
            "아이디": self.idText.text(),
            "비밀번호": self.pwText.text(),
            "비밀번호 확인": self.confirmPwText.text(),
            "이름(성)": self.firstNameText.text(),
            "이름(이름)": self.secondNameText.text(),
            "이메일(앞)": self.emailFirstText.text(),
            "이메일(뒤)": self.emailSecondText.text(),
            "성별": self.genderGroup.checkedButton().text() if self.genderGroup.checkedButton() else "",
        }

        for label, value in fields.items():
            if not value:
                QMessageBox.information(self, "오류", f"'{label}' 항목이 비어 있습니다.", QMessageBox.Ok)
                return

        if fields["비밀번호"] != fields["비밀번호 확인"]:
            QMessageBox.warning(self, "오류", "비밀번호와 비밀번호 확인이 일치하지 않습니다.", QMessageBox.Ok)
            return

        # 이메일 합치기
        email = f"{fields['이메일(앞)']}@{fields['이메일(뒤)']}"
        gender_value = 1 if fields["성별"] == "남자" else 2

        # DB 삽입
        query = QSqlQuery(self.db)
        query.prepare("""
            INSERT INTO user (user_id, password, name, email_1, email_2, sex)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(fields["아이디"])
        query.addBindValue(fields["비밀번호"])
        query.addBindValue(fields["이름(성)"] + fields["이름(이름)"])
        query.addBindValue(fields["이메일(앞)"])
        query.addBindValue(fields["이메일(뒤)"])
        query.addBindValue(gender_value)

        if query.exec():
            QMessageBox.information(self, "회원가입", "회원 정보가 성공적으로 저장되었습니다!", QMessageBox.Ok)
            self.show_menu_page()
        else:
            QMessageBox.critical(self, "DB 오류", f"회원 정보 저장 실패: {query.lastError().text()}", QMessageBox.Ok)


    def show_menu_page(self):
        # Logic to display the login page
        self.widget.setCurrentWidget(self.widget.main_window)







