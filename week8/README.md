## 核心

不要在功能函数里写 input()，也不要在功能函数里直接 print。

功能函数应该接收参数并返回结果（或抛出异常/退出）。测试函数是就是测试这些返回值和预期的异常

测试类的话，应该`assert`被它们影响的属性或测试它们抛出的异常

### pset

#### season

`fromiosformat()`是`date`的**类方法**，可以将一`YYYY-MM-DD`的IOS格式的字符串转化为`date`对象。如果格式不对就会报`ValueError`错误，在这里`season.py`里可以用来验证输入

```python
def check_birthday(user_in):
    """ 验证逻辑 """
    try:
        return date.fromisoformat(user_in)
    except ValueError:
        sys.exit("Invalid date")
```

`datetime.date`对象重载了一个减法`-`可以将两个日期进行减法得到中间的天数对象，但不能直接print输出，因为相减后还是一个date类。用属性`days`输出

```python
now = date.today()
d = date.fromisoformat("1999-01-01")

diff = now - d

print(diff)
print(diff.days)
print(diff.total_seconds())
```

#### jar

