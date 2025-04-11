from product import Product

class Store:
    def __init__(self, products=None):
        self.products = products or []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Only instances of Product can be added.")
        self.products.append(product)
        print(f"{product.name} has been added to the store.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} has been removed from the store.")
        else:
            print(f"{product.name} is not in the store.")

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product.is_active() and product.quantity >= quantity:
                product.quantity -= quantity
                total_price += product.buy(quantity)
                print(f"Added {quantity} of {product.name} to the order.")
            else:
                print(f"{product.name} is not available in the requested quantity.")
        return total_price


    def show_items(self):
        print("Inventory")
        for product in self.products:
            print(f"{product}")


store = Store(
    [Product("MacBook Air M2", price=1450, quantity=100),
     Product("Bose QuietComfort Earbuds", price=250, quantity=500),
     Product("Google Pixel 7", price=500, quantity=250),
    ]
)
