import inflect

p = inflect.engine()
def main():
    print(adieu_song())



def adieu_song():

    try :
        lst=[]
        while True:
            st=input("name :")
            lst.append(st)

    except EOFError:
        mylist = p.join(tuple(lst))
        return "Adieu, adieu, to " + mylist




if __name__ == "__main__":
    main()
