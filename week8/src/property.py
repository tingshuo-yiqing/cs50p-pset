class Fruit:
    def __init__(self, name):
        self._name = name

     

def main():

    fruit = Fruit("apple")

    print(fruit._name)

if __name__ == "__main__":
    main()