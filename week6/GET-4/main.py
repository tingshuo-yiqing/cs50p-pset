import csv
from random import shuffle

FILENAME = "writing.csv"

class Word:
    def __init__(self, word, Chinese):
        self.word = word
        self.Chinese = Chinese
    
    def __str__(self):
        return f"{self.Chinese}: {self.word}"
    

def load_file(filename):
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            w = Word(row["word"], row["Chinese"])
            words.append(w)
    return words


# 暂时不用管
def append_word(filename, Word):
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer = csv.DictWriter(file, fieldnames=["word", "Chinese"])
        # 现在默认有标题
        writer.writerow({"word":Word.word, "Chinese":Word.Chinese})

def input_new_word():
    word = input("请输入单词: ").strip()
    if word == "help":
        content()
        return
    chinese = input("请输入意思: ").strip()
    if chinese == "help":
        content()
        return
    new_word = Word(word, chinese)
    append_word(FILENAME, new_word)
    print(f"{new_word} 添加成功!")


def user_input(word: Word):
    w = input(f"{word.Chinese}: ")
    return w


def practice():
    words = load_file(FILENAME)
    shuffle(words)
    size = len(words)
    for i, word in enumerate(words):
        print(f"本次共有{size}个单词，剩余{size-i}")
        ans = word.word
        while True:
            user_in = user_input(word)    
            if user_in == ans:
                print("🎉🎉🎉")
                break
            elif user_in == "next":
                print(word)
                break
            elif user_in == "break":
                print(f"\n===========已退出===========")
                return
            elif user_in == "help":
                content()
                return 
    print("🎉🎉🎉已全部复习完成🎉🎉🎉")

def content():
    print("===========开始今天的学习叭===========")
    print("1.练习模式请输入practice")
    print("2.添加新单词(word, Chinese)请输入add")
    print("3.如果需要帮助输入help")
    print("4.退出练习请输入break或Ctrl + C")

def main():
    content()
    try:
        while True:   
            pattern = input("请开始今天的计划: ")
            if pattern == "practice":
                practice()
            elif pattern == "add":
                input_new_word()
            elif pattern == "help":
                content()
            elif pattern == "break":
                return

    except ValueError:
        raise ValueError("请仔细看输入")
    
    except KeyboardInterrupt:
        print(f"\n===========已退出===========")
        return

if __name__ == "__main__":
    main()