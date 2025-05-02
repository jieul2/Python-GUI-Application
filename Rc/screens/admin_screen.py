import sys
import os
from PyQt5 import QtWidgets, uic
from widgets.gui_setup import load_ui
from widgets.widget_manager import widget

from screens.select_screen import SelectScreen


form_class, base_class = load_ui("Rc/ui/admin.ui")

class AdminScreen(base_class, form_class):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget



        self.selectButton.clicked.connect(self.selectButtonClicked)


        self.setWindowTitle("RC Admin")

    def selectButtonClicked(self):
        self.select_screen = SelectScreen()
        self.select_screen.show()