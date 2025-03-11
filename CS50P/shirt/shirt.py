import sys
from PIL import Image
from PIL import ImageOps
import os
def main():
    shirt_printer()
def shirt_printer():
    try:
        if (os.path.splitext(sys.argv[1])[1] or os.path.splitext(sys.argv[2])[1]) not in [".jpg", ".jpeg", ".png"]:
            sys.exit(f"Not a photo file ")
        elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
            sys.exit("Input and output have different extensions")
        elif len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        with Image.open(sys.argv[1]) as input_im,Image.open("shirt.png") as tof_to_paste:
            im=ImageOps.fit(input_im,(600,600),method = 0,bleed = 0.0, centering =(0.5, 0.5))
            im.paste(tof_to_paste,tof_to_paste)
            im.show()
            im.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Could not read ",sys.argv[1])






if __name__ == "__main__":
    main()
