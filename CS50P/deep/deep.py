def main():
    say = input("say anything you want ").lower().rstrip().lstrip()
    print(deep(say))


def deep(input):
    if input == "42" or input == "forty two" or input == "forty-two" :
        return "Yes"
    return "No"



main()
