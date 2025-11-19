import sys
from datetime import date
import inflect
p = inflect.engine()

def check_birthday(user_in):
    """ 验证逻辑 """
    try:
        return date.fromisoformat(user_in) 
    except ValueError:
        sys.exit("Invalid date")


def calc_minutes(birthday):
    """ 计算逻辑 """
    now_date = date.today()
    minutes = p.number_to_words((now_date-birthday).days * 24 * 60, andword="")  # 去掉and
    
    return minutes.capitalize()


def main():
    """ 主函数里输入 """
    birthday = check_birthday(input("Date in Brith:"))

    print(f"{calc_minutes(birthday)} minutes")

if __name__ == "__main__":
    main()