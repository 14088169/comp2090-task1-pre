class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # 商品ID
        self.name = name              # 商品名称
        self.price = price            # 商品价格
    
    def get_basic_info(self):
        return f"商品ID：{self.product_id}，名称：{self.name}"
