class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id  
        self.name = name              
        self.price = price            
        self.stock = stock    

    def get_basic_info(self):
        return f"Product ID: {self.product_id}, Name: {self.name}"
    
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"