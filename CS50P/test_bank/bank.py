def main():
    greet = input("say anything you want ").lower().strip()
    print(f"${value(greet)}")


def value(input):
    if "hello" in input :
        return 0
    elif input[0]=="h" and not("hello" in input):
        return 20
    return 100


if __name__ == "__main__":
    main()
