
# 导入 Flask 类
from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义路由：当用户访问网站根路径 '/' 时，执行下面的函数
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'  # 返回给浏览器的内容

# 运行应用（仅在当前脚本被直接执行时运行）
if __name__ == '__main__':
    app.run(debug=True)  # debug=True 表示开启调试模式

