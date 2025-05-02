import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QButtonGroup
from PyQt5.QtCore import QTimer
from widgets.gui_setup import load_ui
from screens.admin_screen import AdminScreen
from widgets.widget_manager import widget


form_class, base_class = load_ui("Rc/ui/signup.ui")

class SignupScreen(base_class, form_class):
    def __init__(self, widget): 
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        # objects 생성 모듈
        self.setWindowTitle("RC Signup")

        self.genderGroup = QButtonGroup(self)
        self.genderGroup.addButton(self.maleButton)
        self.genderGroup.addButton(self.femaleButton)


        self.menuButton.clicked.connect(self.show_menu_page)
        self.signupButton.clicked.connect(self.submitPushed)


    def submitPushed(self):

        id = self.idText.text()
        pw = self.pwText.text()
        confirmpw = self.confirmPwText.text()
        firstName = self.firstNameText.text()
        secondName = self.secondNameText.text()
        firstEmail = self.emailFirstText.text()
        secondEmail = self.emailSecondText.text()
        checked_button = self.genderGroup.checkedButton()
        if checked_button:
            gender = checked_button.text()
        else: return
        
        print(id, pw, confirmpw, firstName, secondName, firstEmail, secondEmail, gender)

        QMessageBox.information(self, "DataBase 등록 !!!")



    def show_menu_page(self):
        # Logic to display the login page
        self.widget.setCurrentWidget(self.widget.main_window)