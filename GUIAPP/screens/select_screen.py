import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5 import *
from widgets.gui_setup import load_ui
from widgets.widget_manager import widget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from models.db_connect import connect_to_db


form_class, base_class = load_ui("Rc/ui/select.ui")


class SelectScreen(base_class, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("RC Admin")
        self.db = connect_to_db()

        
        self.setup_model()
        self.model.select()


    def connect_to_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(os.path.join(os.path.dirname(__file__), '../db/Rc.db'))
        if not self.db.open():
            print("Failed to open database")
        else:
            print("Database connected.")

    def setup_model(self):
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('user')
        self.tableView.setModel(self.model)
