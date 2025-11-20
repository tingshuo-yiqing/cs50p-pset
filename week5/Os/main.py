import os
from datetime import date

name = os.name
print(name)

cwd = os.getcwd()
print(cwd)


path = os.path.join(os.getcwd(), "", "os.md")
print(path)

dir_name, file_name = os.path.split(path)
print(dir_name, file_name)

now = date.today()
d = date.fromisoformat("1999-01-01")

diff = now - d

print(diff)
print(diff.days)
print(diff.total_seconds())