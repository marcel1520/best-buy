from store import *


def menu_header(header):
    return header


def menu_options(options_list):
    return options_list


def user_input(user_choice):
    return user_choice


def list_of_items():
    pass


def main():
    header_string = f"Store Menu\n{'-' * len('Store Menu')}"
    menu_list = (
        f"1. List all products in store\n"
        f"2. Show total amount in store\n"
        f"3. Make an order\n"
        f"4. Quit"
    )
    user_string = "Please choose a number: "

    header_menu = menu_header(header_string)
    options_menu = menu_options(menu_list)
    input_user = user_input(user_string)


    print(header_menu)
    print(options_menu)
    print(input_user)


if __name__ == "__main__":
    main()


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)
google = Product("Google Pixel 7", price=500, quantity=250)

bose.show()
mac.show()
google.show()

bose.set_quantity(1000)
bose.show()

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))