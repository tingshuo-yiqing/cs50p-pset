class Student:

    student_nums = 0
    teacher = "sensi"

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Student.student_nums += 1

    @classmethod
    def count_student(cls):
        return f"有{cls.student_nums}个学生"
    
    @staticmethod
    def foo():             
        print("这是一个静态方法")
    

st1 = Student("tingshuo", "man")
st2 = Student("yiqing", "woman")

print(st1.student_nums)  # 对象调用类属性
print(Student.student_nums)  # 类调用类属性
print(Student.count_student())  # 类调用类函数

print(vars(st1))
st1.teacher = "hhh"
print(vars(st1))
print(st1.teacher)  
print(Student.teacher)
print(st2.teacher)

n = input("请输入属性: ")
print(hasattr(st1, n))
print(getattr(st1, n))
delattr(st1, n)
print(hasattr(st1, n))