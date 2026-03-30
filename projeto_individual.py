# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:35:05 2026

@author: Filipe
"""


#Funções
def avancar_direita(blocos, inicio):
    posicao = inicio # copia o valor de inicio para posicao
    # só avança se existir um bloco à frente e se esse bloco for acessível
    while posicao + 1 < len(blocos) and blocos[posicao + 1] >= blocos[posicao]:
        posicao = posicao + 1
    return posicao


def avancar_esquerda(blocos, inicio):
    posicao = inicio 
    # while para a esquerda
    while posicao -1 >= 0 and blocos[posicao - 1] >= blocos[posicao]:
        posicao = posicao - 1
    return posicao


def solucao(blocos):
    maior_distancia = 0  # guarda a maior distância encontrada, começa em 0 porque ainda não testámos nada
    
    for i in range(len(blocos)):  # testa cada bloco como ponto de partida e avança para ambos os lados
        direita = avancar_direita(blocos, i)
        esquerda = avancar_esquerda(blocos, i)
        distancia = direita - esquerda  # diferença entre as posições finais dos dois sapos
        
        if distancia > maior_distancia:  # se esta distância for maior que a melhor até agora, actualiza
            maior_distancia = distancia
    
    return maior_distancia


#Testes

# bloco inicial dado
blocos = [2,6,8,5] 
print(solucao(blocos))

# bloco de 5 testes criado (2 do enunciado, 3 aleatórios)
testes = [
        ([2,6,8,5], 2),
        ([1,5,5,2,6], 3),
        ([1,1,1,1], 3),
        ([5,4,3,2,1], 4),
        ([1,2,3,4,5], 4),
        ]

# Executa cada teste e compara com o valor esperado
for blocos, valor_esperado in testes:

    distância = solucao(blocos) # distância máxima encontrada
    
    print("Blocos:", blocos)
    print("Distância:", distância)
    print("Valor esperado:", valor_esperado)