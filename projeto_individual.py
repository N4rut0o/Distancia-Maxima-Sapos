# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:35:05 2026

@author: Filipe
"""
# bloco inicial dado
blocos = [2,6,8,5]

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

print(avancar_direita(blocos, 0))
print(avancar_esquerda(blocos, 3))