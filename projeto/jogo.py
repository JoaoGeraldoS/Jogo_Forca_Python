
import os
import random
from arquivos import personagens
import time

aleatorio = random.choice(personagens)

nova_entrada = ''
chances = 10

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = "{:02d}".format(s)
        print('Aguarde..', min_sec_format, end="\r")
        if min_sec_format == 1:
            break
        time.sleep(1)
        num_of_secs -= 1

countdown(10)

while chances > 0:
    erros = 0
    for letra in aleatorio:

        if letra in nova_entrada:
            print(f'{letra}', end=' ')
        else:
            print('_', end=' ')
            erros += 1

    entrada = input('\n\nDigite uma letra: ')

    nova_entrada += entrada

    if erros == 0:
        print('Você acertou!')
        print(f'A palavra era {aleatorio}')
        break

    if nova_entrada:
        os.system('cls')
    
    if entrada not in aleatorio:
        chances -= 1
        print('Nao existe essa letra ')

        if chances == 0:
            print('Perdeu')

    