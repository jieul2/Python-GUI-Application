import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from widgets.gui_setup import load_ui
from widgets.widget_manager import widget
import widgets.widget_manager

from screens.admin_screen import AdminScreen
from screens.login_screen import LoginScreen
from screens.signup_screen import SignupScreen

form_class, base_class = load_ui("Rc/ui/main.ui")

class MainWindow(base_class, form_class):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)

        self.widget = widget

        
    
        self.mainAction.triggered.connect(self.show_main_page)
        self.loginAction.triggered.connect(self.show_login_page)
        self.loginButton.clicked.connect(self.show_login_page)
        self.regButton.clicked.connect(self.show_signup_page)
    


    def show_main_page(self):
        self.widget.setCurrentIndex(self.widget.indexOf(self))
    def show_login_page(self):
        # Logic to display the login page
        self.widget.setCurrentWidget(self.widget.login_screen)
    def show_signup_page(self):
        self.widget.setCurrentWidget(self.widget.signup_screen)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    widgets.widget_manager.widget = QtWidgets.QStackedWidget()
    widget = widgets.widget_manager.widget

    # 클래스들을 (이름, 클래스) 튜플로 나열
    screens = [
        ("main_window", MainWindow),
        ("login_screen", LoginScreen),
        ("admin_screen", AdminScreen),
        ("signup_screen", SignupScreen)
    ]

    # 반복문으로 인스턴스 생성, 속성 저장, 위젯에 추가
    for name, ScreenClass in screens:
        screen_instance = ScreenClass(widget)
        setattr(widget, name, screen_instance)
        widget.addWidget(screen_instance)

    widget.setFixedSize(800, 600)
    widget.setWindowTitle("RC")
    widget.show()
    
    app.exec_()