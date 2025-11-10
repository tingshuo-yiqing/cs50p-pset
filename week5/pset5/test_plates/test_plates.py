from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("AAA666") == True


def test_len():
    assert is_valid('') == False
    assert is_valid('H') == False
    assert is_valid('ADSUWB78243') == False

def test_num():
    assert is_valid("CS05") == False
    assert is_valid("5555") == False
    assert is_valid("50CS") == False

def test_order():
    assert is_valid("CS5C5") == False

def test_isaalnum():
    assert is_valid("CS50,") == False
    assert is_valid("CS50 ") == False
    assert is_valid("CS50.") == False
    assert is_valid("123") == False
    assert is_valid("ASDFFG") == True  # 可以全部为字母