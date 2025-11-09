data = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    d = input("Date: ")

    if '/' in d:
        try:
            m, day, y = map(int, d.split('/'))
            if m > 12 or m < 1 or day > 32:
                continue 
            print(f"{y}-{m:02}-{day:02}")
            break
        except ValueError:
            continue

    try:
        d = d.split()

        if d[0] not in data or ',' not in d[1]:
            continue
        m, y, day = data.index(d[0]), int(d[2]), int(d[1].replace(',', ''))
        if day > 31:
            continue
        print(f"{y}-{m:02}-{day:02}")
        break
    except ValueError:
        continue