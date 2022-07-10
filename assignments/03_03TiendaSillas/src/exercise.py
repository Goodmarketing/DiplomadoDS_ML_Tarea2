def total_antes_descuento(tipo_silla,cantidad):
    if tipo_silla == 'B':
        total_antes_descuento = float(cantidad * 700)
    elif tipo_silla == 'E':
        total_antes_descuento = float(cantidad * 900)
    elif tipo_silla == 'L':
        total_antes_descuento = float(cantidad * 1500)
    return total_antes_descuento

def calcula_descuento(total_inicial,tipo_cliente):
    if tipo_cliente == 'F':
        descuento = total_inicial * .2
    elif tipo_cliente == 'N':
        if 10000 <= total_inicial <=20000:
            descuento = total_inicial * .1
        elif total_inicial > 20000:
            descuento = total_inicial * .15
        else:
            descuento = 0.0
    return descuento
    
def main():
    silla = input('Tipo silla: ')
    cliente = input('Tipo cliente: ')
    cantidad = int(input('Cantidad de sillas: '))
    subtotal = total_antes_descuento(silla,cantidad)
    descuento = calcula_descuento(subtotal,cliente)
    total = subtotal - descuento
    print(f"Total sin dcto.  ${subtotal:>7}")
    print(f"Descuento        ${descuento:>7}")
    print(f"Total a pagar    ${total:>7}")

if __name__ == '__main__':
    main()
