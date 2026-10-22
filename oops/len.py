class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def add_item(self, item):
        self.items.append(item)

cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

print(len(cart))