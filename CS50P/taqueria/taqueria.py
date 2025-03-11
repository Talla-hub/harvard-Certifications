def main():
    menu()


def menu():
    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    try:
        tot=0
        while True :
            s=input("Items: ").lower().title().strip()
            if s in menu.keys():
                tot+=menu[s]
                print(f"Total : ${tot:0.2f}")
    except EOFError:
        print("\n",end="")










if __name__ == "__main__":
    main()
