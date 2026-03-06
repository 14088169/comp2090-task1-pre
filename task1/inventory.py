from product import Product
import json


class Inventory:
    LOW_STOCK_THRESHOLD = 10

    def __init__(self, filename="warehouse_data.json"):
        # Initialize the inventory with a filename for data storage
        self.filename = filename
        self.products = {}
        self.load_data()

    def add_product(self, product):
        # Add a new product to the inventory
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            print(f"Product with ID {product.id} already exists.")
    
    def update_stock(self, product_id,amount,role):
        # Update the stock of a product based on the role of the user
        if product_id in self.products:
            self.products[product_id].stock += amount
        else:
            print(f"Product with ID {product_id} not found.")
        
        amount = int(amount)
        if role == "staff":
            if amount > 0:
                raise ValueError("Staff cannot add stock")
            if amount+self.products[product_id].stock < 0:
                raise ValueError("Insufficient inventory")
            self.products[product_id].stock -= amount
        if role == "manager":
            if amount+self.products[product_id].stock < 0:
                raise ValueError("Insufficient inventory")
            self.products[product_id].stock += amount
        
        self.save_data()


    def load_data(self):
        # Load data from JSON file
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for product_data in data:
                    product = Product(**product_data)
                    self.products[product.product_id] = product
        except FileNotFoundError:
            self.products = {}

                
    def check_low_stock(self):
        # Return a list of products that are low in stock
        low_stock_products = [product for product in self.products.values() if product.stock < self.LOW_STOCK_THRESHOLD]
        return low_stock_products
    

    def search_product(self, keyword):
        # Search by name or product ID
        for product in self.products.values():
            if keyword.lower() in product.name.lower() or keyword == product.product_id:
                return product
        else:
            raise ValueError("Product not found")

    def sort_products(self, key):
        if key == "name":
            return sorted(self.products.values(), key=lambda x: x.name)
        elif key == "price":
            return sorted(self.products.values(), key=lambda x: x.price)
        elif key == "stock":
            return sorted(self.products.values(), key=lambda x: x.stock)
        else:
            return list(self.products.values())