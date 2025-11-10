## 本周可以学习到：

1. 捕获`Ctrl + D`
```python
try:
    item = input()
except EOFError:
    ...
``` 
捕获`Ctrl + C`的`KeyboardInterrupt`和捕获除0的`ZeroDivisionError`


2. 常见格式方法
```python
print(f"{n:02}") # 前导0

print(f"{val:.xf}") # 格式化小数位数，保留小数点后x位
```
