class Sale():
    def __init__(self, time):
        self.time = time

    def __grandTotal__(self, quantity, price) -> float:
        grandTotal = float(quantity*price)
        return grandTotal

    def __add_item__(self, quantity: int, description: str, price: float, itemid: str) -> None:
        return

#Quantity
class SalesLineItem():
    def __init__(self, quantity):
        self.quantity = quantity

#Price
class ProductDescription():
    def __init__(self, description, price, itemId):
        self.description = description
        self.price = price
        self.itemId = itemId
