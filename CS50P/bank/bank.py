def main():
    greet = input("say anything you want ").lower().rstrip().lstrip()
    print(bank(greet))


def bank(input):
    if "hello" in input :
        return "$0"
    elif input[0]=="h" and not("hello" in input):
        return "$20"
    return "$100"



main()
