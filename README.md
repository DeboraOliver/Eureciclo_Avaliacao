#Desafio de programação inicial

Dado um conjunto de garrafas d'água, com volumes de água diferentes entre si, e um galão de água. Crie um algoritmo, na linguagem que achar melhor, para escolher as garrafas a serem utilizadas para encher o galão, de acordo:

i.  O galão deve ser completamente preenchido com o volume das garrafas;
ii. Procure esvaziar totalmente as garrafas escolhidas;
iii.Quando não for possível esvaziar todas garrafas escolhidas, deixe a menor sobra possível;
iv. utilize o menor número de garrafas possível;

--------------------------------------------------

#SOLUÇÃO

##Bibliotecas Utilizadas

import random

## Declaração das variáveis 

 volume_galao = 5

 Os volumes de cada garrafa:
    g1 = 1
    g2 = 3
    g3 = 4.5
    g4 = 1.5

    lista_de_garrafas = [g1,g2,g3,g4]

 O número de garrafas é calculado tendo em vista o tamanho do vetor lista_garrafas:
    n_garrafas = len(lista_de_garrafas)

## Encontrando o menor nº de garrafas

Usarei um laço para testar o número de garrafas que satisfaz a necessidade:
n = 1

    while n < (n_garrafas + 1):

Criamos pequenas listas derivadas da lista principal (lista_de_garrafas):

        lista_ramdomizada = random.sample(lista_de_garrafas, n)
Se, a soma dos volumes das garrafas forem iguais ao volume total do galão, saímos do laço:
                if (sum(lista_ramdomizada)== volume_galao) or (sum(lista_ramdomizada) == volume_galao + 0.5):
            volume_sobra = sum(lista_ramdomizada) - volume_galao
            print("Com {} garrafas {} sobra {}L".format(len(lista_ramdomizada), lista_ramdomizada, volume_sobra))
            break
 	
Caso nenhuma das condições anteriores não seja satisfeita:
	n+=1

No entanto, quando a condição anterior não for satisfeita e já atingirmos o n==4 (total de garrafas), criamos uma nova lista randomizada com um número menor de garrafas:

        elif n==n_garrafas:
            lista_ramdomizada = random.sample(lista_de_garrafas, n-2)

Desta forma, voltamos a testar acombinação de um número menor de garrafas!
 
        if (sum(lista_ramdomizada)== volume_galao) or (sum (lista_ramdomizada) == volume_galao + 0.5):
            volume_sobra = sum(lista_ramdomizada) - volume_galao
            print("Com {} garrafas {} sobra {}L".format(len(lista_ramdomizada), lista_ramdomizada, volume_sobra))
            break

Se mesmo assim não encontrarmos o menor número de garrafas que satisfaçam os requisitos, nosso n é decrescido:
            n-=1
         