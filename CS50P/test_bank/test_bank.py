from bank import value

def test_hello():
    assert value("hello my friend")==0
def test_no_hello():
    assert value("What's up")==100
def test_one_h():
    assert value("Hye bro")==20
