import pytest
from store import Store
from product import Product


def test_add_product():
    store = Store()
    product = Product("Test Product", price=100.0, quantity=20)

    store.add_product(product)

    assert product in store.products
    assert len(store.products) == 1

def test_add_invalid_product():
    store = Store()

    with pytest.raises(ValueError, match="Only instances of Product can be added."):
        store.add_product("not a product")

def test_buy_valid_quantity():
    product = Product("PhoneX", price=100, quantity=4)

    total_cost = product.buy(3)

    assert total_cost == 300
    assert product.quantity == 1

def test_buy_too_much():
    product = Product("PhoneX", price=100, quantity=4)

    with pytest.raises(ValueError, match="Not enough stock to complete purchase."):
        product.buy(5)

    assert product.quantity == 4

def test_product_deactivates_when_zero_quantity():
    product = Product("Laptop", price=1000, quantity=2)

    product.buy(1)
    assert product.quantity == 1
    assert product.is_active() is True

    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False

