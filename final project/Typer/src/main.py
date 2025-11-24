import typer
import json
from weather import load_weather
from tabulate import tabulate

app = typer.Typer()


@app.command()
def search(
    city: str, advise: bool = typer.Option(False, "--advise", "-a", help="向AI获取建议")
):
    
    """ 处理fetch_city_data函数中抛出的异常 """
    try:
        info = load_weather(city)

        table_data = [[key, value] for key, value in info.items()]
        print(tabulate(table_data, tablefmt="plain"))
    except ValueError as e:
        print(f"❌ 查询失败: {e}")
        raise typer.Exit(code=1)
    except RuntimeError as e:
        print(f"⚠️ 系统错误: {e}")
        raise typer.Exit(code=1)


@app.command()
def compare(city1: str, city2: str):
    info1 = load_weather(city1)
    info2 = load_weather(city2)


if __name__ == "__main__":
    app()
