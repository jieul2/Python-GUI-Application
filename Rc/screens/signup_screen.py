import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
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