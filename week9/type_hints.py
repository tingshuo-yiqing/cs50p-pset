from __future__ import annotations  
from typing import Literal, Iterable
from datetime import datetime


class Student:
    def __init__(
        self,
        name: str,
        birthday: datetime | str,  # 类型也可以是一个类
        gender: Literal["male", "female"],  # 也可以自定义
        courses: list[str],
        scores: dict[str, int],
    ):
        self.name = name
        self.gender = gender
        self.courses = courses
        self.scores = scores

    def follow(self, other_student: Student):
        """当在类中用未完全定义完的类作为类型时，导入__future__的annotatons"""
        ...

    def __str__(self) -> str:
        return "这是一个__str__，具体懒得写了"


student = Student(
    "tingshuo",
    datetime.now(),
    "male",
    ["c", "python", "c++"],
    {"c": 100, "c++": 100, "python": 100},
)

print(student)


def my_sum(nums: Iterable[int]) -> int:
    return sum(nums)


print(my_sum([1, 2, 3, 4, 5]))
print(my_sum((1, 2, 3, 4, 5)))