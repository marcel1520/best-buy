class Product:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be integer")
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert len(name) >= 5, f"Product name must be at least 5 characters long!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be integer")
        if quantity < 0:
            raise ValueError(f"Quantity {quantity} cannot be less than zero!")
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.quantity > 0

    def activate(self):
        if self.quantity <= 0:
            self.quantity = 1
        print(f"{self.name} has been activated.")

    def deactivate(self):
        self.set_quantity(0)
        print(f"{self.name} has been deactivated")

    def show(self):
        return f"{self.name}, {self.price}, {self.quantity}"

    def buy(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be integer")
        if not self.is_active:
            raise ValueError(f"Product {self.name} is inactive and cannot be purchased")
        if quantity > self.quantity:
            raise ValueError("Not enough stock to complete purchase.")
        if quantity <= 0:
            raise ValueError("Quantity must be larger zero.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity

