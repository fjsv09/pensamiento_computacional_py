def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0, f'{palabra} no se permiten str vacios'

            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print('sssssssss', e)

    return primeras_letras


lista = ['aaaa', '', 2, '1111', 0.3]
print(primera_letra(lista))
