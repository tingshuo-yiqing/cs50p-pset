import typer
from weather import load_weather
from tabulate import tabulate
from analyse import get_advise, get_compare_advise
import functools
from rich import print as rprint

app = typer.Typer()


def handle_weather_errores(func):
    """统一处理 weather.py 抛出的错误"""

    @functools.wraps(func)
    def wrapper(*argv, **kwargv):
        try:
            return func(*argv, **kwargv)

        except ValueError as e:
            print(f"输入错误: {e}")
            raise typer.Exit(code=1)
        except RuntimeError as e:
            print(f"系统错误: {e}")
            raise typer.Exit(code=1)
        except Exception as e:
            print(f"未知错误: {e}")
            raise typer.Exit(code=1)

    return wrapper


@app.command()
@handle_weather_errores
def search(
    city: str, advise: bool = typer.Option(False, "--advise", "-a", help="向AI获取建议")
):
    """处理fetch_city_data函数中抛出的异常"""

    info = load_weather(city)

    table_data = [[key, value] for key, value in info.items()]
    print(tabulate(table_data, tablefmt="plain"))

    if advise:
        advice = get_advise(city, info)
        rprint(f"\n[bold green]--- Gemini 的建议 ---[/bold green]")
        print(advice)


@app.command()
@handle_weather_errores
def compare(
    city1: str,
    city2: str,
    advise: bool = typer.Option(False, "--advise", "-a", help="向AI获取建议"),
):
    """比较两个城市的天气异同"""
    info1 = load_weather(city1)
    info2 = load_weather(city2)

    header = ["items", info1["Name"], info2["Name"]]
    table_data = [
        [key, info1[key], info2[key]] for key in info1.keys() if key != "Name"
    ]

    print(tabulate(table_data, headers=header, tablefmt="plain"))
    if advise:
        advice = get_compare_advise(table_data)
        rprint(f"\n[bold green]--- Gemini 的分析 ---[/bold green]")
        print(advice)

if __name__ == "__main__":
    app()
