import pytest
from twttr import shorten

def test_str():
    assert shorten("What's your name 221")=="Wht's yr nm 221"
def test_without_cap():
    assert shorten("mOr talla dia")=="mr tll d"
def test_char():
    assert shorten("@!%")=="@!%"
