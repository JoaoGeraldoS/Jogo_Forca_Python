import random
import os

personagns = ['HomemAranha', 'SuperHomem', 'Batman']

aleatorio = random.choice(personagns)
print(aleatorio)

nova_entrada = ''
chances = 12

while chances > 0:
    erros = 0
    for letra in aleatorio:

        if letra in nova_entrada:
            print(letra)
        else:
            print('_')
            erros += 1


    entrada = input('Digite uma letra: ')

    nova_entrada += entrada

    if erros == 0:
        print('Você acertou!')
        print(f'A palavra era {nova_entrada}')
        break

    if nova_entrada:
        os.system('cls')
    
    if entrada not in aleatorio:
        chances -= 1
        print('Voce perdeu')

        if chances == 0:
            print('Perdeu')

