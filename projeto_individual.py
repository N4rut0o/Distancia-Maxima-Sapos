# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:35:05 2026

@author: Filipe
"""
# bloco inicial dado
blocos = [3, 5, 7, 2]

# inicio da posicao (tornar isto variável para o utilizador andar esquerda/direita)
posicao = 0

# só avança se existir um bloco à frente e se esse bloco for acessível = (limite)
while posicao + 1 < len(blocos) and blocos[posicao + 1] >= blocos[posicao]:
    posicao = posicao + 1
    print(f"O sapo avançou para a posição {posicao}. (altura {blocos[posicao]})")

print(f"O sapo ficou na posição {posicao}") # só salta para a frente se o próximo bloco for igual ou maior

# while para a esquerda
while posicao -1 >= 0 and blocos[posicao - 1] >= blocos[posicao]:
    posicao = posicao - 1
    print(f"O sapo avançou para a posição {posicao}. (altura {blocos[posicao]})")

print(f"O sapo ficou na posição {posicao}") 