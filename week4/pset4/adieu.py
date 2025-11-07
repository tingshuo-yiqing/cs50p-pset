import sys

import inflect
p = inflect.engine()

names = []

try:
    while True:
        names.append(input())  # 没有 "Name:" 提示可以过
except EOFError:
    print(f"Adieu, adieu, to {p.join(names)}")
    sys.exit()

# try:
#     while True:
#         names.append(input("Name: "))
# # 捕获 Ctrl + D
# except EOFError:
#     print("\nAdieu, adieu, ",end='')
#     n = len(names)
#     if n == 1:
#         print(f"to {names[0]}")
#     elif n == 2:
#         print(f"to {names[0]} and {names[1]}")
#     else:
#         print(f"to {names[0]}, ", end='')
#         for i in range(1, n-1):
#             print(f"{names[i]}, ",end='')
#         print(f"and {names[-1]}")
#     sys.exit()