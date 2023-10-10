class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

item = Item(10, 20)
print("Price:", item.price)  
print("Weight:", item.weight)
