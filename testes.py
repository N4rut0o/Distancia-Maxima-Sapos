"""
Testes do Projeto Individual — Problema dos Sapos
Ficheiro separado para manter o código principal limpo
"""
 
from projeto_individual import solucao, solucao_n_sapos, mostrar_grafico
 
# bloco inicial dado
blocos = [2,6,8,5] 
distancia, partida = solucao(blocos)
print(f"Distância: {distancia} | Partida: bloco {partida}")

# testes de casos limite para verificar se programa não crasha
distancia, partida = solucao([1])  # um único bloco, ou seja, o sapo não se pode mover
print(f"1 bloco: distância {distancia}") 

distancia, partida = solucao([1, 1]) # dois blocos iguais, conseguem separar-se 1 posição
print(f"2 blocos iguais: distância {distancia}")

distancia, partida = solucao([]) # lista vazia — não deveria crashar 
print(f"lista vazia: distância {distancia}")

# Testes de cores gráficos
mostrar_grafico([2,6,8,5])
mostrar_grafico([1,5,5,2,6])
mostrar_grafico([1])

# Testes de validação
mostrar_grafico([0, 0, 0, 0]) # fix altura_max — antes dava UserWarning no eixo Y
mostrar_grafico([2,6,8,5], n_sapos=0)  # fix n_sapos<=1 — antes dava IndexError
mostrar_grafico([2,6,8,5], tolerancia=1, n_sapos=5)  # testa N sapos com tolerância
distancia, partida = solucao([]) # lista vazia — não deveria crashar 
print(f"lista vazia: distância {distancia}")
distancia, partida = solucao([0, 0, 0, 0]) # testa todos os blocos a zero — valida fix de altura_max
print(f"todos zeros: distância {distancia}") 
distancia, partida, posicoes = solucao_n_sapos([2,6,8,5], n_sapos=0) # testa n_sapos=0 — valida fix do <= 1 em solucao_n_sapos (antes crashava com 0)
print(f"n_sapos=0: posições={posicoes}")