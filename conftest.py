import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def test_correct_init_category():
    return Category("Смартфоны", "Cмартфоны, как средство не только коммуникации, "
                                 "но и получения дополнительных функций для удобства жизни", [1, 2, 3, 4])


@pytest.fixture
def test_correct_init_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
