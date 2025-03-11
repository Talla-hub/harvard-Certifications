import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        pattern=r"^([0-9]{1,2}):?([0-9]{2})? ([AMP]{2}) to ([0-9]{1,2}):?([0-9]{2})? ([AMP]{2})$"
        matche=re.search(pattern,s)


        if matche:
            if not matche.group(2) :
                m1=00
            if not matche.group(5):
                m2=00
            if matche.group(5) or matche.group(5):
                m1,m2=int(matche.group(2)),int(matche.group(5))
            if (1 <= int(matche.group(1)) <=12 and  matche.group(3) == "PM" ) or  (1 <=int(matche.group(4)) <=12  and matche.group(6) == "PM"):
                h1,h2=int(matche.group(1))+12,int(matche.group(4))+12
                if h1==24:
                    h1=12
                if h2==24:
                    h2=12
            if (matche.group(3) == "AM"):
                h1=int(matche.group(1))
                if h1==12:
                    h1=00
            if (matche.group(6) == "AM"):
                h2=int(matche.group(4))
                if h2==12:
                    h2=00

            if m1>=60 or m2>=60:
                raise ValueError("Not Allowed")

            return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
        raise  ValueError("Not Allowed")




if __name__ == "__main__":
    main()
