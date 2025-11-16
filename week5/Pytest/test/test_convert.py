import pytest
from week5.Pytest.convert import convert

def test_convert():
    assert convert(1) == 149597870700
    assert convert(50) == 50 * 149597870700

#todo 用来测试是否会引发我们期待的错误
def test_error():
    with pytest.raises(TypeError):
        convert("1")
        convert("au")

def test_float_convert():
    assert convert(0.001) == pytest.approx(149597870)