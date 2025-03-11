def main():
    sentence = input("Say something :  ").strip()
    print(shorten(sentence),end="")



def shorten(sentence):
    lst=list(sentence)
    sent=""
    for i in range(len(sentence)):
        if sentence[i].lower() in ["a","o","i","u","e"]:
            lst[i]=""
        sent+=lst[i]


    return sent





if __name__ == "__main__":
    main()
