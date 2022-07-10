def pares_en_rango(inf,sup):
    if inf == sup:
        if inf % 2 == 0:
            print(inf)
        elif inf % 2 != 0:
            print('No hay pares')
    if inf != sup and inf < sup:
        if inf % 2 == 0:
            for i in range(inf,sup+1,2):
                print(f'{i}')
        elif inf % 2 != 0:
            for i in range(inf+1,sup+1,2):
                print(f'{i}')
    if sup < inf:
        if sup % 2 == 0:
            for i in range(sup,inf+1,2):
                print(f'{i}')
        elif sup % 2 != 0:
            for i in range(sup+1,inf+1,2):
                print(f'{i}')
    
def main():
    inf = int(input("Valor 1: "))
    sup = int(input("Valor 2: "))
    pares_en_rango(inf,sup)

if __name__ == '__main__':
    main()
