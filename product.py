class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  
        self.name = name              
        self.price = price            
    
    def get_basic_info(self):
        return f"商品ID：{self.product_id}，名称：{self.name}"
