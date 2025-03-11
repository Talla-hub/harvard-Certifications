def main():
    sentence = input("Input a Sentence: ")
    print(convert(sentence))


def convert(input):
    return input.replace(":)", "🙂").replace(":(" , "🙁")




main()
