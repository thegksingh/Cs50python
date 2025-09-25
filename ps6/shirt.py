from PIL import Image, ImageOps
import sys


def main():
    file_to_open, file_to_save = number_arguments()
    check_extension(file_to_open, file_to_save)
    try:
        image = Image.open(file_to_open)
    except FileNotFoundError:
        sys.exit("File not found")
    shirt = Image.open("shirt.png")
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, (0, 0), shirt)
    image.save(file_to_save)


def number_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line argumnets")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line argumnets")
    else:
        file_to_open = sys.argv[1]
        file_to_save = sys.argv[2]
        return file_to_open, file_to_save


def check_extension(file_to_open, file_to_save):
    file_to_open = file_to_open.lower()
    file_to_save = file_to_save.lower()
    if not file_to_open.endswith(
        (".jpg", ".jpeg", ".png")
    ) or not file_to_save.endswith((".jpg", ".jpge", ".png")):
        sys.exit("Invalid file extension input")
    else:
        name, extention = file_to_open.split(".")
        name2, extention2 = file_to_save.split(".")
        if extention != extention2:
            sys.exit("Input and Output have different extensions")


if __name__ == "__main__":
    main()
