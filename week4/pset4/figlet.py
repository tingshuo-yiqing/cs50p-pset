import sys
from random import choice
from pyfiglet import Figlet
# https://cs50.harvard.edu/python/psets/4/figlet/

figlet = Figlet()
fonts = figlet.getFonts()

user_in = sys.argv

if len(user_in) not in [1, 3]:
    exit("Invalid usage")
elif len(user_in) == 3 and user_in[1] not in ["-f", "--font"]:
    exit("Invalid usage")

if len(user_in) == 1:
    f = choice(fonts)
else:
    f = user_in[2]

figlet.setFont(font=f)

s = input("Input: ")

print("Output:\n", figlet.renderText(s))