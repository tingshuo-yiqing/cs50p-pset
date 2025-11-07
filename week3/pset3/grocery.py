from collections import Counter

items = Counter()

while True:
    try:
        items[input()] += 1
    except EOFError:
        for item, count in sorted(items.items()):
            print(count, item.upper())
        break