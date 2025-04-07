class Product:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError(f"Quantity {quantity} cannot be less than zero!")
        self.quantity = quantity

    def is_active(self):
        return self.quantity > 0

    def activate(self):
        if self.quantity <= 0:
            self.quantity = 1
        print(f"{self.name} has been activated.")

    def deactivate(self):
        self.quantity = 0
        print(f"{self.name} has been deactivated")

    def show(self):
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity):
        return self.price * quantity


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

store = Store(
        [Product("MacBook Air M2", price=1450, quantity=100),
         Product("Bose QuietComfort Earbuds", price=250, quantity=500),
         Product("Google Pixel 7", price=500, quantity=250),
        ])



def menu_header(header):
    return header


def menu_options(options_list):
    return options_list


def user_input(user_choice):
    return input(user_choice)


def list_of_items(store):
    products = store.get_all_products()
    if not products:
        print("No active products available in the store.")
    else:
        print("Available products:")
        for product in products:
            print(f"{product.name}, {product.price}, {product.quantity}")


def add_to_shopping_list(bb_store):
    shopping_list = []
    while True:
        products = bb_store.get_all_products()
        if not products:
            print("No active product available in the store.")
            break

        print("Available Products: ")
        for index, product in enumerate(products, 1):
            print(f"{index}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        print("Enter 0 to finish adding products to the shopping list")

        try:
            product_index = int(input("Enter number of the product you want to add to your shopping list: "))
            if product_index == 0:
                break
            elif 1 <= product_index <= len(products):
                selected_product = products[product_index - 1]
                quantity = int(input(f"Enter quantity of '{selected_product.name}' to add: "))
                if quantity <= 0:
                    print("Enter a positive number")
                    continue
                if quantity > selected_product.quantity:
                    print(f"Only {selected_product.quantity} available in the store. Select smaller amount.")
                    continue
                shopping_list.append((selected_product, quantity))
                print(f"Added {quantity} of '{selected_product.name}' to your shopping list.\n")
            else:
                print("Invalid number, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
    return shopping_list


def main():
    header_string = f"Store Menu\n{'-' * len('Store Menu')}"
    menu_list = (
        f"1. List all products in store\n"
        f"2. Show total amount in store\n"
        f"3. Make an order\n"
        f"4. Quit"
    )
    user_string = "Please choose a number: "
    while True:
        header_menu = menu_header(header_string)
        options_menu = menu_options(menu_list)

        print(header_menu)
        print(options_menu)
        input_user = user_input(user_string)

        if input_user == "1":
            list_of_items(store)
        elif input_user == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total quantity of all products in the store: {total_quantity}")
        elif input_user == "3":
            shopping_list = add_to_shopping_list(store)
            if shopping_list:
                total_price = store.order(shopping_list)
                print(f"Total price of order: ${total_price}")
            else:
                print("No items were added to the shopping list.")
        elif input_user == "4":
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please select again.")


if __name__ == "__main__":
    main()