# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:35:05 2026

@author: Filipe
"""

# Imports
import time
import pandas as pd
import matplotlib.pyplot as plt


# Funções
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
    partida = 0 # variável criada para ficarmos com o ponto de partida de cada sapo
    for i in range(len(blocos)):  # testa cada bloco como ponto de partida e avança para ambos os lados
        direita = avancar_direita(blocos, i)
        esquerda = avancar_esquerda(blocos, i)
        distancia = direita - esquerda  # diferença entre as posições finais dos dois sapos
        
        if distancia > maior_distancia:  # se esta distância for maior que a melhor até agora, actualiza
            maior_distancia = distancia
            partida = i # guarda o bloco de partida correspondente
    
    return maior_distancia, partida

def classificar_tempo(tempo):
    if tempo < 0.000004:
        return "Rápido"
    elif tempo < 0.000005:
        return "Normal"
    else:
        return "Lento"

# Testes

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

# Lista
resultados = []  # lista para guardar os resultados de cada teste

# Executa cada teste e compara com o valor esperado
for blocos, valor_esperado in testes:
    
    inicio = time.perf_counter() # utilizar o time.perf_counter para o início da contagem
    distancia, partida = solucao(blocos) # distância máxima encontrada / colacada entre inicio e fim para ser cronometrada
    fim = time.perf_counter() # mesma lógica do inicio mas para o termino da contagem 
    tempo_execucao = fim - inicio  # tempo total de execução
    
    print(f"Blocos: {blocos}")
    print(f"Distância: {distancia}")
    print(f"Valor esperado: {valor_esperado}")
    print(f"tempo: {tempo_execucao:.5f}s")
    
    # guarda os resultados do teste atual
    resultados.append({
        "blocos"        : str(blocos),
        "distancia"     : distancia,
        "valor_esperado": valor_esperado,
        "correto"       : distancia == valor_esperado,
        "tempo"         : tempo_execucao
    })
    
    # Gráfico com sapos coloridos por posição
    esquerda = avancar_esquerda(blocos, partida)
    direita  = avancar_direita(blocos, partida)

    # cores para identificar visualmente as posições do sapo no gráfico
    cores = ["gray"] * len(blocos)
    cores[esquerda] = "green"   
    cores[partida]  = "blue"    
    cores[direita]  = "red"     

    pd.Series(blocos).plot(kind="bar", color=cores)
    plt.title(f"Blocos: {blocos} | Distância: {distancia}")
    plt.xlabel("Posição")
    plt.ylabel("Altura")
    plt.show()

# Análise dos resultados com pandas
df_resultados = pd.DataFrame(resultados)
df_resultados["Tempo de Execução"] = df_resultados["tempo"].apply(classificar_tempo)
print(df_resultados)