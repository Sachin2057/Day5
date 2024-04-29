class Product:
    def __init__(self, price):
        self.price = price


class DiscountedPrice(Product):
    def __init__(self, price, discount):
        super().__init__(price=price)
        self.discount = discount
        self.price = self.price-(self.price*self.discount/100)


def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price


products = [Product(100), DiscountedPrice(50, 10), Product(75)]
print("Total Price:", calculate_total_price(products))
