from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""

def test_item2():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.price == 10000
