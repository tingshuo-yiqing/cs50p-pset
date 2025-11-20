from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        # self.area = self.radius ** 2 * pi  # 属性初始化后确定了，area不随radius的变化而变化

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("半径必须为正数")
        self._radius = value

    @property
    def area(self):
        return self.radius ** 2 * pi  # 将求area的方法变成属性，此时area随radius的变化而变化

s = Circle(-1)

print(s.area)

s.radius = 2

print(s.area)