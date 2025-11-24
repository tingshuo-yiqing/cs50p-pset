try:
    x = 1 / 0
except ZeroDivisionError as e:
    # 此时 e 是一个异常对象
    print(f"错误类型: {type(e)}")
    print(f"错误信息: {e}") # 打印具体的报错信息 "division by zero"
    # 你还可以记录日志： logger.error(e)