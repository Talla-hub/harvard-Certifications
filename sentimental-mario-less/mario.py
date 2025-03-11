def get_Height():
    while True:
        try:
            Height = int(input("Height: "))
            if Height < 1 or Height > 8:
                pass
            else:
                return Height
        except ValueError:
            pass


n = get_Height()
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("#"*i)
