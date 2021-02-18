persona = {}


def agregar(nombre, edad):
    persona[nombre] = edad


def main():

    limite = 2

    for i in range(limite):
        nombre = input('Escribir un nombre: ')
        edad = int(input('Escribir la edad: '))

        agregar(nombre, edad)

    for nombre, edad in persona.items():
        print(nombre + ' tiene ' + str(edad) + ' anios')


if __name__ == '__main__':
    main()
