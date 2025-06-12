import customtkinter as ctk
from PIL import Image, ImageTk
import os
import subprocess
import sys

# 창 기본 설정
window = ctk.CTk()
window.title("랭킹 페이지")
window.geometry("1920x1080")
window.configure(fg_color="#FBE6A2")  # 배경 노랑

# 현재 선택된 메뉴
selected_menu = ctk.StringVar(value="JAVA")

def switch_page(menu_name):
    selected_menu.set(menu_name)
    update_menu_styles()
    print(f"🔁 '{menu_name}' 페이지로 전환")

    # level.py 절대 경로로 찾기
    script_path = os.path.join(os.path.dirname(__file__), "level.py")
    script_path = os.path.abspath(script_path)
    script_dir = os.path.dirname(script_path)

    # subprocess 실행 시 작업 디렉토리 설정
    subprocess.Popen(
        [sys.executable, script_path, menu_name],
        cwd=script_dir
    )

    window.withdraw()

def update_menu_styles():
    for btn, name in menu_buttons:
        if selected_menu.get() == name:
            btn.configure(text_color="#2962FF", font=("Arial", 16, "bold"))
        else:
            btn.configure(text_color="black", font=("Arial", 16))

# 상단 바
top_frame = ctk.CTkFrame(window, height=80, fg_color="white", corner_radius=0)
top_frame.pack(fill="x", side="top")

# 왼쪽: 로고 프레임
logo_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
logo_frame.pack(side="left", padx=30, pady=20)

# logo.png 이미지 로딩
logo_path = os.path.join(os.path.dirname(__file__), "..","assets", "logo.png")
logo_path = os.path.abspath(logo_path)
logo_image = ctk.CTkImage(Image.open(logo_path), size=(60, 60))

logo_label = ctk.CTkLabel(logo_frame, image=logo_image, text="")
logo_label.pack(side="left", padx=5)

# 로고 텍스트
logo_text = ctk.CTkLabel(logo_frame, text="TACO", font=("Arial", 22, "bold"), text_color="black")
logo_text.pack(side="left")

# 밑줄 강조
underline = ctk.CTkFrame(logo_frame, width=50, height=6, fg_color="#FFF59D", corner_radius=3)
underline.place(relx=0.5, rely=1, anchor="s", x=12, y=8)

# 가운데 메뉴 버튼
menu_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
menu_frame.pack(side="left", padx=80)

menus = ["JAVA", "PYTHON", "HTML"]
menu_buttons = []

for menu in menus:
    btn = ctk.CTkButton(
        menu_frame,
        text=menu,
        command=lambda m=menu: switch_page(m),
        fg_color="transparent",
        hover_color="#f1f1f1",
        text_color="black",
        font=("Arial", 16),
        width=60,
        height=30,
    )
    btn.pack(side="left", padx=20)
    menu_buttons.append((btn, menu))

update_menu_styles()

# 오른쪽 아이콘
user_icon = ctk.CTkLabel(top_frame, text="◡̈", font=("Arial", 26), text_color="black")
user_icon.pack(side="right", padx=30)

# 랭킹 제목 + 드롭다운
title_frame = ctk.CTkFrame(window, fg_color="#FBE6A2")
title_frame.pack(pady=30)

dropdown = ctk.CTkOptionMenu(
    title_frame,
    values=menus,
    fg_color="#ffffff",
    text_color="black",
    button_color="#ffffff",
    button_hover_color="#f1f1f1",
    width=120
)
dropdown.set("JAVA")
dropdown.pack(side="left", padx=10)

title_label = ctk.CTkLabel(title_frame, text="실시간 랭킹", font=("Arial", 20, "bold"), text_color="black")
title_label.pack(side="left", padx=10)

# 실행
window.mainloop()