def main():
    coin = int(input("insert a coin :  ").strip())
    print(coke_machine(coin))



def coke_machine(coin):
    s=0
    while coin not in [25,5,10] :
            print("Amount Due: " + str(50-s))
            coin = int(input(" coin not accepted insert -->25,10,5 cents :  ").strip())
    s=int(coin)
    while s < 50:
        print("Amount Due: " + str(50-s))
        coin = input("insert a coin :  ").strip()
        s+=int(coin)

    if s >= 50 :
        return "Change Owed: " + str(s - 50)




if __name__ == "__main__":
    main()
