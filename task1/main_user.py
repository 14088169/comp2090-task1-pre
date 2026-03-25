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
    selectmode=tk.MULTIPLE
)
scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=list_box.yview)
list_box.config(yscrollcommand=scroll.set)
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

def refresh_list():
    list_box.delete(0, tk.END)
    for p in inventory.products.values():
        list_box.insert(tk.END, str(p))

def buy():
    indices = list_box.curselection()
    if not indices:
        messagebox.showwarning("提示", "请选择商品")
        return

    bought = []
    total_price = 0

    for i in reversed(indices):
        text = list_box.get(i)
        pid = text.split("|")[0].replace("ID:", "").strip()
        p = inventory.products[pid]

        bought.append(f"{p.name}  单价：{p.price}")
        total_price += p.price
        del inventory.products[pid]

    inventory.save_data()
    refresh_list()

    messagebox.showinfo(
        "购买成功",
        "你已购买：\n• " + "\n• ".join(bought) + f"\n\n合计总价：{total_price}"
    )

btn_frame = ttk.Frame(root, padding=10)
btn_frame.pack(fill=tk.X)

ttk.Button(btn_frame, text="刷新列表", command=refresh_list).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="确认购买", command=buy).pack(side=tk.LEFT, padx=5)

refresh_list()
root.mainloop()