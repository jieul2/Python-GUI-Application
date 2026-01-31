import os

def connect_to_db():
    from PyQt5.QtSql import QSqlDatabase

    connection_name = "rc_connection"

    if QSqlDatabase.contains(connection_name):
        return QSqlDatabase.database(connection_name)

    db = QSqlDatabase.addDatabase("QSQLITE", connection_name)

    # 절대경로로 지정
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../db/Rc.db"))
    print(f"📂 DB 경로: {db_path}")
    db.setDatabaseName(db_path)

    if not db.open():
        print("❌ 데이터베이스 연결 실패:", db.lastError().text())
    else:
        print("✅ 데이터베이스 연결 성공")

    return db
