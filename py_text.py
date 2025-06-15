import sqlite3

DB_PATH = "py_game.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS python(
                code TEXT PRIMARY KEY,      --코드
                level TEXT NOT NULL        --난이도
        );
    ''')


def insert_python_code(code, level):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO python (code, level) VALUES (?, ?)",
                (code, level)
            )
            conn.commit()

def delete_python_code(code):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM python WHERE code = ?",
            (code,)
        )
        conn.commit()

if __name__ == "__main__":
    create_tables()

    # insert_python_code("print('Hello World')\nname = 'Python'\nprint(name)", '초급')
    # insert_python_code("list = [1,2,3,4]\nlist = list + [0,7]\nlist.append(8)\nprint(list)", '초급')
    # insert_python_code("month = 2\ndate = 16\nprint('나의 생일은',str(month)+'월',str(date)+'일 입니다.')",'초급')
    # insert_python_code("club = 'App and me'\nclub = club.split(" ")\nprint(club[0])", '초급')
    # insert_python_code("str = 'mirim'\nprint(str.upper())", '초급')

    # insert_python_code("number = 4\nif number%2==0:\n\tprint('짝수입니다.')\nelse:\n\tprint('홀수입니다.')", '중급')
    # insert_python_code("count = 0\nfor i in range(1,100+1):\n\tfor j in str(i):\n\t\tif j in \"369\":\n\t\t\tcount+=1\nprint(count)", '중급')
    # insert_python_code("score = (int)(input('점수를 입력하세요 : '))\nif score>=90:\n\tprint('A')\nelif score>=80 and score<90:\n\tprint('B')\nelif score>=70 and score<80:\n\tprint('C')\nelse:\n\tprint('D')",'중급')
    # insert_python_code("def factorial(n):\n\tif n<=1:\n\t\treturn 1\n\treturn n * factorial(n-1)\nprint(factorial(5))", '중급')
    # insert_python_code("def login(id, pw):\n\tif( id == 'scott' and pw == 'tiger'):\n\t\treturn True\n\telse:\n\t\treturn False\nprint(login('admin','1234'))\nprint(login('scott', 'tiger'))", '중급')

    # delete_python_code("def factorial(n):\n\tif n<=1:\n\t\treturn 1\n\treturn n * factorial(n-1)\nprint(factorial(5))")


    # insert_python_code("import random\nnumber = random.randint(1, 10)\nguess = int(input('1부터 10 사이의 숫자를 맞혀보세요: '))\nif guess == number:\n\tprint('정답입니다!')\nelse:\n\tprint(f'틀렸습니다. 정답은 {number}입니다.')", '고급')
    # insert_python_code("numbers = [7, 2, 9, 4, 5]\nmax_num = numbers[0]\nfor n in numbers:\n\tif n > max_num:\n\t\tmax_num = n\nprint(f'최댓값: {max_num}')", '고급')
    # insert_python_code("n = int(input('숫자를 입력하세요: '))\nis_prime = True\nif n < 2:\n\tis_prime = False\nfor i in range(2, int(n**0.5) + 1):\n\tif n % i == 0:\n\t\tis_prime = False\n\t\tbreak\nprint('소수입니다.' if is_prime else '소수가 아닙니다.')", '고급')