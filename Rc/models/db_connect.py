import sqlite3
import os

# DB 파일 경로 설정 (절대 경로로 작성하는 것이 안전)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db', 'Rc.db')

def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None
