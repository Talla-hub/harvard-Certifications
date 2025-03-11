from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("AB1234") == True
    assert is_valid("CS50") == True


def test_invalid_start_with_number():
    assert is_valid("12CS50") == False
    assert is_valid("12CS50") == False

def test_invalid_length():
    assert is_valid("NRVO0US") == False
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("PI3.14") == False
    assert is_valid("OUTATIME") == False
def test_invalid_zero():
    # Plates with improper zero placement
    assert is_valid("CS05") == False     # No leading zeros in the number part
    assert is_valid("AB0123") == False   # Leading zero in the middle
    assert is_valid("CS0") == False





