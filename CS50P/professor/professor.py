import random
def main():
    print(f"Score : {generate_integer(get_level())}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass



def generate_integer(get_level):
    if get_level==1:
        start =0
        end=9
    elif get_level==2:
        start =10
        end=99
    elif get_level==3:
        start =100
        end=999
    score=0
    i=1
    j=1
    while i<=10 :
        x=random.randrange(start,end)
        y=random.randrange(start,end)
        r= x + y
        inp=input(f"{x} + {y} = ")

        while  j<4 :
                if ((inp.isnumeric())  and (int(inp)< 0 or int(inp)!=r) ) or (inp.isalpha()):
                    print("EEE")
                    if score>0:
                        score-=1
                    if j==3:
                        print(f"{x} + {y} = {r}")
                        i+=1
                        break

                    inp=input(f"{x} + {y} = ")
                    j+=1
                    i+=1

                elif (inp.isnumeric()) and (int(inp)==r):
                    score+=1
                    i+=1
                    break

    return score

if __name__ == "__main__":
    main()
