class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID:{self.product_id} | 名称:{self.name} | 价格:{self.price} | 库存:{self.stock}"

    def get_info(self):
        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }