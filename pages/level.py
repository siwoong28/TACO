import customtkinter as ctk
import tkinter as tk
import subprocess
import sys
import os


class DifficultySelector:
    def __init__(self):
        # 기본 테마 설정
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # 메인 윈도우 생성
        self.root = ctk.CTk()
        self.root.title("난이도 선택")
        self.root.geometry("1000x700")
        self.root.configure(fg_color="#FBE6A2")  # 지정된 배경색

        # 창을 화면 중앙에 위치시키기
        self.center_window()

        # 난이도별 코드 설정
        self.difficulty_codes = {
            "초급": [
                "print('Hello World')",
                "name = 'Python'",
                "print(name)"
            ],
            "중급": [
                "public class Main{",
                "    public static void main(String[] args){",
                "        int a = 1; int b = 2; int c = 3;",
                "        System.out.println(a + b + c);",
                "    }",
                "}"
            ],
            "고급": [
                "import java.util.*;",
                "public class Calculator {",
                "    private double result;",
                "    public Calculator() { this.result = 0.0; }",
                "    public double add(double a, double b) {",
                "        return this.result = a + b;",
                "    }",
                "    public static void main(String[] args) {",
                "        Calculator calc = new Calculator();",
                "        System.out.println(calc.add(10.5, 20.3));",
                "    }",
                "}"
            ]
        }

        self.setup_ui()

    def center_window(self):
        """창을 화면 중앙에 위치시키는 함수"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_ui(self):
        # 메인 컨테이너
        main_frame = ctk.CTkFrame(self.root, fg_color="#FBE6A2")
        main_frame.pack(fill="both", expand=True, padx=50, pady=50)

        # 제목
        title_label = ctk.CTkLabel(
            main_frame,
            text="난이도 선택",
            font=("Arial", 48, "bold"),
            text_color="black",
            fg_color="transparent"
        )
        title_label.pack(pady=(50, 80))

        # 버튼 컨테이너
        button_container = ctk.CTkFrame(main_frame, fg_color="#FBE6A2")
        button_container.pack(expand=True, fill="both")

        # 버튼들을 담을 프레임 (가로 배치)
        buttons_frame = ctk.CTkFrame(button_container, fg_color="#FBE6A2")
        buttons_frame.pack(expand=True)

        # 난이도 버튼들
        difficulty_levels = ["초급", "중급", "고급"]

        for i, level in enumerate(difficulty_levels):
            # 각 버튼을 위한 컨테이너
            button_frame = ctk.CTkFrame(buttons_frame, fg_color="#FBE6A2")
            button_frame.pack(side="left", padx=40, pady=50)

            # 난이도 버튼
            difficulty_btn = ctk.CTkButton(
                button_frame,
                text=level,
                width=200,
                height=250,
                font=("Arial", 28, "bold"),
                fg_color="white",
                text_color="black",
                hover_color="#F0F0F0",
                corner_radius=20,
                border_width=2,
                border_color="#E0E0E0",
                command=lambda l=level: self.select_difficulty(l)
            )
            difficulty_btn.pack()

            # 버튼에 마우스 호버 효과 추가
            self.add_hover_effect(difficulty_btn)

    def add_hover_effect(self, button):
        """버튼에 호버 효과를 추가하는 함수"""

        def on_enter(event):
            button.configure(
                fg_color="#F5F5F5",
                border_color="#D0D0D0"
            )

        def on_leave(event):
            button.configure(
                fg_color="white",
                border_color="#E0E0E0"
            )

        # 마우스 이벤트 바인딩
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def select_difficulty(self, level):
        """난이도 선택 시 play.py를 실행하는 함수"""
        print(f"선택된 난이도: {level}")

        # 선택된 난이도의 코드 가져오기
        selected_code = self.difficulty_codes.get(level, [])

        try:
            # play.py 실행 (난이도와 코드를 인자로 전달)
            self.run_play_game(level, selected_code)
        except Exception as e:
            print(f"게임 실행 중 오류 발생: {e}")
            self.show_error_message(str(e))

    def run_play_game(self, difficulty, code_lines):
        """play.py를 실행하는 함수"""
        try:
            # level.py 기준 디렉토리
            base_dir = os.path.dirname(os.path.abspath(__file__))

            # play.py 절대 경로 찾기
            possible_paths = [
                os.path.join(base_dir, "play.py"),
                os.path.join(base_dir, "pages", "play.py")
            ]

            play_file_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    play_file_path = path
                    break

            if not play_file_path:
                raise FileNotFoundError("play.py 파일을 찾을 수 없습니다.")

            # 현재 level 창 닫기
            self.root.destroy()

            # 환경변수로 정보 전달
            env = os.environ.copy()
            env['GAME_DIFFICULTY'] = difficulty
            env['GAME_CODE'] = '|'.join(code_lines)

            # play.py 실행
            subprocess.Popen([sys.executable, play_file_path], env=env)

        except Exception as e:
            raise e

    def show_error_message(self, error_msg):
        """에러 메시지를 표시하는 함수"""
        # 새로운 창 생성
        error_window = ctk.CTkToplevel(self.root)
        error_window.title("오류")
        error_window.geometry("500x250")
        error_window.configure(fg_color="white")
        error_window.resizable(False, False)

        # 창을 화면 중앙에 위치시키기
        error_window.transient(self.root)
        error_window.grab_set()

        # 메시지 컨테이너
        message_container = ctk.CTkFrame(error_window, fg_color="white")
        message_container.pack(fill="both", expand=True, padx=30, pady=30)

        # 오류 메시지 표시
        error_label = ctk.CTkLabel(
            message_container,
            text="게임 실행 중 오류가 발생했습니다:",
            font=("Arial", 16, "bold"),
            text_color="red"
        )
        error_label.pack(pady=(10, 5))

        # 상세 오류 내용
        detail_label = ctk.CTkLabel(
            message_container,
            text=error_msg,
            font=("Arial", 12),
            text_color="black",
            wraplength=400
        )
        detail_label.pack(pady=(5, 20))

        # 확인 버튼
        ok_button = ctk.CTkButton(
            message_container,
            text="확인",
            width=100,
            height=40,
            font=("Arial", 16, "bold"),
            fg_color="#FF6B6B",
            text_color="white",
            hover_color="#FF5252",
            corner_radius=10,
            command=error_window.destroy
        )
        ok_button.pack(pady=10)

    def run(self):
        """애플리케이션 실행"""
        self.root.mainloop()


if __name__ == "__main__":
    app = DifficultySelector()
    app.run()