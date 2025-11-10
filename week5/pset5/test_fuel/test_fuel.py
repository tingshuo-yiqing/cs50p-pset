from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/2') == 50


def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(5) == '5%'


def test_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0') # 避免进入 a > b
    with pytest.raises(ValueError):
        convert('a/b')
    with pytest.raises(ValueError):
        convert('-1/2')
    with pytest.raises(ValueError):
        convert('1/-2')
    with pytest.raises(ValueError):
        convert('3/2') 