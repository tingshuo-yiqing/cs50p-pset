import json
from module import Word

FILE_JSON = "words.json"

def save_progress(words, filename):
    """Word列表 -> json文件"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([w.to_dict() for w in words], file, ensure_ascii=False, indent=4)


def load_progress(filename):
    """json文件 -> 字典列表 -> Word类列表"""
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            return [Word.from_dict(item) for item in data]
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        print(f"文件{filename}不存在，已创建一个空的 JSON 文件")
        return []
