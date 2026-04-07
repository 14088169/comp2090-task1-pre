import tkinter as tk
from tkinter import ttk
from main_admin import AdminPage
from main_user import UserPage


class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        ttk.Label(self, text="请选择登录角色", font=("微软雅黑", 18)).pack(pady=50)
        ttk.Button(self, text="管理员", command=lambda: controller.show_frame(AdminPage), width=20).pack(pady=10)
        ttk.Button(self, text="用户", command=lambda: controller.show_frame(UserPage), width=20).pack(pady=10)
        ttk.Button(self, text="退出", command=controller.quit, width=20).pack(pady=10)


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("库存管理系统")
        self.geometry("700x400")
        
        container = ttk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (HomePage, AdminPage, UserPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(HomePage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if hasattr(frame, 'refresh_list'):
            frame.refresh_list()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
