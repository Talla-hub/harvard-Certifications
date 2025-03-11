def main():
    user_input=input("Tape your something ")
    print(playback(user_input))
def playback(input):
    return input.replace(" ","...")
main()
