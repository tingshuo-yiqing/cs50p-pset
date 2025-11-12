import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += check(x, y)
    print(f"Score: {score}")

def check(x, y):
    temp = 0
    while temp < 3:
        try:
            temp += 1
            ans = int(input(f"{x} + {y} = "))
            if ans == x + y:
                return 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")
            pass
    print(f"{x} + {y} = {x + y}")
    return 0

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level-1) , 10 ** level - 1)


if __name__ == "__main__":
    main()