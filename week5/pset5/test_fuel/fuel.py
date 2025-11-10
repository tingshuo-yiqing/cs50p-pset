def main():
    usr_in = input("Fraction: ")
    print(gauge(convert(usr_in)))


def convert(fraction):
    try:
        fraction = fraction.split('/')
        a, b = int(fraction[0]), int(fraction[1])

        if b == 0:
            raise ZeroDivisionError
        if a < 0 or b < 0 or a > b:
            #! 这里 1/0的话会进入ValueError，但是它期望的是ZeroDivisionError
            raise ValueError # 不合法数字

        return int(100 * (a / b))

    except (ValueError, ZeroDivisionError): 
        raise  # 不是数字

def gauge(percentage):
    if 1 < percentage < 99:
        return f'{percentage:.0f}%'  # 转化成百分数
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"


if __name__ == "__main__":
    main()