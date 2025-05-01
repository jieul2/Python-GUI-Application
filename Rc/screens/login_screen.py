import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from widgets.gui_setup import load_ui
from screens.admin_screen import AdminScreen
from widgets.widget_manager import widget


form_class, base_class = load_ui("Rc/ui/login.ui")

class LoginScreen(base_class, form_class):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        # objects 생성 모듈
        self.setWindowTitle("RC Login")

        self.loginButton.clicked.connect(self.loginButtonClicked)
        self.idText.returnPressed.connect(self.loginButtonClicked)
        self.pwText.returnPressed.connect(self.loginButtonClicked)

    def loginButtonClicked(self):
    # 로그인 버튼 클릭 시 동작하는 함수
        print(f"Login button clicked   Id = {self.idText.text()} Password = {self.pwText.text()}")
        if self.idText.text() == "admin" or self.pwText.text() == "1234":
            QMessageBox.information(self, "Login", "Login Success")
            self.widget.setCurrentWidget(self.widget.admin_screen)
            
        QMessageBox.information(self, "Login", f"Id = {self.idText.text()} \n Password = {self.pwText.text()}")