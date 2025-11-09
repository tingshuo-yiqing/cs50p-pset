from twttr import shorten

def test_lowwercase():
    assert shorten('1asdef') == '1sdf'
    assert shorten('1sdf') == '1sdf'
    assert shorten('aeiou') == ''

def test_uppercase():
    assert shorten('1Asdef') == '1sdf'
    assert shorten('AEIOU') == ''

def test_omitting():
    assert shorten('') == ''

def test_numbers():
    assert shorten('123') == '123'
    assert shorten('1a23') == '123'

def test_punctuation():
    assert shorten('as123,.,.') == 's123,.,.'
    assert shorten('a,.,.') == ',.,.'
    assert shorten(',.,.') == ',.,.'