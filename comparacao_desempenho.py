"""
Análise de Desempenho — Problema dos Sapos (extra)
Comparação entre a abordagem inicial O(n²) e a otimizada O(n)
"""

# Imports
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

# Funções

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

# Esta função corre os testes e gera o gráfico
def executar_comparacao():
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


    # Gráfico de Barras — O(n²) vs O(n) para 10⁵ blocos 
    tamanhos_milhares = [0, TAMANHO_TESTE // 1000] # Converter X para milhares para o gráfico ficar mais limpo (0 a 100)
    y_lento = [0, tempo_lento]
    y_rapido = [0, tempo_rapido]

    # Configuração do estilo visual
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(10, 6))

    # Desenhar Linha O(n²) - Vermelho escuro, contínuo, com marcador
    ax.plot(tamanhos_milhares, y_lento,
        marker="o", markersize=8, color="darkred", linewidth=2.5,
        linestyle="-", label="Abordagem Inicial $O(n^2)$")

    # Desenhar Linha O(n) - Verde escuro, tracejado, com marcador
    ax.plot(tamanhos_milhares, y_rapido,
        marker="o", markersize=8, color="darkgreen", linewidth=2.5,
        linestyle="--", label="Versão Otimizada $O(n)$")

    # Anotar os pontos finais com os tempos exatos medidos
    # O(n²) - Texto abaixo e à direita do ponto
    ax.annotate(f"{tempo_lento:.1f} s",
            xy=(tamanhos_milhares[-1], y_lento[-1]),
            xytext=(-15, -25), textcoords="offset points",
            color="darkred", fontsize=12, fontweight="bold", ha='right')

    # O(n) - Texto acima e à direita do ponto
    ax.annotate(f"{tempo_rapido:.3f} s",
            xy=(tamanhos_milhares[-1], y_rapido[-1]),
            xytext=(-15, 10), textcoords="offset points",
            color="darkgreen", fontsize=12, fontweight="bold", ha='right')

    # Títulos e Rótulos (Mantendo o texto original, ajustando contexto)
    ax.set_title(f"Impacto da Otimização: Comparação de Desempenho\n(Dados reais medidos para {TAMANHO_TESTE} blocos)",
             fontsize=14, pad=15)
    ax.set_xlabel("Tamanho da Lista (N) em milhares de blocos", fontsize=12)
    ax.set_ylabel("Tempo de execução (segundos)", fontsize=12)

    # Configurar o eixo X para mostrar apenas 0 e o ponto final (100k)
    ax.set_xticks(tamanhos_milhares)
    # Garantir que o eixo Y começa em 0
    ax.set_ylim(bottom=-1) 

    # Legenda e Grelha
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.4, linestyle="--")

    # Ajuste de layout
    plt.tight_layout()

    # Mostrar gráfico
    plt.show()