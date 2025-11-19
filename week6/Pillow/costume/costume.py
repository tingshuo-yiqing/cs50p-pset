import sys
from PIL import Image

argv = sys.argv[1:]

images = []

for arg in argv:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)