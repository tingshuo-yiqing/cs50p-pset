def main():
    ...


def is_valid(s):
    n = len(s)
    if n < 2 or n > 6:
        return False
    
    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False
    
    number_state = False
    for ch in s:
        if ch.isdigit():
            if not number_state:
                if ch == '0':
                    return False
                number_state = True
        else: # 如果是字母
            
            if number_state:
                return False

    return True


if __name__ == "__main__":
    main()