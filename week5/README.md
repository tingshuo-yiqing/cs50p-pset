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

