import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip_add):
    # try:
        pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
        if ma := re.search(pattern, ip_add):
            parts=[int(ma.group(i)) for i in range(1,5)]
            if all(0<=part<=255 for part in parts):
                return True
        return False
    # except AttributeError:
    #     sys.exit("False")






if __name__ == "__main__":
    main()
