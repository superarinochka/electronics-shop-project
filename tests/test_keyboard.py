import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def test_item1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(test_item1):
    assert test_item1.__str__() == 'Dark Project KD87A'


def test_language(test_item1):
    assert test_item1.language == 'EN'


def test_change_lang(test_item1):
    assert test_item1.change_lang().language == 'RU'
    assert test_item1.change_lang().language == 'EN'
