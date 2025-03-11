import random

def main():

    guess_game()



def guess_game():
        n=input("Level : ")
        while True:
            if (n.isnumeric()  and int(n)<= 0) or (n.isalpha()) :
                n=input("Level : ")
            elif n.isnumeric() and int(n)>0:
                break
        g= random.randrange(1, int(n))
        guess=input("Guess : ")
        while True:
            if (guess.isnumeric()  and int(guess)<= 0) or (guess.isalpha()):
                guess=input("Guess : ")
            elif (guess.isnumeric() and g>int(guess)):
                print("Too small!")
                guess=input("Guess : ")
            elif (guess.isnumeric() and g<int(guess)):
                print("Too large!")
                guess=input("Guess : ")
            else:
                print("Just right!")
                exit()









if __name__ == "__main__":
    main()
