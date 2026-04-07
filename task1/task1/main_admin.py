import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from product import Product

inventory = Inventory()


class AdminPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Return button takes the user back to the home page
        def go_home():
            for frame_class in self.controller.frames:
                if frame_class.__name__ == "HomePage":
                    controller.show_frame(frame_class)
                    return
        
        return_btn_frame = ttk.Frame(self)
        return_btn_frame.pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(return_btn_frame, text="← Back to Home", command=go_home).pack(side=tk.LEFT)
        
        # Top input panel for product details
        top_frame = ttk.Frame(self, padding=15)
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="Product ID:").grid(row=0, column=0, padx=5, pady=3)
        self.pid_entry = ttk.Entry(top_frame)
        self.pid_entry.grid(row=0, column=1, padx=5, pady=3)

        ttk.Label(top_frame, text="Name:").grid(row=0, column=2, padx=5, pady=3)
        self.name_entry = ttk.Entry(top_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=3)

        ttk.Label(top_frame, text="Price:").grid(row=1, column=0, padx=5, pady=3)
        self.price_entry = ttk.Entry(top_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=3)

        ttk.Label(top_frame, text="Stock:").grid(row=1, column=2, padx=5, pady=3)
        self.stock_entry = ttk.Entry(top_frame)
        self.stock_entry.grid(row=1, column=3, padx=5, pady=3)

        # Product list display area
        list_frame = ttk.Frame(self, padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.list_box = tk.Listbox(list_frame, font=("Arial", 11))
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll.set)
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Action buttons for admin operations
        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X)
        ttk.Button(btn_frame, text="Search", command=self.search_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Add", command=self.add_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_product).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_inputs).pack(side=tk.LEFT, padx=5)

    def refresh_list(self):
        # Refresh the product list display with current inventory data
        self.list_box.delete(0, tk.END)
        for p in inventory.products.values():
            self.list_box.insert(tk.END, str(p))

    def add_product(self):
        # Add a new product or update an existing one based on the entered product ID and details
        pid = self.pid_entry.get().strip()
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        
        # Validate input data
        if not (pid and name and price and stock):
            messagebox.showwarning("Warning", "Please complete all fields")
            return

        if any(c.isspace() for c in pid):
            messagebox.showwarning("Warning", "Product ID cannot contain whitespace")
            return
        
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Error", "Price/stock must be numeric")
            return

        if price <= 0 or stock < 0:
            messagebox.showerror("Error", "Price must be greater than 0 and stock cannot be negative")
            return
        
        # Check if the product ID already exists and update it if confirmed
        if pid in inventory.products:
            result = messagebox.askyesno("Product Exists", f"Product ID {pid} already exists. Update it?")
            if result:
                inventory.products[pid].name = name
                inventory.products[pid].price = price
                inventory.products[pid].stock = stock
                inventory.save_data()
                self.refresh_list()
                messagebox.showinfo("Success", "Product updated successfully")
            else:
                messagebox.showinfo("Notice", "Operation canceled")
        else:
            p = Product(pid, name, price, stock)
            inventory.products[pid] = p
            inventory.save_data()
            self.refresh_list()
            messagebox.showinfo("Success", "Product added successfully")

    def clear_inputs(self):
        # Clear all admin entry fields to prevent accidental reuse
        self.pid_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)

    def delete_product(self):
        # Delete a product from inventory based on the entered product ID, with confirmation
        pid = self.pid_entry.get().strip()
        if not pid:
            messagebox.showwarning("Warning", "Please enter a product ID")
            return

        if any(c.isspace() for c in pid):
            messagebox.showwarning("Warning", "Product ID cannot contain whitespace")
            return
        
        # Check if the product ID exists and delete it if confirmed
        if pid in inventory.products:
            result = messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete product ID {pid}?")
            if result:
                del inventory.products[pid]
                inventory.save_data()
                self.refresh_list()
                self.pid_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Product deleted successfully")
            else:
                messagebox.showinfo("Notice", "Delete canceled")
        else:
            messagebox.showwarning("Error", f"Product ID {pid} does not exist")

    def search_product(self):
        # Search for products by ID or name based on the entered keywords and display results in the list box
        id_keyword = self.pid_entry.get().strip()
        name_keyword = self.name_entry.get().strip()

        if not id_keyword and not name_keyword:
            messagebox.showwarning("Warning", "Please enter a product ID or name to search")
            return

        try:
            if id_keyword:
                # Exact match by ID
                if id_keyword in inventory.products:
                    self.list_box.delete(0, tk.END)
                    self.list_box.insert(tk.END, str(inventory.products[id_keyword]))
                    messagebox.showinfo("Search Result", "Found 1 matching product (ID)")
                    return
                else:
                    raise ValueError("Product not found")

            # Search by name (partial match)
            products = inventory.search_product(name_keyword)
            self.list_box.delete(0, tk.END)
            for p in products:
                self.list_box.insert(tk.END, str(p))
            messagebox.showinfo("Search Result", f"Found {len(products)} matching products (name)")
        except ValueError:
            if id_keyword:
                messagebox.showwarning("Search Result", f"ID not found: {id_keyword}")
            else:
                messagebox.showwarning("Search Result", f"Name not found: {name_keyword}")
