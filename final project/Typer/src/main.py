import typer
from weather import load_weather
from tabulate import tabulate
from analyse import get_advise
import functools
from rich import print as rprint

app = typer.Typer()


@app.command()
def search(
    city: str, advise: bool = typer.Option(False, "--advise", "-a", help="向AI获取建议")
):
    """处理fetch_city_data函数中抛出的异常"""
    try:
        info = load_weather(city)

        table_data = [[key, value] for key, value in info.items()]
        print(tabulate(table_data, tablefmt="plain"))

        if advise:
            advice = get_advise(city, info)
            rprint(f"\n[bold green]--- Gemini 的建议 ---[/bold green]")
            print(advice)
    except ValueError as e:
        print(f"❌ 查询失败: {e}")
        raise typer.Exit(code=1)
    except RuntimeError as e:
        print(f"⚠️ 系统错误: {e}")
        raise typer.Exit(code=1)


@app.command()
def compare(city1: str, city2: str):
    """比较两个城市的天气异同"""
    info1 = load_weather(city1)
    info2 = load_weather(city2)


if __name__ == "__main__":
    app()
