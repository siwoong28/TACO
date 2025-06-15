import sqlite3

DB_PATH = "html.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS html(
                code TEXT PRIMARY KEY,      --코드
                level TEXT NOT NULL        --난이도
        );
    ''')


def insert_html_code(code, level):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO html (code, level) VALUES (?, ?)",
            (code, level)
        )
        conn.commit()


def delete_html_code(code):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM html WHERE code = ?",
            (code,)
        )
        conn.commit()

if __name__ == "__main__":
    create_tables()

    # insert_html_code("<!DOCTYPE html>\n<html>\n<head>\n\t<title>Hello World</title>\n</head>\n<body>\n\t<h1>Hello World</h1>\n\t<p>Welcome to HTML!</p>\n</body>\n</html>","초급")
    # insert_html_code("<!DOCTYPE html>\n<html>\n<head>\n\t<title>Hello World</title>\n</head>\n<body>\n\t<p>MY name is Siwoong</p>\n\t<span>Im Mirim Meister high school student</span>\n</body>\n</html>","초급")
    # insert_html_code("<!DOCTYPE html>\n<html>\n<head>\n\t<title>Hello World</title>\n</head>\n<body>\n\t<p>Let's go! Lotte Giants!</p>\n\t<div>Let's go! Busan!</div>\n</body>\n</html>","초급")

    insert_html_code("<!DOCTYPE html>\n<html>\n<head>\n\t<title>Hello World</title>\n\t<style>\n\t\tbody{font-family: Arial, sans-serif;}\n\t\t.container { max-width: 800px; margin: 0 auto; }\n\t\t.header { background-color: #f0f0f0; padding: 20px; }\n\t</style>\n</head>\n<body>\n\t<div class=\"container\">\n\t\t<div class=\"header\">\n\t\t\t<h1>My Website</h1>\n\t\t\t<nav>\n\t\t\t\t<a href=\"#home\">Home</a>\n\t\t\t\t<a href=\"#about\">About</a>\n\t\t\t</nav>\n\t\t</div>\n\t</div>\n</body>\n</html>","고급")
    insert_html_code("<!DOCTYPE html>\n<html>\n<head>\n\t<title>Hello World</title>\n\t<style>\n\t\tp{background-color:red;}\n\t</style>\n</head>\n<body>\n\t<p>Let's go! Lotte Giants!</p>\n\t<div>Let's go! Busan!</div>\n</body>\n</html>","중급")
