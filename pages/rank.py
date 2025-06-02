import customtkinter as ctk

# 테마 설정
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # yellow → blue 로 변경

class TacoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TACO 실시간 랭킹")
        self.geometry("900x600")
        self.configure(bg="#FFE082")  # 노란 배경

        self.create_ui()

    def create_ui(self):
        # 상단 바
        top_frame = ctk.CTkFrame(self, height=60, fg_color="white", corner_radius=0)
        top_frame.pack(fill="x", side="top")

        logo_label = ctk.CTkLabel(top_frame, text="🐙 TACO", font=("Arial", 20, "bold"), text_color="black")
        logo_label.pack(side="left", padx=20)

        # 중앙 영역
        center_frame = ctk.CTkFrame(self, fg_color="#FFE082")
        center_frame.pack(pady=20)

        dropdown = ctk.CTkOptionMenu(center_frame, values=["JAVA", "PYTHON", "HTML"])
        dropdown.set("JAVA")
        dropdown.pack()

        label = ctk.CTkLabel(center_frame, text="실시간 랭킹", font=("Arial", 18, "bold"), text_color="black")
        label.pack(pady=10)

        # 랭킹 박스 예시 하나
        for i in range(5):
            box = ctk.CTkFrame(self, width=300, height=60, corner_radius=10)
            box.pack(pady=5)
            ctk.CTkLabel(box, text=f"{i+1}위 ● 평균타수 1,032", font=("Arial", 14)).pack(padx=10, pady=10)

if __name__ == "__main__":
    app = TacoApp()
    app.mainloop()