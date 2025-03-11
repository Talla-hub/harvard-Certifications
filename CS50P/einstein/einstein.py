def main():
    masse = int(input("give a mass \n m : "))
    print(einstein(masse))


def einstein(input):
    c=300000000
    return " E : " + str(input*(c**2))




main()

