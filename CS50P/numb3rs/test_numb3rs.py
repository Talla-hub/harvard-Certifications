from numb3rs import validate

def test_val():
    assert validate("222.222.123.44") == True
    assert validate("12.6.123.44") == True

def test_error():
    assert validate("222.222.123.cat") == False
    assert validate("cat") == False
    assert validate("255.255.255.256") == False
