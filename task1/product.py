"""Product data model used by the inventory system."""

class Product:
    """Represents a single product in inventory."""

    def __init__(self, product_id, name, price, stock):
        # Validate product data to ensure integrity of inventory
        if not product_id or any(c.isspace() for c in product_id):
            raise ValueError("Product ID cannot be empty or contain whitespace")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if stock < 0:
            raise ValueError("Stock cannot be negative")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        # Better format for displaying product information in the list box
        return f"ID:{self.product_id} | Name:{self.name} | Price:{self.price} | Stock:{self.stock}"

    def get_info(self):
        # Return product information as a dictionary for JSON serialization
        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }