import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
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
        self.devButton.clicked.connect(self.devButtonClicked)
        #self.adminCheck.stateChanged.connect(self.loginButtonClicked)
        self.idText.returnPressed.connect(self.loginButtonClicked)
        self.pwText.returnPressed.connect(self.loginButtonClicked)

    def devButtonClicked(self):
        self.idText.setText("admin")
        self.pwText.setText("1234")
        self.adminCheck.setCheckState(2)

    def loginButtonClicked(self):
    # 로그인 버튼 클릭 시 동작하는 함수
        print(f"Login button clicked   Id = {self.idText.text()} Password = {self.pwText.text()}")
        if self.idText.text() == "admin" and self.pwText.text() == "1234" and self.adminCheck.isChecked() == True:
            if QMessageBox.question(self, "Admin", "Admin으로 로그인 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes):
                self.widget.setCurrentWidget(self.widget.admin_screen)
                QMessageBox.information(self, "Login", "Login Success")
                
        else:
            QMessageBox.information(self, "Login", f"Id = {self.idText.text()} \n Password = {self.pwText.text()}")