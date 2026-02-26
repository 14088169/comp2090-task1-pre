from product import Product
from inventory import Inventory
from user import User

if __name__ == "__main__":
    apple = Product("abc", "苹果", 5.99)
    stock = Inventory()
    admin = User("U001", "管理员", "admin")

    print(apple.get_basic_info())
