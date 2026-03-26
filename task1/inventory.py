from product import Product
import json

class Inventory:
    LOW_STOCK_THRESHOLD = 10

    def __init__(self, filename="warehouse_data.json"):
        self.filename = filename
        self.products = {}
        self.load_data()

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            raise ValueError(f"Product with ID {product.product_id} already exists.")

    def update_stock(self, product_id, amount, role):
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")

        amount = int(amount)
        if role == "staff":
            if amount > 0:
                raise ValueError("Staff cannot add stock")
            if self.products[product_id].stock + amount < 0:
                raise ValueError("Insufficient inventory")
            self.products[product_id].stock += amount
        elif role == "manager":
            if self.products[product_id].stock + amount < 0:
                raise ValueError("Insufficient inventory")
            self.products[product_id].stock += amount
        self.save_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for product_data in data:
                    product = Product(**product_data)
                    self.products[product.product_id] = product
        except FileNotFoundError:
            self.products = {}

    def save_data(self):
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
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"保存失败: {e}")

    def check_low_stock(self):
        low_stock_products = [product for product in self.products.values() if product.stock < self.LOW_STOCK_THRESHOLD]
        return low_stock_products

    def search_product(self, keyword):
        keyword = keyword.strip().lower()
        matches = []
        for product in self.products.values():
            if keyword in product.name.lower() or keyword == product.product_id:
                matches.append(product)
        if not matches:
            raise ValueError("Product not found")
        return matches

    def sort_products(self, key):
        if key == "name":
            return sorted(self.products.values(), key=lambda x: x.name)
        elif key == "price":
            return sorted(self.products.values(), key=lambda x: x.price)
        elif key == "stock":
            return sorted(self.products.values(), key=lambda x: x.stock)
        else:
            return list(self.products.values())
