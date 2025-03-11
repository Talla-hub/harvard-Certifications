def main():
    calcul = input("write your computing expression ").strip()
    print(interpreter(calcul))


def interpreter(input):
        x,y,z = input.split()
        match y:
            case "+" :
                return float(x)+float(z)
            case "-":
                return float(x)-float(z)
            case "*":
                return float(x)*float(z)
            case "/" :
                if float(z)== 0:
                    return "z is must be different to 0"
                return float(x)/float(z)
            case _:
                return "computer expression is wrong"



main()
