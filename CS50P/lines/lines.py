import sys
def main():
    print(lines_of_code())






def lines_of_code():
    try:
        i=0
        if (len(sys.argv)==2) and (not sys.argv[1].endswith(".py")):
            sys.exit("Not a Python file")
        elif len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        with open(sys.argv[1],"r") as file:
            for l in file:
                if (not l.lstrip().startswith("#")) and (not l.isspace()):
                    #print(l,end="")
                    i+=1
            return i


    except FileNotFoundError:
        sys.exit("File does not exist")






if __name__ == "__main__":
    main()
