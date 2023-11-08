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

def materialesNecesarios(resistencia):
    if resistencia >= 3500:
        cemento = 420
        arena = 0.67
        grava = 0.67
        agua = 220
    elif resistencia >= 3000:
        cemento = 350
        arena = 0.56
        grava = 0.84
        agua = 180
    elif resistencia >= 2500:
        cemento = 300
        arena = 0.48
        grava = 0.96
        agua = 170
    elif resistencia >= 2000:
        cemento = 260
        arena = 0.63
        grava = 0.84
        agua = 170
    else:
        cemento = 210
        arena = 0.5
        grava = 1.0
        agua = 160
    return cemento, arena, grava, agua


def totalMaterialesNecesarios(cemento, arena, grava, agua, volumen):
    total_cemento = cemento * volumen
    total_arena = arena * volumen
    total_grava = grava * volumen
    total_agua = agua * volumen
    return total_cemento, total_arena, total_grava, total_agua

def presentarCliente(cliente, total_cemento, total_arena, total_grava, total_agua):
    with open('cliente.csv', mode='w') as archivo:
        archivo.write(f'Cliente: {cliente}\n')
        archivo.write(f'---- Materiales necesarios ----\n')
        archivo.write(f'Cemento (kg): {round(total_cemento, 2)}\n')
        archivo.write(f'Arena (mt3): {round(total_arena, 2)}\n')
        archivo.write(f'Grava (mt3): {round(total_grava, 2)}\n')
        archivo.write(f'Agua (lts.): {round(total_agua, 2)}\n')
    return archivo


def main():
    #Calculo volumen
    volumen = calculoVolumen()
    print(f'El volumen de la superficie es de {volumen} mts3')
    
    #Resistencia y materiales necesarios
    resistencia = float(input('Resistencia necesaria de la superficie (En PSI o lb/cm2): '))
    cemento, arena, grava, agua = materialesNecesarios(resistencia)

    total_cemento, total_arena, total_grava, total_agua = totalMaterialesNecesarios(cemento, arena, grava, agua, volumen)

    #Creacion archivo csv
    cliente = input('Ingrese el nombre del cliente: ')
    presentarCliente(cliente, total_cemento, total_arena, total_grava, total_agua)

main()


