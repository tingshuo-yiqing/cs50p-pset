def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    
    print(f"{au} AU is {convert(au)} m")


def convert(au):
    """ 函数独立性原则，其不能依赖main函数里try """

    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700

if __name__ == "__main__":
    main()