import csv
import sys

def readcsv(read_file, modify_file):
    try:
        with open(read_file, encoding="utf-8") as read, open(modify_file, "w", newline="", encoding="utf-8") as write:
            reader = csv.DictReader(read)

            writer = csv.DictWriter(write, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                name = row["name"].split(", ")
                new_row = {
                    "first": name[1],
                    "last": name[0],
                    "house": row["house"]
                }
                writer.writerow(new_row)

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


def main():
    argv = sys.argv
    size = len(argv)
    if size == 1:
        sys.exit("Too few command-line arguments")
    elif size > 3:
        sys.exit("Too many command-line arguments")

    before, after = argv[1], argv[2]
    readcsv(before, after)


if __name__ == "__main__":
    main()