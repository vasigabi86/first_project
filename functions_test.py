from gyaksz6 import print_osszead

from gyaksz6 import print_space


def test_print_osszead():
    result = print_osszead(2, 3)
    assert result == 5


def test_print_space():
    result = print_space("asdasdasdas")
    assert result == 0
