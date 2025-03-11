def main():
    percentage = convert(input("What's fraction : "))
    print(gauge(percentage))






def convert(fraction):
    while True :
        try :
            x,y=fraction.split("/")
            d=int(x)/int(y)
            d=round(d*100)
            if 0<=d<=100:
                return d

        except (ValueError,ZeroDivisionError):
            fraction=input("What's fraction : ")


def gauge(percentage):
    if 1<percentage<99:
        return str(percentage) +"%"
    elif 99<=percentage<=100:
        return "F"
    elif percentage<=1:
        return "E"






if __name__ == "__main__":
    main()
