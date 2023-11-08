def seleccionUnidadMedida():
    print('Seleccione la unidad de medida con la que desea trabajar.')
    print('1 - Metros')
    print('2 - Pies')
    print('3 - Centimetros')
    opcion = int(input('Ingrese la opción: '))

    if opcion == 1:
        return 'metros'
    elif opcion == 2:
        return 'pies'
    else:
        return 'centimetros'
    

def conversoraMetros(dimension, unidad):
    if unidad == 'metros':
        return dimension
    elif unidad == 'pies':
        return dimension * 0.3048
    elif unidad == 'centimetros':
        return dimension * 0.01
     

def calculoVolumen():
    unidad = seleccionUnidadMedida()
    largo = float(input(f'Ingrese el largo de la superficie en {unidad}: '))
    ancho = float(input(f'Ingrese el ancho de la superficie en {unidad}: '))
    espesor = float(input(f'Ingrese el espesor de la superficie en {unidad}: '))

    # Se convierten las dimensiones a metros
    largo = conversoraMetros(largo, unidad)
    ancho = conversoraMetros(ancho, unidad)
    espesor = conversoraMetros(espesor, unidad)

    volumen = largo * ancho * espesor
    return volumen


def main():
    volumen = calculoVolumen()
    print(f'El volumen de la superficie es de {volumen} mts3')

main()


