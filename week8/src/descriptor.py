""" 
在property.py里验证一个属性radius的合法性所以看不出什么问题

现在的Rectangle有两个属性验证方式一模一样就变得很重复了

所以现在引入了 [描述符] 的概念: 把一个类的属性的访问交给另一个类处理
"""

class PositiveNumber:
    def __set_name__(self, owner, name):
        """ 实现不同的属性应用同一套模板 """
        self.private_name = f"_{name}" 


    def __get__(self, instance, owner):
        """ 表示获取owner类的instance实例的属性 """
        return getattr(instance, self.private_name) 


    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f'{self.private_name[1:].capitalize()} is required to be a positive number!')
        
        setattr(instance, self.private_name, value)
    

class Rectangle:
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(2, 2)
print(r.__dict__)
# r.width = -1
r.height = -1
print(r.width)