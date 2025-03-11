from seasons import Seasons
import pytest
def test_seasons():
    test_date = "1999-01-01"
    result = str(Seasons(test_date))
    assert result=="Thirteen million, five hundred eighty-nine thousand, two hundred eighty minutes"
def test_invalid_date_format():
    with pytest.raises(SystemExit):
        Seasons("February 6th, 1998")
