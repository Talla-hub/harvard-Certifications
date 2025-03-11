import re
import sys


def main():
    print(count(input("Input: ")))


def count(s):
    pattern=r'\bum\b'
    matche=re.findall(pattern,s,re.IGNORECASE)
    return len(matche)



if __name__ == "__main__":
    main()
