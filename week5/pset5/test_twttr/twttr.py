def main():
    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    lowercases = "aeiou"
    uppercases = "AEIOU"
    word = [i for i in word if i not in "aeiouAEIOU"]
    # mistake version
    # word = [i for i in word if i not in lowercases]
    # word = [i for i in word if i not in uppercases]

    return ''.join(word)

if __name__ == "__main__":
    main()
