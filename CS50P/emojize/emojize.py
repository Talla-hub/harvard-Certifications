import emoji

def main():
    st=input("Input : ")
    print(emoji_convert(st))



def emoji_convert(st):
    return emoji.emojize(st,language='alias')



if __name__ == "__main__":
    main()
