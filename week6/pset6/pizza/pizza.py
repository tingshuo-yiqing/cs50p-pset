import csv
import sys
import os
from tabulate import tabulate


def readcsv(filename):
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            header = reader.fieldnames

            ret = [list(row.values()) for row in reader]
        return header, ret
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    argv = sys.argv
    
    size = len(argv)

    if size == 1:
        sys.exit("Too few command-line arguments")
    elif size > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not argv[1].lower().endswith(".csv"):
        # name, ext = os.path.splitext(argv[1])
        # if ext.lower() != ".csv":
            sys.exit("Not a CSV file")
    
    filename = argv[1]
    header, csv_file = readcsv(filename)
    print(tabulate(csv_file, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()
