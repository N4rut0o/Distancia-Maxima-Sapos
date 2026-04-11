"""
Análise de Desempenho — Problema dos Sapos (extra)
Comparação entre a abordagem inicial O(n²) e a otimizada O(n)
"""

import time
from tqdm import tqdm

 
# versão lenta O(n²) — para comparar com a versão optimizada - é a abordagem original antes de identificar o problema de desempenho
def avancar_direita_lento(blocos, inicio):
    posicao = inicio
    while posicao + 1 < len(blocos) and blocos[posicao + 1] >= blocos[posicao]:
        posicao = posicao + 1
    return posicao
 
def avancar_esquerda_lento(blocos, inicio):
    posicao = inicio
    while posicao - 1 >= 0 and blocos[posicao - 1] >= blocos[posicao]:
        posicao = posicao - 1
    return posicao
 
def solucao_lenta(blocos):
    # para cada bloco como partida, avança nas duas direcções
    # problema: recalcula tudo de novo em cada iteração — O(n²)
    maior_distancia = 0
    for i in range(len(blocos)):
        direita  = avancar_direita_lento(blocos, i)
        esquerda = avancar_esquerda_lento(blocos, i)
        distancia = direita - esquerda
        if distancia > maior_distancia:
            maior_distancia = distancia
    return maior_distancia
 
 
# versão rápida O(n) — pré-calcula os arrays esquerda[] e direita[] 
def solucao_rapida(blocos):
    if len(blocos) == 0:
        return 0, 0
    n = len(blocos)
    esquerda = [0] * n
    for i in range(1, n):
        esquerda[i] = esquerda[i - 1] if blocos[i - 1] >= blocos[i] else i
    direita = [0] * n
    direita[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        direita[i] = direita[i + 1] if blocos[i + 1] >= blocos[i] else i
    maior_distancia = 0
    partida = 0
    for i in range(n):
        distancia = direita[i] - esquerda[i]
        if distancia > maior_distancia:
            maior_distancia = distancia
            partida = i
    return maior_distancia, partida

# Comparação de tempo de ambas soluções para 100000 blocos 
TAMANHO_TESTE = 100000
blocos_teste = list(range(TAMANHO_TESTE)) # Lista crescente 


# Teste da versão Rápida O(n)
print("A executar versão Otimizada O(n)...")
inicio = time.perf_counter()
distancia_rapida, partida = solucao_rapida(blocos_teste)
tempo_rapido = time.perf_counter() - inicio
print(f" -> Versão Otimizada O(n) concluída em: {tempo_rapido:.5f} s (Distância: {distancia_rapida})\n")

# Teste da versão Lenta O(n²)
print("A executar versão Original O(n²)...")
inicio = time.perf_counter()

# Usamos a lógica exata do Relatório (Listing 2) para a barra de progresso
maior_distancia_lenta = 0
for i in tqdm(range(len(blocos_teste)), desc="Progresso O(n²)"):
    direita = avancar_direita_lento(blocos_teste, i)
    esquerda = avancar_esquerda_lento(blocos_teste, i)
    distancia = direita - esquerda
    if distancia > maior_distancia_lenta:
        maior_distancia_lenta = distancia

tempo_lento = time.perf_counter() - inicio
print(f"\n -> Versão Original O(n²) concluída em: {tempo_lento:.5f} s (Distância: {maior_distancia_lenta})")