## 文件夹中的__init__.py

即便这个文件是空的，他也会告诉python这个文件夹是一个包(packages)而不仅仅是一个模块。

而`__init__.py`里面的内容与**包的导入方式**和**初始化行为**有关

### 用法
#### 1.一般初始化

```python
# utils/__init__.py
print("utils 包已被导入")

PI = 3.14159

def hello():
    print("Hello from utils!")
```
再导入调用：
```python
import utils
utils.hello()
print(utils.PI)
```

#### 2.`__all__` 控制导出内容
当我们使用`from package import *`，可以指定导入特定的模块

```python
__all__ = ["math_tools", "string_tools"]
```

这样只会导入这两个特定的模块，而不是所有

#### 3.封装与便捷导入

在`__init__.py`里导入:

```python
from .math_tools import add
from .string_tools import upper
```
这样用户就可以:
```python
from utils import add, upper
```
而不用写`from utils.math_tools import add`

## pytest库

1. pytest.raise()的用法

用于测试代码会不会抛出指定的异常。

通常用于验证你的函数在错误的输入下能否进行正确的报错

```python
import pytest

def test_example():
    with pytest.raises(ValueError):
        int("abc")  # 这里会抛出 ValueError
```
如果抛出了对应的异常则，测试通过否则失败


## isinstance函数

`isinstance(obj, type)` 用于判断一个对象是否是某种类型或其子类的实例。

### 用途

常用于**函数的独立性**，确保这个函数不依赖于其它模块也可以正常处理不合法的输入

`raise`关键字

1. 类型检查

```python
def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    return x * x
```

2. 测试时验证返回类型
   
```python
def test_square_type():
    assert isinstance(square(3), int)
```