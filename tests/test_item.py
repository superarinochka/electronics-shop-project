import os.path
import pytest
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError
# item1 = Item("Смартфон", 1000, 20)
# item2 = Item("Ноутбоук", 20000, 5)


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
# def test_instantiate_from_csv(item):
#    item.instantiate_from_csv("src/items.csv")
#    assert len(Item.all) == 5
file_path = os.path.join(os.path.dirname(__file__), 'items.csv')


def test_instantiate_from_csv_2():
    with pytest.raises(FileNotFoundError, match='Отстутствует файл'):
       Item.instantiate_from_csv('item.csv')

def test_instantiate_from_csv_3():
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv('items.csv')


def test_repr(item):
    assert item.__repr__() == "Item('Смартфон', 1000.0, 20)"


def test_str(item):
    assert item.__str__() == "Смартфон"

def test_add(item, test_phone1):
    assert test_phone1 + item == 25
