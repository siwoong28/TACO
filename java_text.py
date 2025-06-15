import sqlite3

DB_PATH = "java_game.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS java(
                code TEXT PRIMARY KEY,      --코드
                level TEXT NOT NULL        --난이도
        );
    ''')

def insert_java_code(code, level):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO java (code, level) VALUES (?, ?)",
            (code, level)
        )
        conn.commit()


def delete_java_code(code):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM java WHERE code = ?",
            (code,)
        )
        conn.commit()


if __name__ == "__main__":
    create_tables()

    # insert_java_code("public class HelloWorld {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println(\"Hello World\");\n\t}\n}", '초급')
    # insert_java_code("public class ab {\n\tpublic static void main(String[] args) {\n\t\tint a = 1;\n\t\tint b = 5;\n\t\tSystem.out.println(a + b);\n\t}\n}", '초급')
    # insert_java_code("public class ab {\n\tpublic static void main(String[] args) {\n\t\tint a = 4;\n\t\tint b = 7;\n\t\tSystem.out.println(a + b);\n\t\tSystem.out.println(a - b);\n\t\tSystem.out.println(a * b);\n\t\tSystem.out.println(a / b);\n\t}\n}", '초급')

    # insert_java_code("public class gugudan {\n\tpublic static void main(String[] args) {\n\t\tint dan = 5;\n\t\tSystem.out.println("== " + dan + '단 ==');\n\t\tfor (int i = 1; i <= 9; i++)\n\t\t\tSystem.out.println(dan + \" x \" + i + \" = \" + (dan * i));\n\t}\n\t}\n}",'중급')
    # insert_java_code("public class Max {\n\tpublic static void main(String[] args) {\n\t\tint[] nums = {3, 7, 2, 9, 5};\n\t\tint max = nums[0];\n\t\tfor (int i = 0; i<nums.length; i++){\n\t\t\tif (i > max) max = n;\n\t\t}\n\t\tSystem.out.println(\"최댓값: \" + max);\n\t}\n}",'중급')
    # insert_java_code("import java.util.Scanner;\npublic class EvenOddCheck {\n\tpublic static void main(String[] args) {\n\t\tScanner sc = new Scanner(System.in);\n\t\tif (n % 2 == 0) {\n\t\t\tSystem.out.println(\"짝수입니다.\");\n\t\t} else {\n\t\t\tSystem.out.println(\"홀수입니다.\");\n\t\t}\n\t}\n}",'고급')

    # insert_java_code("public class Sum {\n\tpublic static void main(String[] args) {\n\t\tint sum = 0;\n\t\tfor (int i = 1; i <= 10; i++) {\n\t\t\tsum += i;\n\t\t}\n\t\tSystem.out.println(\"1부터 10까지의 합: \" + sum);\n\t}\n}",'중급')
    # insert_java_code("public class str_length {\n\tpublic static void main(String[] args) {\n\t\tString text = \"Hello, Java!\";\n\t\tint length = text.length();\n\t\tSystem.out.println(\"문자열 길이: \" + length);\n\t}\n}",'고급')
    # insert_java_code("import java.util.Scanner;\npublic class Factorial{\n\tpublic static void main(String[] args) {\n\t\tScanner sc = new Scanner(System.in);\n\t\tSystem.out.print(\"정수를 입력하세요: \");\n\t\tint n = sc.nextInt();\n\t\tlong result = 1;\n\t\tfor (int i = 1; i <= n; i++) {\n\t\t\tresult *= i;\n\t\t}\n\t\tSystem.out.println(n + \"! = \" + result);\n\t}\n}",'고급')