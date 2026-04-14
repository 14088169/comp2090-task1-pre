"""Manage inventory data and persist it to a JSON file."""

from product import Product
import json
import os

class Inventory:
    LOW_STOCK_THRESHOLD = 10

    def __init__(self, filename="warehouse_data.json"):
        # Use a path relative to this module so JSON loads correctly
        # even when the app is started from a different working directory.
        base_dir = os.path.dirname(__file__)
        self.filename = os.path.join(base_dir, filename)
        self.products = {}
        self.load_data()

    def add_product(self, product):
        # Add a new product to inventory, ensuring the ID is unique
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            raise ValueError(f"Product with ID {product.product_id} already exists.")

    def update_stock(self, product_id, amount, role):
        # Update stock level with role-based permissions
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")

        amount = int(amount)
        if role == "staff":
            # Staff can only buy items, not restock inventory
            if amount > 0:
                raise ValueError("Staff cannot add stock")
            if self.products[product_id].stock + amount < 0:
                raise ValueError("Insufficient inventory")
            self.products[product_id].stock += amount
        elif role == "manager":
            if self.products[product_id].stock + amount < 0:
                raise ValueError("Insufficient inventory")
            self.products[product_id].stock += amount
        
        # Remove product if stock is zero or negative
        if self.products[product_id].stock <= 0:
            del self.products[product_id]
        
        self.save_data()

    def load_data(self):
        # Load inventory from JSON file, if the file exists
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for product_data in data:
                    product = Product(**product_data)
                    self.products[product.product_id] = product
        except FileNotFoundError:
            self.products = {}

    def save_data(self):
        # Persist inventory state to the JSON data file
        try:
            data = []
            for product in self.products.values():
                data.append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": product.price,
                    "stock": product.stock
                })
            with open(self.filename, "w", encoding="utf-8") as f:
                # Use ensure_ascii=False and indent=4 to properly handle non-ASCII characters in product names and improve readability of the JSON file
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Save failed: {e}")

    def check_low_stock(self):
        # Return a list of products that are below the low stock threshold
        low_stock_products = [product for product in self.products.values() if product.stock < self.LOW_STOCK_THRESHOLD]
        return low_stock_products

    def search_product(self, keyword):
        # Search for products by name or ID, ignoring case and whitespace
        keyword = keyword.strip().lower()
        matches = []
        for product in self.products.values():
            if keyword in product.name.lower() or keyword == product.product_id:
                matches.append(product)
        if not matches:
            raise ValueError("Product not found")
        return matches

    def sort_products(self, key):
        # Sort products by specified key (name, price, or stock)
        if key == "name":
            return sorted(self.products.values(), key=lambda x: x.name)
        elif key == "price":
            return sorted(self.products.values(), key=lambda x: x.price)
        elif key == "stock":
            return sorted(self.products.values(), key=lambda x: x.stock)
        else:
            return list(self.products.values())
