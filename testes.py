"""
Testes do Projeto Individual — Problema dos Sapos
Ficheiro separado para manter o código principal limpo
"""

from projeto_individual import solucao, solucao_n_sapos, mostrar_grafico, classificar_tempo
import time
import pandas as pd
import random


# foi necessário para evitar que o Python execute o menu de projeto_individual.py ao importá-lo
if __name__ == "__main__":

    # testes com valor esperado — 2 blocos dados do enunciado + outros casos
    testes = [
        ([2, 6, 8, 5],    2, 0, "exemplo 1 do enunciado"),
        ([1, 5, 5, 2, 6], 3, 0, "exemplo 2 do enunciado"),
        ([1, 1, 1, 1],    3, 0, "todos os blocos iguais"),
        ([5, 4, 3, 2, 1], 4, 0, "alturas sempre a descer"),      
        ([5, 4, 3, 2, 1], 4, 1, "alturas a descer com tolerância 1"),
        ([1, 2, 3, 4, 5], 4, 0, "alturas sempre a subir"),
        ([1],             0, 0, "um único bloco"),
        ([],              0, 0, "lista vazia"),
    ]

    resultados = []

    # Executa cada teste e compara com o valor esperado
    for blocos, valor_esperado, tolerancia, nome in testes:

        inicio = time.perf_counter() 
        distancia, partida = solucao(blocos, tolerancia)
        fim = time.perf_counter()
        tempo_execucao = fim - inicio  

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
    df_resultados["classificacao"] = df_resultados["tempo"].apply(classificar_tempo)
    print(df_resultados)


#  testes de robustez - casos limite para verificar se programa não crasha
distancia, partida = solucao([1]) 
print(f"1 bloco: distância {distancia}") 

distancia, partida = solucao([1, 1])
print(f"2 blocos iguais: distância {distancia}")

distancia, partida = solucao([])  
print(f"lista vazia: distância {distancia}")

distancia, _ = solucao([0, 0, 0, 0])
print(f"todos zeros: distância {distancia}")

distancia, _, posicoes = solucao_n_sapos([2, 6, 8, 5], n_sapos=0)
print(f"n_sapos=0: posições={posicoes}")


# Testes de cores gráficos
mostrar_grafico([2,6,8,5])
mostrar_grafico([1,5,5,2,6])
mostrar_grafico([1])
mostrar_grafico([0, 0, 0, 0])                          
mostrar_grafico([2, 6, 8, 5], n_sapos=0)              
mostrar_grafico([2, 6, 8, 5], tolerancia=1, n_sapos=5) 


# TAMANHO_LISTA pode ser alterado / deveria estar no topo como professor mencionou 
TAMANHO_LISTA = 10 ** 5
 
# lista aleatória em vez de só crescente — mais representativo de casos reais
random.seed(42) # ter a mesma seed faz com que outros possam correr os mesmos testes e obter exatamente os mesmos resultados!
blocos_grandes = [random.randint(1, 100) for _ in range(TAMANHO_LISTA)]
inicio = time.perf_counter()
distancia, _ = solucao(blocos_grandes)
fim = time.perf_counter()
print(f"distância: {distancia} | tempo: {fim - inicio:.5f}s")