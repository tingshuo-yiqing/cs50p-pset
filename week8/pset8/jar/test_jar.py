from jar import Jar
import pytest

"""
测试类的时候一般测的是 方法 根据该方法的功能（对属性的影响）进行assert

测试函数的时候一般测试 返回值和非法输入
"""

def test_init():
    """ 测试初始化: 1.默认参数 2.自定义参数 3.非法参数"""
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

    jar2 = Jar(3)
    assert jar2.capacity == 3
    assert jar2.size == 0

    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    """ 测试打印方法 """
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    """ 测试deposit方法 """
    jar = Jar()

    with pytest.raises(ValueError):
        jar.deposit(-1) 

    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(4)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    """ 测试withdraw方法 """
    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(-3)

    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.withdraw(30)