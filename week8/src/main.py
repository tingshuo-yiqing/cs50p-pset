
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 在发出声音"
    
    def eat(self):
        return f"{self.name} 嚼嚼嚼"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} 汪汪汪"
    
    def eat(self):
        return super().eat()


def main():
    dog = Animal("大狗大狗")
    print(dog.eat())
    print(dog.speak())

    ddog = Dog("小狗小狗")
    print(ddog.speak())


if __name__ == "__main__":
    main()