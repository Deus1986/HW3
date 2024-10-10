"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) == True
        assert product.check_quantity(55) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False

    @pytest.mark.parametrize("quantity", [1, 55, 1000])
    def test_product_buy(self, product, quantity):
        # TODO напишите проверки на метод buy
        product.buy(quantity)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        cart.add_product(product, 7)
        assert cart.products[product] == 12

    def test_remove_one_product(self, cart, product):
        cart.add_product(product, 12)
        cart.remove_product(product, 1)
        assert cart.products[product] == 11

    def test_remove_more_quantity_of_product(self, cart, product):
        cart.add_product(product, 12)
        cart.remove_product(product, 13)
        assert cart.products == {}

    def test_remove_product_with_default_count(self, cart, product):
        cart.add_product(product, 12)
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_product_with_empty_cart(self, cart, product):
        with pytest.raises(ValueError):
            cart.remove_product(product)

    def test_clear_cart_with_products(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        cart.clear(product)
        assert not cart.products

    def test_assert_total_price(self, cart, product):
        cart.add_product(product, 40)
        total_price = cart.get_total_price()
        assert total_price == product.price * 40

    def test_buy_products_from_cart(self, cart, product):
        cart.add_product(product, 40)
        cart.buy()
