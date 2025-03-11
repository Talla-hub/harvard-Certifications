import sys
import csv
def main():
    csv_formatting()
def csv_formatting():
    try:
        if (len(sys.argv)==3) and (not sys.argv[1].endswith(".csv")):
            sys.exit("Not a csv file")
        elif len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        with open(sys.argv[1],"r", newline='') as file,open(sys.argv[2],"w",newline='') as f:
            reader=csv.DictReader(file)
            writer=csv.DictWriter(f,fieldnames=['first', 'last','house'])
            writer.writeheader()
            for re in reader:
                last_name,first_name=re["name"].split(",")
                house=re["house"]
                writer.writerow({"first":first_name.strip(),"last":last_name.strip(),"house":house})



    except FileNotFoundError:
        sys.exit("Could not read ",sys.argv[1])






if __name__ == "__main__":
    main()
