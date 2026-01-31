from PyQt5 import uic

def load_ui(ui_file):
    form_class, base_class = uic.loadUiType(ui_file)
    return form_class, base_class