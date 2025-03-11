from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar
    with pytest.raises(ValueError):
        Jar(-12)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(13)
