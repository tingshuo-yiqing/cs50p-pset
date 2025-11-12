import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        temp = 0
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                temp += 1
                if ans == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    if temp == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                print("EEE")
                temp += 1
                if temp == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
                continue

    print(f"Score: {score}")

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