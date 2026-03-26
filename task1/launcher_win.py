import tkinter as tk
from tkinter import ttk
import os

def open_admin():
    root.destroy()
    os.system("python main_admin.py")

def open_user():
    root.destroy()
    os.system("python main_user.py")

root = tk.Tk()
root.title("库存管理系统")
root.geometry("400x250")
root.resizable(False, False)

ttk.Label(root, text="请选择登录角色", font=("微软雅黑", 16)).pack(pady=40)
ttk.Button(root, text="管理员", command=open_admin, width=15).pack(pady=5)
ttk.Button(root, text="用户", command=open_user, width=15).pack(pady=5)

root.mainloop()
