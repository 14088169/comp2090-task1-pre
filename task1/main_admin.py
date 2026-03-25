import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from product import Product

inventory = Inventory()
root = tk.Tk()
root.title("管理员界面")
root.geometry("700x500")

top_frame = ttk.Frame(root, padding=15)
top_frame.pack(fill=tk.X)

ttk.Label(top_frame, text="商品ID：").grid(row=0, column=0, padx=5, pady=3)
pid_entry = ttk.Entry(top_frame)
pid_entry.grid(row=0, column=1, padx=5, pady=3)

ttk.Label(top_frame, text="名称：").grid(row=0, column=2, padx=5, pady=3)
name_entry = ttk.Entry(top_frame)
name_entry.grid(row=0, column=3, padx=5, pady=3)

ttk.Label(top_frame, text="价格：").grid(row=1, column=0, padx=5, pady=3)
price_entry = ttk.Entry(top_frame)
price_entry.grid(row=1, column=1, padx=5, pady=3)

ttk.Label(top_frame, text="库存：").grid(row=1, column=2, padx=5, pady=3)
stock_entry = ttk.Entry(top_frame)
stock_entry.grid(row=1, column=3, padx=5, pady=3)

list_frame = ttk.Frame(root, padding=10)
list_frame.pack(fill=tk.BOTH, expand=True)

list_box = tk.Listbox(list_frame, font=("微软雅黑", 11))
scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=list_box.yview)
list_box.config(yscrollcommand=scroll.set)
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

def refresh_list():
    list_box.delete(0, tk.END)
    for p in inventory.products.values():
        list_box.insert(tk.END, str(p))

def add_product():
    pid = pid_entry.get().strip()
    name = name_entry.get().strip()
    price = price_entry.get().strip()
    stock = stock_entry.get().strip()
    if not (pid and name and price and stock):
        messagebox.showwarning("提示", "请填写完整")
        return
    try:
        price = float(price)
        stock = int(stock)
    except:
        messagebox.showerror("错误", "价格/库存必须是数字")
        return
    p = Product(pid, name, price, stock)
    inventory.add_product(p)
    inventory.save_data()
    refresh_list()

def delete_product():
    pid = pid_entry.get().strip()
    if pid in inventory.products:
        del inventory.products[pid]
        inventory.save_data()
        refresh_list()

def search_product():
    keyword = pid_entry.get().strip()
    if not keyword:
        return
    try:
        p = inventory.search_product(keyword)
        list_box.delete(0, tk.END)
        list_box.insert(tk.END, str(p))
    except:
        messagebox.showinfo("结果", "未找到商品")

btn_frame = ttk.Frame(root, padding=10)
btn_frame.pack(fill=tk.X)
ttk.Button(btn_frame, text="刷新", command=refresh_list).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="搜索", command=search_product).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="添加", command=add_product).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="删除", command=delete_product).pack(side=tk.LEFT, padx=5)

refresh_list()
root.mainloop()