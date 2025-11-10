while True:
    usr_in = input("Fraction: ").split('/')
    try:
        a, b = int(usr_in[0]), int(usr_in[1])

        if a > b or a < 0 or b < 0:
            continue

        p = 100 * (a / b)
        
        # gauge.py
        if 1 < p < 99:
            print(f'{p:.0f}%')  # 转化成百分数
        elif p <= 1:
            print("E")
        elif p >= 99:
            print("F")
        break

    except (ValueError, ZeroDivisionError):
        continue
