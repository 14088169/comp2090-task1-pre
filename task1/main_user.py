import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from product import Product

inventory = Inventory()


class UserPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        # 返回按钮
        def go_home():
            for frame_class in self.controller.frames:
                if frame_class.__name__ == "HomePage":
                    controller.show_frame(frame_class)
                    return
        
        return_btn_frame = ttk.Frame(self)
        return_btn_frame.pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(return_btn_frame, text="返回主页", command=go_home).pack(side=tk.LEFT)

        list_frame = ttk.Frame(self, padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.list_box = tk.Listbox(
            list_frame,
            font=("微软雅黑", 11),
            selectmode=tk.SINGLE
        )
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll.set)
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X)

        ttk.Button(btn_frame, text="刷新列表", command=self.refresh_list).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="购买", command=self.buy).pack(side=tk.LEFT, padx=5)

    def refresh_list(self):
        self.list_box.delete(0, tk.END)
        for p in inventory.products.values():
            self.list_box.insert(tk.END, f"ID:{p.product_id} | {p.name} | 单价:{p.price} | 库存:{p.stock}")

    def buy(self):
        idx = self.list_box.curselection()
        if not idx:
            messagebox.showwarning("提示", "请选择一个商品")
            return

        text = self.list_box.get(idx[0])
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
        self.refresh_list()
        messagebox.showinfo("购买成功", f"购买：{p.name}\n单价：{p.price}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("用户购买界面")
    root.geometry("650x450")
    
    class DummyController:
        def show_frame(self, frame_class):
            pass
    
    app = UserPage(root, DummyController())
    app.pack(fill=tk.BOTH, expand=True)
    app.refresh_list()
    root.mainloop()