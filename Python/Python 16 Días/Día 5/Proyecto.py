from random import choice

palabras = ['panadero', 'mesa', 'libro', 'programacion']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_termiando = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una Letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has Elegido una letra correcta.")
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))


def checar_letras(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("YA HAS INTENTADO ESA LETRA. INGRESA OTRA DIFERENTE.")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print("Te has quedado sin vidas.")
    print("La palabra oculta era: " + palabra)
    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades! Has ganado!")
    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_termiando:
    print('*' * 20)
    mostrar_nuevo_tablero(palabra)
    print(" ")
    print('Letras Incorrectas: ' + '-'.join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print('*' * 20)
    letra = pedir_letra()
    intentos, terminado, aciertos = checar_letras(letra, palabra, intentos, aciertos)
    juego_termiando = terminado
