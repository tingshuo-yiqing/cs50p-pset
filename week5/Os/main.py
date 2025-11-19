import os

name = os.name
print(name)

cwd = os.getcwd()
print(cwd)


path = os.path.join(os.getcwd(), "", "os.md")
print(path)

dir_name, file_name = os.path.split(path)
print(dir_name, file_name)