import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5 import *
from widgets.gui_setup import load_ui
from widgets.widget_manager import widget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


form_class, base_class = load_ui("Rc/ui/update.ui")


class UpdateScreen(base_class, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("RC Admin")

        self.toggle = False

        self.connect_to_db()
        self.setup_model()
        self.model.select()
        self.upButton.clicked.connect(self.updateButtonClicked)

        



    def updateButtonClicked(self):
        self.toggle = not self.toggle
        self.toggleLabel.setText(str(self.toggle))
        if self.toggle:
            self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        else:
            self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

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
