"""
在静态语言中必须硬编码属性，这样会把属性写死。

于是我们可以使用getattr和setsttr来将字符串转化为可以访问的属性
"""

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number

student = Student("小明", 114514)
attr = input("请输入属性: ")

name = getattr(student, attr)
# 等价于 name = student.attr
print(name)

setattr(student, attr, 123456789)
# 相当于 student.attr = 123456789
print(student.number)