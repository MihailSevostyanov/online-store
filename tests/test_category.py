import pytest
from src.category import Category


@pytest.mark.usefixtures("test_correct_init_category")
def test_init(test_correct_init_category):
    assert test_correct_init_category.name == 'Смартфоны'
    assert test_correct_init_category.description == ('Cмартфоны, как средство не только коммуникации, '
                                                      'но и получения дополнительных функций для удобства жизни')


def test_summ_numb(test_correct_init_category):
    assert test_correct_init_category.total_number_of_unique_products == 4
    assert test_correct_init_category.total_number_of_categories == 1
