import csv
from random import shuffle
from module import Word
from progress import save_progress, load_progress

FILE_JSON = "words.json"

def load_file():
    words = load_progress(FILE_JSON)
    return words


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
    words = load_file()
    words.append(new_word)
    save_progress(words, FILE_JSON)
    print(f"{new_word} 添加成功!")


def user_input(word: Word):
    return input(f"{word.Chinese}: ")


def practice():
    words = load_file()
    shuffle(words)
    size = len(words)
    for i, word in enumerate(words):
        print(f"本次共有{size}个单词，剩余{size-i}")
        ans = word.word
        while True:
            user_in = user_input(word).lower().strip()
            if user_in == ans:
                word.correct_count += 1
                print("🎉🎉🎉")
                break
            elif user_in == "next":
                print(word)
                break
            elif user_in == "break":
                print(f"\n===========已退出===========")
                save_progress(words, FILE_JSON)
                return
            elif user_in == "help":
                content()
                return 
            else:
                word.error_count += 1
    save_progress(words, FILE_JSON)
    print("🎉🎉🎉已全部复习完成🎉🎉🎉")


def content():
    print("===========开始今天的学习叭===========")
    print("1.练习模式请输入practice")
    print("2.添加新单词(word, Chinese)请输入add")
    print("3.如果需要帮助输入help")
    print("4.退出练习请输入exit或Ctrl + C")


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
                continue
            elif pattern == "exit":
                return

    except ValueError:
        raise ValueError("请仔细看输入")
    
    except KeyboardInterrupt:
        print(f"\n===========已退出===========")
        return

if __name__ == "__main__":
    main()