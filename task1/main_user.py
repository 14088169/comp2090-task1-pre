import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from product import Product

inventory = Inventory()
root = tk.Tk()
root.title("用户购买界面")
root.geometry("650x450")

list_frame = ttk.Frame(root, padding=10)
list_frame.pack(fill=tk.BOTH, expand=True)

list_box = tk.Listbox(
    list_frame,
    font=("微软雅黑", 11),
    selectmode=tk.SINGLE
)
scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=list_box.yview)
list_box.config(yscrollcommand=scroll.set)
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

def refresh_list():
    list_box.delete(0, tk.END)
    for p in inventory.products.values():
        list_box.insert(tk.END, f"ID:{p.product_id} | {p.name} | 单价:{p.price} | 库存:{p.stock}")

def buy():
    idx = list_box.curselection()
    if not idx:
        messagebox.showwarning("提示", "请选择一个商品")
        return

    text = list_box.get(idx[0])
    pid = text.split("|")[0].replace("ID:", "").strip()
    p = inventory.products[pid]

    buy_count = 1

    if p.stock < buy_count:
        messagebox.showerror("错误", "库存不足，无法购买")
        return

    p.stock -= buy_count

    if p.stock <= 0:
        del inventory.products[pid]

    inventory.save_data()
    refresh_list()
    messagebox.showinfo("购买成功", f"购买：{p.name}\n单价：{p.price}")

btn_frame = ttk.Frame(root, padding=10)
btn_frame.pack(fill=tk.X)

ttk.Button(btn_frame, text="刷新列表", command=refresh_list).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="购买", command=buy).pack(side=tk.LEFT, padx=5)

refresh_list()
root.mainloop()