# db.py
import sqlite3

DB_PATH = "typing_game.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,                  -- 아이디
                name TEXT NOT NULL,                   -- 이름
                password TEXT NOT NULL,               -- 비밀번호

                total_time INTEGER DEFAULT 0,         -- 전체 연습 시간 (초 단위)
                avg_speed REAL DEFAULT 0,             -- 평균 타수 (타자 속도)
                avg_accuracy REAL DEFAULT 0,          -- 평균 정확도 (%)

                recent_code TEXT DEFAULT '',          -- 최근 작성한 코드 (문자열)
                frequent_mistake TEXT DEFAULT ''      -- 자주 틀리는 글자
            );
        ''')
        conn.commit()