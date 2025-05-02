import os
from PyQt5.QtSql import QSqlDatabase

def connect_to_db():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(os.path.join(os.path.dirname(__file__), '../db/Rc.db'))

    if not db.open():
        print("❌ 데이터베이스 연결 실패")
    else:
        print("✅ 데이터베이스 연결 성공")

    return db
