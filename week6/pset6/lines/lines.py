import sys

argv = sys.argv

size = len(argv)

if size == 1:
    sys.exit("Too few command-line arguments")
elif size > 2:
    sys.exit("Too many command-line arguments")
else:
    s = argv[1].split('.')
    if s[-1] != "py":
        sys.exit("Not a Python file")


def count_filelines(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()  # 去空行
            if line and not line.startswith("#"):  # 检查注释
                count += 1
    return count


def main():
    try:
        lines = count_filelines(argv[1])
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
