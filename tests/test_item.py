from src.item import Item
import pytest
from src.phone import Phone
"""Здесь надо написать тесты с использованием pytest для модуля item."""

@pytest.fixture
def item():
    return Item("Смартфон", 1000.0, 20)


@pytest.fixture
def test_phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(item):
    assert item.price == 1000.0
    assert item.name == "Смартфон"
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 20000
    assert type(item.calculate_total_price()) is float


def test_name(item):
    item.name = "Смартфонсмартфон"
    assert item.name == "Смартфонсм"
    assert len(item.name) == 10


def test_apply_discount(item):
    assert item.price == 1000.0
    item.pay_rate = 0.15
    item.apply_discount()
    assert item.price == 150.0


def test_string_to_number(item):
    assert item.string_to_number("5.0") == 5
    assert item.string_to_number("6.5") == 6


def test_instantiate_from_csv(item):
    item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5


def test_repr(item):
    assert item.__repr__() == "Item('Смартфон', 1000.0, 20)"


def test_str(item):
    assert item.__str__() == "Смартфон"

def test_add(item, test_phone1):
    assert test_phone1 + item == 25
