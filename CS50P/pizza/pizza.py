import sys
import csv
from tabulate import tabulate
def main():
    lines_of_code()
def lines_of_code():
    try:
        menu=[]
        if (len(sys.argv)==2) and (not sys.argv[1].endswith(".csv")):
            sys.exit("Not a csv file")
        elif len(sys.argv)<2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>2:
            sys.exit("Too many command-line arguments")
        with open(sys.argv[1]) as file:
            reader=csv.reader(file)
            for m in reader:
                menu.append(m)
            headers =[menu[0][0],menu[0][1],menu[0][2]]
            print(tabulate(menu[1:], headers, tablefmt="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")






if __name__ == "__main__":
    main()
