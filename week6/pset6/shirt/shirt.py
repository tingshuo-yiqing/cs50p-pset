import sys
from PIL import Image, ImageOps

SHIRT = "shirt.png"

def argv_process():
    argv = sys.argv
    size = len(argv)

    if size < 3:
        sys.exit("Too few command-line arguments")
    elif size > 3:
        sys.exit("Too many command-line arguments")
    else:
        first_ext = argv[1].split('.')[-1].lower()
        second_ext = argv[2].split('.')[-1].lower()

        if second_ext not in ["jpg", "jpeg", "png"]:
            sys.exit("Invalid output")
        if first_ext != second_ext:
            sys.exit("Input and output have different extensions")

    return argv[1], argv[2]


def image_process(photo_image, after_image):
    try:
        with Image.open(photo_image) as photo, Image.open(SHIRT) as shirt:
            
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, (0, 0), shirt)  # 第三个参数是确保透明区域不会变黑
            photo.save(after_image)

    except FileNotFoundError:
        sys.exit("Input does not exist")


def main():
    first_image, after_image = argv_process()
    image_process(first_image, after_image)


if __name__ == "__main__":
    main()
