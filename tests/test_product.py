import pytest
from src.product import Product


@pytest.fixture
def test_correct_init_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_for_second_class(test_correct_init_product):
    assert test_correct_init_product.name == 'Samsung Galaxy C23 Ultra'
    assert test_correct_init_product.description == '256GB, Серый цвет, 200MP камера'
    assert test_correct_init_product.price == 180000.0
    assert test_correct_init_product.quantity == 5
