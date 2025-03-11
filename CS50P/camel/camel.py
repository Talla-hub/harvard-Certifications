def main():
    camel = input("camel case writings :  ").strip()
    print("sneak case : ",sneak_case(camel))



def sneak_case(camel):
    newcamel=""
    lst=""
    for i in range(len(camel)):
        newcamel = camel[i]
        if camel[i]==camel[i].upper():
            newcamel ="_"+ camel[i]
        lst+=newcamel

    return lst.lower()

if __name__ == "__main__":
    main()
