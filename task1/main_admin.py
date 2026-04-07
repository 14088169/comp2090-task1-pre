import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from product import Product

inventory = Inventory()


class AdminPage(ttk.Frame):
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
        ttk.Button(return_btn_frame, text="← 返回主页", command=go_home).pack(side=tk.LEFT)
        
        # 顶部输入框
        top_frame = ttk.Frame(self, padding=15)
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="商品ID：").grid(row=0, column=0, padx=5, pady=3)
        self.pid_entry = ttk.Entry(top_frame)
        self.pid_entry.grid(row=0, column=1, padx=5, pady=3)

        ttk.Label(top_frame, text="名称：").grid(row=0, column=2, padx=5, pady=3)
        self.name_entry = ttk.Entry(top_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=3)

        ttk.Label(top_frame, text="价格：").grid(row=1, column=0, padx=5, pady=3)
        self.price_entry = ttk.Entry(top_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=3)

        ttk.Label(top_frame, text="库存：").grid(row=1, column=2, padx=5, pady=3)
        self.stock_entry = ttk.Entry(top_frame)
        self.stock_entry.grid(row=1, column=3, padx=5, pady=3)

        # 列表框
        list_frame = ttk.Frame(self, padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.list_box = tk.Listbox(list_frame, font=("微软雅黑", 11))
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll.set)
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # 按钮
        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X)
        ttk.Button(btn_frame, text="刷新", command=self.refresh_list).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="搜索", command=self.search_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="添加", command=self.add_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="删除", command=self.delete_product).pack(side=tk.LEFT, padx=5)

    def refresh_list(self):
        self.list_box.delete(0, tk.END)
        for p in inventory.products.values():
            self.list_box.insert(tk.END, str(p))

    def add_product(self):
        pid = self.pid_entry.get().strip()
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        
        if not (pid and name and price and stock):
            messagebox.showwarning("提示", "请填写完整")
            return
        
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("错误", "价格/库存必须是数字")
            return
        
        # 检查ID是否已存在
        if pid in inventory.products:
            # 询问用户是否更新
            result = messagebox.askyesno("商品已存在", f"商品ID {pid} 已存在。是否更新？")
            if result:
                # 更新现有商品
                inventory.products[pid].name = name
                inventory.products[pid].price = price
                inventory.products[pid].stock = stock
                inventory.save_data()
                self.refresh_list()
                messagebox.showinfo("成功", "商品更新成功")
            else:
                messagebox.showinfo("提示", "操作已取消")
        else:
            # 添加新商品
            p = Product(pid, name, price, stock)
            inventory.products[pid] = p
            inventory.save_data()
            self.refresh_list()
            messagebox.showinfo("成功", "商品添加成功")

    def delete_product(self):
        pid = self.pid_entry.get().strip()
        if not pid:
            messagebox.showwarning("提示", "请输入商品ID")
            return
        
        if pid in inventory.products:
            result = messagebox.askyesno("删除确认", f"确定要删除商品ID {pid} 吗？")
            if result:
                del inventory.products[pid]
                inventory.save_data()
                self.refresh_list()
                self.pid_entry.delete(0, tk.END)
                messagebox.showinfo("成功", "商品删除成功")
            else:
                messagebox.showinfo("提示", "删除已取消")
        else:
            messagebox.showwarning("错误", f"商品ID {pid} 不存在")

    def search_product(self):
        id_keyword = self.pid_entry.get().strip()
        name_keyword = self.name_entry.get().strip()

        if not id_keyword and not name_keyword:
            messagebox.showwarning("提示", "请输入商品ID或名称搜索")
            return

        try:
            if id_keyword:
                # 精确匹配ID
                if id_keyword in inventory.products:
                    self.list_box.delete(0, tk.END)
                    self.list_box.insert(tk.END, str(inventory.products[id_keyword]))
                    messagebox.showinfo("搜索结果", f"找到 1 个匹配商品（ID）")
                    return
                else:
                    raise ValueError("Product not found")

            # 名称搜索（模糊匹配）
            products = inventory.search_product(name_keyword)
            self.list_box.delete(0, tk.END)
            for p in products:
                self.list_box.insert(tk.END, str(p))
            messagebox.showinfo("搜索结果", f"找到 {len(products)} 个匹配商品（名称）")
        except ValueError:
            if id_keyword:
                messagebox.showwarning("搜索结果", f"未找到ID: {id_keyword}")
            else:
                messagebox.showwarning("搜索结果", f"未找到名称: {name_keyword}")


# 保持独立运行的兼容性
if __name__ == "__main__":
    root = tk.Tk()
    root.title("管理员界面")
    root.geometry("700x500")
    
    class DummyController:
        def show_frame(self, frame_class):
            pass
    
    app = AdminPage(root, DummyController())
    app.pack(fill=tk.BOTH, expand=True)
    app.refresh_list()
    root.mainloop()