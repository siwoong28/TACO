import customtkinter as ctk
import tkinter as tk
import subprocess
import sys
import os
import sqlite3
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(PROJECT_ROOT, "java_game.db")

# 전역 창 선언
window = ctk.CTk()
window.title("JAVA 난이도 선택")
window.geometry("1920x1080")
window.configure(fg_color="#FBE6A2")  # 배경색

def center_window():
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

center_window()

def fetch_random_code(level):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT code FROM java WHERE level = ?", (level,))
        rows = cursor.fetchall()

        if not rows:
            return None

        code_str = random.choice(rows)[0]  # 하나 랜덤 선택
        return code_str.splitlines()

def show_error_message(error_msg):
    error_window = ctk.CTkToplevel(window)
    error_window.title("오류")
    error_window.geometry("500x250")
    error_window.configure(fg_color="white")
    error_window.resizable(False, False)

    error_window.transient(window)
    error_window.grab_set()

    message_container = ctk.CTkFrame(error_window, fg_color="white")
    message_container.pack(fill="both", expand=True, padx=30, pady=30)

    error_label = ctk.CTkLabel(
        message_container,
        text="게임 실행 중 오류가 발생했습니다:",
        font=("Arial", 16, "bold"),
        text_color="red"
    )
    error_label.pack(pady=(10, 5))

    detail_label = ctk.CTkLabel(
        message_container,
        text=error_msg,
        font=("Arial", 12),
        text_color="black",
        wraplength=400
    )
    detail_label.pack(pady=(5, 20))

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

def run_play_game(difficulty, code_lines):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
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

        window.destroy()

        env = os.environ.copy()
        env['GAME_DIFFICULTY'] = difficulty
        env['GAME_CODE'] = '|'.join(code_lines)
        env['GAME_LANGUAGE'] = 'JAVA'

        subprocess.Popen([sys.executable, play_file_path], env=env)

    except Exception as e:
        show_error_message(str(e))

def on_difficulty_selected(level):
    print(f"선택된 JAVA 난이도: {level}")
    code_lines = fetch_random_code(level)
    if code_lines is None:
        show_error_message(f"'{level}' 난이도의 코드가 DB에 없습니다!")
        return
    run_play_game(level, code_lines)

def add_hover_effect(button):
    def on_enter(event):
        button.configure(fg_color="#F5F5F5", border_color="#D0D0D0")

    def on_leave(event):
        button.configure(fg_color="white", border_color="#E0E0E0")

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# UI 구성
main_frame = ctk.CTkFrame(window, fg_color="#FBE6A2")
main_frame.pack(fill="both", expand=True, padx=50, pady=50)

title_label = ctk.CTkLabel(
    main_frame,
    text="JAVA 난이도 선택",
    font=("Arial", 48, "bold"),
    text_color="black",
    fg_color="transparent"
)
title_label.pack(pady=(50, 80))

button_container = ctk.CTkFrame(main_frame, fg_color="#FBE6A2")
button_container.pack(expand=True, fill="both")

buttons_frame = ctk.CTkFrame(button_container, fg_color="#FBE6A2")
buttons_frame.pack(expand=True)

for level in ["초급", "중급", "고급"]:
    button_frame = ctk.CTkFrame(buttons_frame, fg_color="#FBE6A2")
    button_frame.pack(side="left", padx=40, pady=50)

    btn = ctk.CTkButton(
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
        command=lambda l=level: on_difficulty_selected(l)
    )
    btn.pack()

    add_hover_effect(btn)

# 앱 실행
window.mainloop()