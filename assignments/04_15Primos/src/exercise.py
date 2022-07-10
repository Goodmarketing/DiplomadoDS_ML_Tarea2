def primo(num):
    if num < 0:
        return False
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2:
        for i in range(2,num):
            if num % i > 0:
                return True
            else:
                return False

def main():
    num = int(input("Escribe un numero entero : "))
    x = primo(num)
    print(x)

if __name__ == '__main__':
    main()
