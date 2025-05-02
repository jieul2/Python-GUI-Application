import sys
import os
from PyQt5 import QtWidgets, uic
from widgets.gui_setup import load_ui
from widgets.widget_manager import widget


from models import db_connect

conn = db_connect.get_connection()

form_class, base_class = load_ui("Rc/ui/select.ui")


class SelectScreen(base_class, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("RC Admin")

        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        conn.close()