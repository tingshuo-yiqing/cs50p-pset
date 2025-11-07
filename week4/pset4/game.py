from random import randint

up = input("Level: ")
while not up.isdigit():
    up = input("Level: ")

up = int(up)
goal = randint(1, up)

# 合理判断输入的合法性
while True:
    try:
        use_int = int(input("Guess: "))
        if use_int <= 0:
            continue
        if use_int > goal:
            print("Too large!")
        elif use_int < goal:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass