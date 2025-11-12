import csv
from random import randint

left = 0
right = 100

def input_file(filename):
    with open(filename, "w", newline="") as views:
        writer = csv.DictWriter(views, fieldnames=["x", "y", "add", "sub"])
        writer.writeheader()  # 写入标题头
        for _ in range(20):
            x = randint(left, right)
            y = randint(left, right)
            writer.writerow(
                {
                    "x": x,
                    "y": y,
                    "add": x + y,
                    "sub": x - y,
                }
            )

def modify_file(filename1, filename2):
    with open(filename1, "r") as file_reader, open(filename2, "w", newline="") as result:
        reader = csv.DictReader(file_reader)
        writer = csv.DictWriter(result, fieldnames=reader.fieldnames + ["mul"]) # 不变的标题直接和reader的一样
        writer.writeheader()
        for row in reader: 
            row["mul"] = calculate_mul(int(row["x"]), int(row["y"]))
            writer.writerow(row)


def main():
    input_file("views.csv")
    modify_file("views.csv", "result.csv")


def calculate_mul(x, y):
    return x * y

if __name__ == "__main__":
    main()