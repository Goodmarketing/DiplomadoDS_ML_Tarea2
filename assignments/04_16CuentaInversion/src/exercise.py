def calculo_interes(cantidad,interes):
    if cantidad > 0 and interes > 0:
        for i in range(1,13,1):
            cantidad = cantidad + (cantidad * ((interes/12)/100))
        return cantidad
    elif cantidad <= 0 or interes <= 0:
        cantidad = 'Error en los datos'
        return cantidad
         
def main():
    cantidad = int(input("Escribe la cantidad de dinero inicial : "))
    interes = int(input("Escribe el porcentaje de interes anual : "))

    x = calculo_interes(cantidad,interes)
    if x != 'Error en los datos':
        x = "{:.2f}".format(x)
        print(x)
    else: 
        print(x)

if __name__ == '__main__':
    main()
