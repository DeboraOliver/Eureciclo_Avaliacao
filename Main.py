#Desafio de programação inicial - EURECICLO

import random

def inicio():
    volume_galao = 5

    #Os volumes de cada garrafa
    g1 = 1
    g2 = 3
    g3 = 4.5
    g4 = 1.5

    lista_de_garrafas = [g1,g2,g3,g4]

    # O número de garrafas
    n_garrafas = len(lista_de_garrafas)

    n = 1

    while n < (n_garrafas + 1):
        lista_ramdomizada = random.sample(lista_de_garrafas, n)
        if (sum(lista_ramdomizada)== volume_galao) or (sum (lista_ramdomizada) == volume_galao + 0.5):
            volume_sobra = sum(lista_ramdomizada) - volume_galao
            print("Com {} garrafas {} sobra {}L".format(len(lista_ramdomizada), lista_ramdomizada, volume_sobra))
            break
        elif n==n_garrafas:
            lista_ramdomizada = random.sample(lista_de_garrafas, n-2)
            if (sum(lista_ramdomizada)== volume_galao) or (sum (lista_ramdomizada) == volume_galao + 0.5):
                volume_sobra = sum (lista_ramdomizada) - volume_galao
                print ("Com {} garrafas {} sobra {}L".format (len (lista_ramdomizada), lista_ramdomizada, volume_sobra))
                break
            n -= 1
        n+=1

if __name__ == '__main__':
    inicio()