import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import os
import subprocess
import sys


class MyPageGUI:
    def __init__(self):
        # 테마 설정
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # 메인 윈도우
        self.root = ctk.CTk()
        self.root.title("마이 페이지")
        self.root.geometry("1920x1080")
        self.root.configure(fg_color="#F5E6A8")

        # 헤더 생성
        self.create_header()

        # 메인 컨테이너 생성
        self.create_main_content()

    def navigate_to_rank(self):
        """rank.py로 이동하는 함수"""
        try:
            # 현재 창 닫기
            self.root.destroy()
            # rank.py 실행
            rank_path = os.path.join(os.path.dirname(__file__), "rank.py")
            if os.path.exists(rank_path):
                subprocess.Popen([sys.executable, rank_path])
            else:
                print("rank.py 파일을 찾을 수 없습니다.")
        except Exception as e:
            print(f"rank.py 실행 중 오류 발생: {e}")

    def create_header(self):
        # 헤더 프레임
        header_frame = ctk.CTkFrame(self.root, fg_color="white", height=80, corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)

        # 왼쪽 - 로고와 마이 페이지 텍스트
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.pack(side="left", padx=30, pady=15)

        # 로고
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
            logo_path = os.path.abspath(logo_path)
            if os.path.exists(logo_path):
                logo_image = ctk.CTkImage(Image.open(logo_path), size=(60, 60))
                logo_button = ctk.CTkButton(
                    left_frame,
                    image=logo_image,
                    text="",
                    width=60,
                    height=60,
                    fg_color="transparent",
                    hover_color="#F0F0F0",
                    corner_radius=10,
                    command=self.navigate_to_rank
                )
                logo_button.pack(side="left", padx=(0, 15))
            else:
                # 로고 파일이 없을 경우 텍스트 버튼으로 대체
                logo_button = ctk.CTkButton(
                    left_frame,
                    text="LOGO",
                    width=60,
                    height=60,
                    fg_color="#4A90E2",
                    hover_color="#357ABD",
                    corner_radius=10,
                    font=("Arial", 12, "bold"),
                    command=self.navigate_to_rank
                )
                logo_button.pack(side="left", padx=(0, 15))
        except Exception as e:
            print(f"로고 로드 중 오류: {e}")
            # 오류 발생 시 텍스트 버튼으로 대체
            logo_button = ctk.CTkButton(
                left_frame,
                text="LOGO",
                width=60,
                height=60,
                fg_color="#4A90E2",
                hover_color="#357ABD",
                corner_radius=10,
                font=("Arial", 12, "bold"),
                command=self.navigate_to_rank
            )
            logo_button.pack(side="left", padx=(0, 15))

        title_label = ctk.CTkLabel(left_frame, text="마이 페이지", font=("Malgun Gothic", 24, "bold"), text_color="#333333")
        title_label.pack(side="left")

        # 유저 아이콘
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", padx=30, pady=15)

        user_icon = ctk.CTkFrame(right_frame, width=40, height=40, fg_color="white", border_width=2,
                                 border_color="#CCCCCC", corner_radius=20)
        user_icon.pack()
        user_icon.pack_propagate(False)

        user_label = ctk.CTkLabel(user_icon, text="👤", font=("Arial", 20))
        user_label.pack(expand=True)

    def create_main_content(self):
        # 메인 컨테이너
        main_container = ctk.CTkFrame(self.root, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=40, pady=40)

        # 콘텐츠 카드
        content_card = ctk.CTkFrame(main_container, fg_color="white", corner_radius=20)
        content_card.pack(fill="both", expand=True)

        main_frame = ctk.CTkFrame(content_card, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=40, pady=40)

        self.create_left_section(main_frame)

        self.create_right_section(main_frame)

    def create_left_section(self, parent):
        left_frame = ctk.CTkFrame(parent, fg_color="transparent", width=300)
        left_frame.pack(side="left", fill="y", padx=(0, 40))
        left_frame.pack_propagate(False)

        # 프로필 이미지
        profile_frame = ctk.CTkFrame(left_frame, width=120, height=120, fg_color="#DDDDDD", corner_radius=60)
        profile_frame.pack(pady=(0, 20))
        profile_frame.pack_propagate(False)

        profile_icon = ctk.CTkLabel(profile_frame, text="👤", font=("Arial", 60), text_color="#999999")
        profile_icon.pack(expand=True)

        # 사용자명
        name_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        name_frame.pack(pady=(0, 30))

        name_label = ctk.CTkLabel(name_frame, text="김미림 ✏️", font=("Malgun Gothic", 24, "bold"), text_color="#333333")
        name_label.pack()

        # 통계 섹션
        stats_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        stats_frame.pack(fill="x")

        # 통계 탭
        tab_frame = ctk.CTkFrame(stats_frame, fg_color="white", border_width=2, border_color="#333333", corner_radius=5)
        tab_frame.pack(anchor="w", pady=(0, 20))

        tab_label = ctk.CTkLabel(tab_frame, text="통계", font=("Malgun Gothic", 14, "bold"), text_color="#333333")
        tab_label.pack(padx=20, pady=10)

        # 통계 항목들
        self.create_stat_item(stats_frame, "전체 진행시간", "39:48")
        self.create_stat_item(stats_frame, "평균 타수(타/분)", "180")

        accuracy_frame = ctk.CTkFrame(stats_frame, fg_color="transparent")
        accuracy_frame.pack(fill="x", pady=15)

        accuracy_top = ctk.CTkFrame(accuracy_frame, fg_color="transparent")
        accuracy_top.pack(fill="x")

        accuracy_label = ctk.CTkLabel(accuracy_top, text="평균 정확도(%)", font=("Malgun Gothic", 16), text_color="#333333")
        accuracy_label.pack(side="left")

        accuracy_value = ctk.CTkLabel(accuracy_top, text="98.00", font=("Malgun Gothic", 16, "bold"),
                                      text_color="#333333")
        accuracy_value.pack(side="right")

        # 진행바
        progress_bar = ctk.CTkProgressBar(accuracy_frame, width=280, height=6, progress_color="#FF6B6B")
        progress_bar.pack(fill="x", pady=(5, 0))
        progress_bar.set(0.98)

        # 구분선
        separator = ctk.CTkFrame(accuracy_frame, height=1, fg_color="#EEEEEE")
        separator.pack(fill="x", pady=(15, 0))

    def create_stat_item(self, parent, label, value):
        item_frame = ctk.CTkFrame(parent, fg_color="transparent")
        item_frame.pack(fill="x", pady=15)

        label_widget = ctk.CTkLabel(item_frame, text=label, font=("Malgun Gothic", 16), text_color="#333333")
        label_widget.pack(side="left")

        value_widget = ctk.CTkLabel(item_frame, text=value, font=("Malgun Gothic", 16, "bold"), text_color="#333333")
        value_widget.pack(side="right")

        # 구분선
        separator = ctk.CTkFrame(item_frame, height=1, fg_color="#EEEEEE")
        separator.pack(fill="x", pady=(15, 0))

    def create_right_section(self, parent):
        right_frame = ctk.CTkFrame(parent, fg_color="transparent")
        right_frame.pack(side="left", fill="both", expand=True)

        # 키보드 섹션
        self.create_keyboard_section(right_frame)

    def create_code_item(self, parent, date, language, code_text, lang_bg_color, is_outlined=False):
        item_frame = ctk.CTkFrame(parent, fg_color="transparent")
        item_frame.pack(fill="x", pady=10)

        # 날짜
        date_label = ctk.CTkFrame(item_frame, fg_color="#E0E0E0", corner_radius=15)
        date_label.pack(side="left", padx=(0, 15))

        date_text = ctk.CTkLabel(date_label, text=date, font=("Arial", 12), text_color="#666666")
        date_text.pack(padx=10, pady=5)

        # 언어 태그
        if is_outlined:
            lang_label = ctk.CTkFrame(item_frame, fg_color="white", border_width=1, border_color="#333333",
                                      corner_radius=15)
            text_color = "#333333"
        else:
            lang_label = ctk.CTkFrame(item_frame, fg_color=lang_bg_color, corner_radius=15)
            text_color = "white"

        lang_label.pack(side="left", padx=(0, 15))

        lang_text = ctk.CTkLabel(lang_label, text=language, font=("Arial", 12, "bold"), text_color=text_color)
        lang_text.pack(padx=15, pady=5)

        # 코드 텍스트
        code_label = ctk.CTkLabel(item_frame, text=code_text, font=("Arial", 14), text_color="#333333")
        code_label.pack(side="left")

    def create_keyboard_section(self, parent):
        keyboard_frame = ctk.CTkFrame(parent, fg_color="#F9F9F9", border_width=2, border_color="#DDDDDD",
                                      corner_radius=15)
        keyboard_frame.pack(fill="both", expand=True, pady=(30, 0))

        keyboard_container = ctk.CTkFrame(keyboard_frame, fg_color="transparent")
        keyboard_container.pack(fill="both", expand=True, padx=20, pady=20)

        # 진행도 바
        progress_bar = ctk.CTkProgressBar(keyboard_container, width=900, height=20, progress_color="#FF6B6B")
        progress_bar.pack(pady=(0, 20))
        progress_bar.set(0.75)

        # 키보드 레이아웃
        keyboard_layout_frame = ctk.CTkFrame(keyboard_container, fg_color="transparent")
        keyboard_layout_frame.pack()

        # 키보드 행 정의
        keyboard_rows = [
            ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace"],
            ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
            ["Caps", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"],
            ["Shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Shift"],
            ["Ctrl", "Alt", "Space", "Alt", "Ctrl"]
        ]

        # 키 상태 정의 (색상)
        key_states = {
            "`": "#F0F0F0", "1": "#F4D03F", "2": "#F4D03F", "3": "#F4D03F", "4": "#F4D03F",
            "5": "#F4D03F", "6": "#F4D03F", "7": "#F4D03F", "8": "#F4D03F", "9": "#F4D03F",
            "0": "#F4D03F", "-": "#F0F0F0", "=": "#F0F0F0", "Backspace": "#F0F0F0",
            "Tab": "#F0F0F0", "Q": "#F4D03F", "W": "#F4D03F", "E": "#F4D03F", "R": "#F4D03F",
            "T": "#F4D03F", "Y": "#F4D03F", "U": "#F4D03F", "I": "#8B4513", "O": "#F4D03F",
            "P": "#F4D03F", "[": "#F4D03F", "]": "#F4D03F", "\\": "#F0F0F0",
            "Caps": "#F0F0F0", "A": "#F4D03F", "S": "#F4D03F", "D": "#E74C3C", "F": "#F4D03F",
            "G": "#F4D03F", "H": "#F4D03F", "J": "#F4D03F", "K": "#F4D03F", "L": "#F4D03F",
            ";": "#F4D03F", "'": "#F4D03F", "Enter": "#F0F0F0",
            "Shift": "#F0F0F0", "Z": "#F4D03F", "X": "#F4D03F", "C": "#F4D03F", "V": "#F4D03F",
            "B": "#F4D03F", "N": "#F39C12", "M": "#F4D03F", ",": "#F4D03F", ".": "#F4D03F",
            "/": "#F4D03F",
            "Ctrl": "#F0F0F0", "Alt": "#F0F0F0", "Space": "#F4D03F"
        }

        for row_idx, row in enumerate(keyboard_rows):
            row_frame = ctk.CTkFrame(keyboard_layout_frame, fg_color="transparent")
            row_frame.pack(pady=3)

            for key in row:
                # 키 크기 설정
                key_width = 70
                if key in ["Backspace"]:
                    key_width = 200
                elif key == "Enter":
                    key_width = 160
                elif key == "Space":
                    key_width = 500
                elif key in ["Tab", "Caps", "Shift"]:
                    key_width = 140

                # 키 색상 설정
                key_color = key_states.get(key, "#F0F0F0")

                if key_color in ["#8B4513", "#E74C3C", "#F39C12"]:
                    text_color = "white"
                else:
                    text_color = "#333333"

                key_btn = ctk.CTkButton(
                    row_frame,
                    text=key if key != "Space" else "Space",
                    width=key_width,
                    height=70,
                    fg_color=key_color,
                    text_color=text_color,
                    hover_color=key_color,
                    corner_radius=6,
                    font=("Arial", 12, "bold"),
                    border_width=1,
                    border_color="#CCCCCC"
                )
                key_btn.pack(side="left", padx=3)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MyPageGUI()
    app.run()