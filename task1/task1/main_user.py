import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from product import Product

inventory = Inventory()


class UserPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
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
            font=("Arial", 11),
            selectmode=tk.SINGLE
        )
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll.set)
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X)

        ttk.Label(btn_frame, text="Quantity:").pack(side=tk.LEFT, padx=5)
        self.quantity_entry = ttk.Entry(btn_frame, width=6)
        self.quantity_entry.pack(side=tk.LEFT, padx=5)
        self.quantity_entry.insert(0, "1")
        self.total_label = ttk.Label(btn_frame, text="Total: 0.00")
        self.total_label.pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Buy", command=self.buy).pack(side=tk.LEFT, padx=5)

    def refresh_list(self):
        self.list_box.delete(0, tk.END)
        for p in inventory.products.values():
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
        p = inventory.products[pid]

        if p.stock < quantity:
            messagebox.showerror("Error", "Insufficient stock, cannot purchase")
            return

        total = p.price * quantity
        self.total_label.config(text=f"Total: {total:.2f}")

        confirmed = messagebox.askyesno(
            "Confirm Purchase",
            f"Product: {p.name}\nUnit price: {p.price:.2f}\nQuantity: {quantity}\nTotal: {total:.2f}\n\nConfirm purchase?"
        )
        if not confirmed:
            return

        p.stock -= quantity

        if p.stock <= 0:
            del inventory.products[pid]

        inventory.save_data()
        self.refresh_list()
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, "1")
        self.total_label.config(text="Total: 0.00")
        messagebox.showinfo("Purchase Successful", f"Purchased: {p.name}\nQuantity: {quantity}\nTotal: {total:.2f}")

