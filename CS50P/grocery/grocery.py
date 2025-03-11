def main():
    grocery_list()

def grocery_list():
    try:
        lst=[]
        while True:
            l=input()
            lst.append(l)
    except EOFError:
        lst.sort()
        d={}
        for t in lst:
            d[t.upper()]=lst.count(t)
        for t in d:
            print(f"{d[t]} {t}")


if __name__ == "__main__":
    main()
