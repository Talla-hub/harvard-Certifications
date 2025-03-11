from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
def main():
    if (sys.argv[1] not in ["-f","--font"]) or (sys.argv[2] not in figlet.getFonts()):
        sys.exit("font doesn't exist")

    st=input("Input : ")
    print(figlet_convert(st))



def figlet_convert(st):
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
        return figlet.renderText(st)
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        return figlet.renderText(st)





if __name__ == "__main__":
    main()
