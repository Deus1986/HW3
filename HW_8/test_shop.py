"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product_2():
    return Product("tinki_vinki", 350, "This is a tinki_vinki", 300)


@pytest.fixture
def empty_cart():
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
        product_quantity_before_sale = product.quantity
        product.buy(quantity)
        assert product.quantity == product_quantity_before_sale - quantity

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

    def test_add_product(self, empty_cart, product):
        empty_cart.add_product(product, 5)
        assert empty_cart.products[product] == 5
        empty_cart.add_product(product, 7)
        assert empty_cart.products[product] == 12

    def test_remove_one_product(self, empty_cart, product):
        empty_cart.add_product(product, 12)
        empty_cart.remove_product(product, 1)
        assert empty_cart.products[product] == 11

    def test_remove_more_quantity_of_product(self, empty_cart, product):
        empty_cart.add_product(product, 12)
        empty_cart.remove_product(product, 13)
        assert empty_cart.products == {}

    def test_remove_product_with_default_count(self, empty_cart, product):
        empty_cart.add_product(product, 12)
        empty_cart.remove_product(product)
        assert empty_cart.products == {}

    def test_remove_product_with_empty_cart(self, empty_cart, product):
        with pytest.raises(ValueError):
            empty_cart.remove_product(product)

    def test_clear_cart_with_products(self, empty_cart, product, product_2):
        empty_cart.add_product(product, 5)
        empty_cart.add_product(product_2, 5)
        assert empty_cart.products[product] == 5
        assert empty_cart.products[product_2] == 5
        empty_cart.clear()
        assert empty_cart.products == {}

    def test_assert_total_price(self, empty_cart, product_2):
        empty_cart.add_product(product_2, 40)
        total_price = empty_cart.get_total_price()
        assert total_price == product_2.price * 40

    def test_assert_total_price_more_than_one_product(self, empty_cart, product, product_2):
        empty_cart.add_product(product, 40)
        empty_cart.add_product(product_2, 20)
        total_price = empty_cart.get_total_price()
        assert total_price == product_2.price * 20 + product.price * 40

    def test_buy_products_from_cart(self, empty_cart, product, product_2):
        empty_cart.add_product(product, 40)
        empty_cart.add_product(product_2, 20)
        product_quantity_before_sale = product.quantity
        product_2_quantity_before_sale = product_2.quantity
        assert empty_cart.products[product] == 40
        assert empty_cart.products[product_2] == 20
        buy_status = empty_cart.buy()
        assert buy_status == "Success"
        assert product.quantity == product_quantity_before_sale - 40
        assert product_2.quantity == product_2_quantity_before_sale - 20

    def test_buy_products_from_cart_with_absent_necessary_quantity_of_goods(self, empty_cart, product, product_2):
        empty_cart.add_product(product, 40)
        empty_cart.add_product(product_2, 400)
        with pytest.raises(ValueError) as error:
            empty_cart.buy()
        assert str(error.value) == "Товара недостаточно"
