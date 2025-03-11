def main():
    time = input("what time is it ?").strip()
    if 7<=convert(time)<=8:
        print ("breakfast time")
    elif 12<=convert(time)<=13:
        print ("lunch time")
    elif 18<=convert(time)<=19:
        print ("dinner time")
    return print ("")



def convert(time):
    h,m = time.split(":")
    return float(h) + float(m)/60

if __name__ == "__main__":
    main()
