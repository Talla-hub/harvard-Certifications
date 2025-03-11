       # if type(x) is not int or type(y) is not int or (x>y):
        #    raise ValueError("Non ok")

def main():
    print(fuel_indication())
def fuel_indication():
    while True:
        try:
            item=input("What's x ")
            x,y=item.split("/")
            d=int(x)/int(y)
            d=round(d*100)
            if 1<d<99:
                return str(d) +"%"
            elif 99<=d<=100:
                return "F"
            elif d<=1:
                return "E"

        except (ValueError,ZeroDivisionError):
            pass






if __name__ == "__main__":
    main()
