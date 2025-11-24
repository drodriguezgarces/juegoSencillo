from random import choice

LISTA_PALABRAS = ["perro", "tomate", "patata"] 

palabra_aleatoria = choice(LISTA_PALABRAS)

letras_adivinadas = []
vidas = 5

# creamos un array con tantos _ como letras tenga la palabra
panel = ["_"] * len(palabra_aleatoria)

while vidas != 0:
    print(f"Te quedan {vidas} vidas")

    # convertimos el array a string
    print("".join(panel))

    print("Letras adivinadas: ")
    print(", ".join(letras_adivinadas))

    # pedimos la palabra o la letra
    opcion = input("Adivina una palabra o la letra: ")
    
    # si se escribe una letra o una palabra
    if len(opcion) == 1:
        if opcion in palabra_aleatoria:
            print("La letra esta en la palabra")
            letras_adivinadas.append(opcion)

            # con la i miramos la posicion y con la c las letras
            for i, c in enumerate(palabra_aleatoria):
                # si la letra coincide con una de la palabra la actualiza en el panel
                if c == opcion:
                    panel[i] = opcion

            # si el panel es igual a la palabra ganamos
            if "".join(panel) == palabra_aleatoria:
                break
        else:
            # si fallamos perdemos una vida
            print("La letra no está en la palabra")
            vidas -= 1
    else:
        # si la palabra es la correcta ganamos
        if opcion == palabra_aleatoria:
            print("Has acertado la palabra")
            break
        else:
            # si la palabra no es correcta perdemos una vida
            print("No has acertado la palabra")
            vidas -= 1

# en caso que lleguemos a 0 vidas significa que hemos perdido
if vidas == 0:
    print(f"No has acertado, la palabra era {palabra_aleatoria}")
else:
    print(f"Enhorabuena, la palabra era {palabra_aleatoria}")