import sys
import os
from PIL import Image,ImageOps


def image_procress(input_image, overlay_image):
    try:
        with Image.open(input_image) as photo, Image.open(overlay_image) as shirt:
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, (0, 0), shirt) # 第三个参数防止透明区域变成黑色

            photo.save("after.jpg")

    except FileNotFoundError:
        sys.exit("图片不存在")


def main():
    image_procress("before1.jpg", "shirt.png")

if __name__ == "__main__":
    main()