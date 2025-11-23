import argparse

parse = argparse.ArgumentParser(description="像猫一样喵喵叫")

parse.add_argument("-n", default=1, help="喵叫的次数", type=int)
parse.add_argument("-e", help="猫在吃鱼")

args = parse.parse_args()

for _ in range(args.n):
    print("喵~")

print(args.e)