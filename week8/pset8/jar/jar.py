class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity # __init__初始化也走一遍setter，少一次raise判断
        self._size = 0   # 只getter不setter，即内部可变外部只读

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0 or self._size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 or self._size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError
        self._capacity = value

    @property
    def size(self):
        return self._size

