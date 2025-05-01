import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from widgets.gui_setup import load_ui
from widgets.widget_manager import widget as shared_widget
import widgets.widget_manager

from screens.admin_screen import AdminScreen
from screens.login_screen import LoginScreen

form_class, base_class = load_ui("Rc/ui/main.ui")

class MainWindow(base_class, form_class):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)

        self.widget = widget

        print(hasattr(self, 'loginAction'))  # True면 존재, False면 UI에 없음

        print(hasattr(self, 'mainAction'))  # True면 존재, False면 UI에 없음    





    
        self.mainAction.triggered.connect(self.show_main_page)
        self.loginAction.triggered.connect(self.show_login_page)
    




    def show_main_page(self):
        self.widget.setCurrentIndex(self.widget.indexOf(self))
    def show_login_page(self):
        # Logic to display the login page
        self.widget.setCurrentWidget(self.widget.login_screen)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    widgets.widget_manager.widget = QtWidgets.QStackedWidget()
    widget = widgets.widget_manager.widget
    MainWindow = MainWindow(widget)
    LoginScreen = LoginScreen(widget)
    AdminScreen = AdminScreen(widget)

    widget.main_window = MainWindow
    widget.login_screen = LoginScreen
    widget.admin_screen = AdminScreen


    widget.addWidget(MainWindow)
    widget.addWidget(LoginScreen)
    widget.addWidget(AdminScreen)

    widget.setFixedSize(800, 600)
    widget.setWindowTitle("RC")
    widget.show()
    
    app.exec_()