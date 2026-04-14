import tkinter as tk
from tkinter import ttk, messagebox


class UserPage(ttk.Frame):
    def __init__(self, parent, controller, inventory):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.inventory = inventory
        
        # Return button to go back to the home page
        def go_home():
            for frame_class in self.controller.frames:
                if frame_class.__name__ == "HomePage":
                    controller.show_frame(frame_class)
                    return
        
        return_btn_frame = ttk.Frame(self)
        return_btn_frame.pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(return_btn_frame, text="Back to Home", command=go_home).pack(side=tk.LEFT)

        list_frame = ttk.Frame(self, padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.list_box = tk.Listbox(
            list_frame,
            font=("Arial", 14),
            selectmode=tk.SINGLE
        )
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll.set)
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X)

        # Search controls
        search_frame = ttk.Frame(self, padding=10)
        search_frame.pack(fill=tk.X)
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame, width=20)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_products).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Show All", command=self.refresh_list).pack(side=tk.LEFT, padx=5)

        # Sort controls
        sort_frame = ttk.Frame(self, padding=10)
        sort_frame.pack(fill=tk.X)
        ttk.Label(sort_frame, text="Sort by:").pack(side=tk.LEFT, padx=5)
        self.sort_var = tk.StringVar(value="name")
        sort_combo = ttk.Combobox(sort_frame, textvariable=self.sort_var, values=["name", "price", "stock"], state="readonly", width=10)
        sort_combo.pack(side=tk.LEFT, padx=5)
        ttk.Button(sort_frame, text="Sort", command=self.sort_products).pack(side=tk.LEFT, padx=5)

        buy_frame = ttk.Frame(self, padding=10)
        buy_frame.pack(fill=tk.X)

        ttk.Label(buy_frame, text="Quantity:").pack(side=tk.LEFT, padx=5)
        self.quantity_entry = ttk.Entry(buy_frame, width=6)
        self.quantity_entry.pack(side=tk.LEFT, padx=5)
        self.quantity_entry.insert(0, "1")
        self.total_label = ttk.Label(buy_frame, text="Total: 0.00")
        self.total_label.pack(side=tk.LEFT, padx=10)

        ttk.Button(buy_frame, text="Buy", command=self.buy).pack(side=tk.LEFT, padx=5)

    def refresh_list(self):
        self.list_box.delete(0, tk.END)
        for p in self.inventory.products.values():
            self.list_box.insert(tk.END, f"ID:{p.product_id} | {p.name} | Price:{p.price} | Stock:{p.stock}")

    def buy(self):
        idx = self.list_box.curselection()
        if not idx:
            messagebox.showwarning("Warning", "Please select a product")
            return

        quantity_text = self.quantity_entry.get().strip()
        if not quantity_text:
            messagebox.showwarning("Warning", "Please enter purchase quantity")
            return

        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a positive integer")
            return

        text = self.list_box.get(idx[0])
        pid = text.split("|")[0].replace("ID:", "").strip()

        total = self.inventory.products[pid].price * quantity
        self.total_label.config(text=f"Total: {total:.2f}")

        confirmed = messagebox.askyesno(
            "Confirm Purchase",
            f"Product: {self.inventory.products[pid].name}\nUnit price: {self.inventory.products[pid].price:.2f}\nQuantity: {quantity}\nTotal: {total:.2f}\n\nConfirm purchase?"
        )
        if not confirmed:
            return

        try:
            self.inventory.update_stock(pid, -quantity, "staff")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.refresh_list()
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, "1")
        self.total_label.config(text="Total: 0.00")
        selected_product = self.inventory.products[pid]
        messagebox.showinfo("Purchase Successful", f"Purchased: {selected_product.name}\nQuantity: {quantity}\nTotal: {total:.2f}")

    def search_products(self):
        # Search for products by name or ID and display results
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Warning", "Please enter a search keyword")
            return

        try:
            matches = self.inventory.search_product(keyword)
            self.list_box.delete(0, tk.END)
            for p in matches:
                self.list_box.insert(tk.END, f"ID:{p.product_id} | {p.name} | Price:{p.price} | Stock:{p.stock}")
            messagebox.showinfo("Search Result", f"Found {len(matches)} matching products")
        except ValueError:
            messagebox.showwarning("Search Result", f"No products found for: {keyword}")

    def sort_products(self):
        # Sort products by the selected key and refresh the list
        key = self.sort_var.get()
        sorted_products = self.inventory.sort_products(key)
        self.list_box.delete(0, tk.END)
        for p in sorted_products:
            self.list_box.insert(tk.END, f"ID:{p.product_id} | {p.name} | Price:{p.price} | Stock:{p.stock}")
        messagebox.showinfo("Sort", f"Products sorted by {key}")

