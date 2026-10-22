class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

product1 = Product("Laptop", 50000)
product2 = Product("Laptop", 50000)
product3 = Product("Mouse", 1000)