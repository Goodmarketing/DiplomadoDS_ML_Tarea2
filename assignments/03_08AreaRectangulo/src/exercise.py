def area(base,altura):
    area = base * altura
    print(f"El área del rectángulo es: {area}")

def main() :
    base = float(input("Dame la base: "))
    altura = float(input("Dame la altura: "))
    area(base,altura)

if __name__=='__main__':
    main()
