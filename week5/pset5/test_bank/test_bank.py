from bank import value

def test_null():
    assert value('') == 100

def test_valid():
    assert value('Hello') == 0
    assert value('HELLO') == 0
    assert value('hello') == 0

def test_unvalid():
    assert value('hell0') == 20
    assert value('Hell0') == 20

def test_normal():
    assert value('sdjfiueiwofh') == 100