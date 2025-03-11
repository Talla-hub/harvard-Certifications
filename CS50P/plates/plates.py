def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s=s.strip()
    if (not s[0:2].isalpha()) or  s.islower() or len(s)> 6 or len(s)<2 or any(k in s for k in [".", ";", ",", ":"]) :
        return False
    j=0
    for i in s[2:]:
        if i.isnumeric():
            if i=="0" and j==0:
                return False
            j+=1
        if i.isalpha() and j!=0:
            return False
    return True





if __name__ == "__main__":
    main()

