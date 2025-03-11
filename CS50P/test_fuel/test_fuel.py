from fuel import convert,gauge
import pytest
def test_convert():
        assert convert("3/4")==75
def teste_error():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("dog/cat")

def test_gauge():
    assert gauge(75)=="75%"
    assert gauge(0)=="E"
    assert gauge(1)=="E"

    assert gauge(100)=="F"
    assert gauge(99)=="F"

