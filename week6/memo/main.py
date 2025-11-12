import json

data = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "hobbies": ["读书", "游泳", "编程"],
    "is_student": False 
}

json_string = json.dumps(data, ensure_ascii=False, indent=4)

print(json_string)

python_dict = json.loads(json_string)

print(python_dict["hobbies"])

with open("progress.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

with open("progress.json", encoding="utf-8") as file:
    l = json.load(file)

print(l)