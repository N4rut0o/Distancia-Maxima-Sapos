# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:35:05 2026

@author: Filipe
"""

# Imports
import time
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm # barra de progresso para visualizar teste da questão "10⁵ blocos?"


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
    
    # protecção para lista vazia — retorna 0 em vez de crashar
    if len(blocos) == 0:
        return 0, 0
    
    n = len(blocos) # guardar numa variável o tamanho para depois percorrer no ciclo
    
    # para cada bloco, guarda até onde o sapo consegue ir para a esquerda
    esquerda = [0] * n
    esquerda[0] = 0
    for i in range(1, n):
        if blocos[i - 1] >= blocos[i]:
            esquerda[i] = esquerda[i - 1]
        else:
            esquerda[i] = i
    
    # para cada bloco, guarda até onde o sapo consegue ir para a direita
    direita = [0] * n
    direita[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if blocos[i + 1] >= blocos[i]:
            direita[i] = direita[i + 1]
        else:
            direita[i] = i
    
    maior_distancia = 0  # guarda a maior distância encontrada, começa em 0 porque ainda não testámos nada
    partida = 0 # variável criada para ficarmos com o ponto de partida de cada sapo
    
    # percorre todos os blocos e encontra qual dá a maior distância
    for i in range(n):  
        distancia = direita[i] - esquerda[i]  # diferença entre as posições finais dos dois sapos
        
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
    
# Função para mostrar os sapos coloridos por posição - com objetivode ser reutilizada ao implementar menu
def mostrar_grafico(blocos):
    distancia, partida = solucao(blocos)
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
    
def ler_blocos():
    resposta = input("Introduza os blocos: ")
    blocos = list(map(int, resposta.split()))
    return blocos 

# código movido para uma função para ser utilizado através do Menu
def correr_testes():
    
    # bloco de 5 testes criado (2 do enunciado, 3 aleatórios)
    testes = [
            ([2,6,8,5], 2),
            ([1,5,5,2,6], 3),
            ([1,1,1,1], 3),
            ([5,4,3,2,1], 4),
            ([1,2,3,4,5], 4),
            ]

    # Lista para guardar os resultados de cada teste
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
        
        
    # Análise dos resultados com pandas
    df_resultados = pd.DataFrame(resultados)
    df_resultados["Tempo de Execução"] = df_resultados["tempo"].apply(classificar_tempo)
    print(df_resultados)
    
    # teste com lista grande para responder à questão do enunciado "o que aconteceria com uma lista de 10⁵ blocos?"
    print("\\n")
    blocos_grandes = list(range(1, 100001))
    inicio = time.perf_counter()
    distancia, partida = solucao(blocos_grandes)
    fim = time.perf_counter()
    print(f"10⁵ blocos | Distância: {distancia} | Tempo: {fim - inicio:.5f}s")

    
# Menu
def menu():
    
    while True:
        print("        -- PROBLEMA DOS SAPOS --          ")
        print("             --- Base ---             ")
        print("  1) Inserir blocos                   ")
        print("  2) Correr testes                    ")
        print("  3) Mostrar gráfico                  ")
        print("  0) Sair                             ")
        print("\n" )

        escolha = input("Opção: ").strip()

        if escolha == "1":
            blocos = ler_blocos()
            distancia, partida = solucao(blocos)
            print(f"\nDistância: {distancia} | Partida: bloco {partida}")
            print("\n" )   

        elif escolha == "2":
            correr_testes()

        elif escolha == "3":
            blocos = ler_blocos()
            mostrar_grafico(blocos)
            print("\n" )   

        elif escolha == "0":
            print("Até logo! 🐸")
            break

        else:
            print("Opção inválida.")
            

# Testes

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
      
# Chamar função Menu para utilizador usar
menu()

