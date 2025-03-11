from working import convert
import pytest
def test_convert():
    convert("8:00 PM to 8:00 AM")=="20:00 to 08:00"
    convert("9 AM to 5 PM")=="09:00 to 17:00"
def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"
    assert convert("1:05 AM to 1:05 PM") == "01:05 to 13:05"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_convert_error():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("09 AM")

