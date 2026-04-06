"""
Projeto Individual — Problema dos Sapos
Laboratórios de Estatística II — Licenciatura em Estatística Aplicada
Ano Letivo 2025/2026
Autor: Luís Filipe Gonçalves
"""

# Imports
import time
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")


# Funções
def avancar_direita(blocos,inicio,tolerancia=0):  # tolerancia permite descer até X unidades (utilizador escolhe)
    posicao = inicio # copia o valor de inicio para posicao
    # só avança se existir um bloco à frente e se esse bloco for acessível
    while posicao + 1 < len(blocos) and blocos[posicao + 1] >= blocos[posicao] - tolerancia:
        posicao = posicao + 1
    return posicao


def avancar_esquerda(blocos,inicio,tolerancia=0):
    posicao = inicio 
    # while para a esquerda
    while posicao - 1 >= 0 and blocos[posicao - 1] >= blocos[posicao] - tolerancia:
        posicao = posicao - 1
    return posicao

# tolerancia = 0 implementada como parâmetro e não variável global para evitar problemas de scope
def solucao(blocos,tolerancia=0):
    
    # protecção para lista vazia — retorna 0 em vez de crashar
    if len(blocos) == 0:
        return 0, 0
    
    n = len(blocos) # guardar numa variável o tamanho para depois percorrer no ciclo
    
    # para cada bloco, guarda até onde o sapo consegue ir para a esquerda
    esquerda = [0] * n
    esquerda[0] = 0
    for i in range(1, n):
        if blocos[i - 1] >= blocos[i] - tolerancia:
            esquerda[i] = esquerda[i - 1]
        else:
            esquerda[i] = i
    
    # para cada bloco, guarda até onde o sapo consegue ir para a direita
    direita = [0] * n
    direita[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if blocos[i + 1] >= blocos[i] - tolerancia:
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

def solucao_n_sapos(blocos,n_sapos,tolerancia=0):
    
    # obtém o bloco de partida e o intervalo
    distancia, partida = solucao(blocos, tolerancia)
    pos_esq = avancar_esquerda(blocos, partida, tolerancia)
    pos_dir = avancar_direita(blocos, partida, tolerancia)
    
    # a distância entre um sapo e ele próprio é sempre 0 e evitar crash se utilizador colocar 1
    if n_sapos == 1:
        return distancia, partida, [partida]
    
    # calcula as posições dos N sapos de forma a ficarem igualmente espaçados no intervalo, utilizando o round
    posicoes = []
    for num_sapo in range(n_sapos): # num_sapos em vez de apenas um "n" porque já uso n em solucao() 
        p = round(pos_esq + num_sapo * (pos_dir - pos_esq) / (n_sapos - 1)) # p é variável temporária que fica com a posição de cada sapo
        posicoes.append(p)
    
    return distancia, partida, posicoes

def classificar_tempo(tempo):
    if tempo < 0.000004:
        return "Rápido"
    elif tempo < 0.000005:
        return "Normal"
    else:
        return "Lento"
    
# Função para mostrar os sapos coloridos por posição - com objetivo de ser reutilizada ao implementar menu / n_sapos = 2 porque é o utilizado por defeito
def mostrar_grafico(blocos,tolerancia=0,n_sapos=2):
     
    if len(blocos) == 0:
        print("Não é possível mostrar gráfico para uma lista vazia.")
        return
    
    # obtém posições consoante o número de sapos
    if n_sapos == 2:
        distancia, partida = solucao(blocos, tolerancia)
        esquerda = avancar_esquerda(blocos, partida, tolerancia)
        direita = avancar_direita(blocos, partida, tolerancia)
        posicoes = [esquerda, direita]
    else:
        distancia, partida, posicoes = solucao_n_sapos(blocos, n_sapos, tolerancia)
    
    # gera uma cor diferente para cada sapo
    # sapo 1 sempre verde, sapo último sempre vermelho, meio gerado automaticamente
    def gerar_cores_sapos(n):
        if n == 1:
            return ["green"]
        if n == 2:
            return ["green", "red"]
        import matplotlib.cm as cm
        mapa = cm.get_cmap("tab10", n)
        cores_geradas = ["green"]
        for i in range(1, n - 1):
            r, g, b, _ = mapa(i)
            cores_geradas.append(f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}")
        cores_geradas.append("red")
        return cores_geradas
    
    cores_sapos = gerar_cores_sapos(len(posicoes))
    
    # cores base de todas as barras
    cores = ["lightgray"] * len(blocos)
    cores[partida] = "blue"
    
    # contar quantas vezes cada posição aparece, adaptada para quando tiver N sapos
    contagem = {}
    for pos in posicoes:
        contagem[pos] = contagem.get(pos, 0) + 1
    
    # atribuir cor normal ou cor de sobreposição
    for idx, pos in enumerate(posicoes):
        if pos == partida or contagem[pos] > 1:
            cores[pos] = "gold"  # quando sapos ficam no mesmo bloco / sapo fica no mesmo bloco que partida
        else:
            cores[pos] = cores_sapos[idx]
    
    plt.figure(figsize=(10, 5))
    ax = pd.Series(blocos).plot(kind="bar", color=cores, rot=0)
    
    # valor dentro de cada barra — preto em cinzentas e gold, branco nas restantes
    for i, v in enumerate(blocos):
        cor_texto = "black" if cores[i] in ["lightgray", "gold"] else "white"
        ax.text(i, v / 2, str(v), ha="center", va="center",
                color=cor_texto, fontsize=9, fontweight="bold")
    
    # seta de distância entre sapo mais à esquerda e mais à direita
    if posicoes[0] != posicoes[-1]:
        y_seta = -max(blocos) * 0.12
        ax.annotate("",
            xy=(posicoes[-1], y_seta),
            xytext=(posicoes[0], y_seta),
            arrowprops=dict(arrowstyle="<->", color="black", lw=1.5))
        ax.text((posicoes[0] + posicoes[-1]) / 2, y_seta - max(blocos) * 0.08,
                f"distância = {distancia}",
                ha="center", fontsize=9, fontweight="bold")
        ax.set_ylim(-max(blocos) * 0.28, max(blocos) * 1.15)
    else:
        ax.set_ylim(0, max(blocos) * 1.15)
    
    # título com partida, tolerância e nº sapos
    tol_str = f" | Tolerância: {tolerancia}" if tolerancia > 0 else ""
    ax.set_title(f"Problema dos Sapos | Partida: bloco {partida} | Distância: {distancia} | {n_sapos} sapos{tol_str}")
    ax.set_xlabel("Posição do bloco")
    ax.set_ylabel("Altura do bloco")
    
    # cores para identificar visualmente a posição de cada sapo, o bloco de partida e posições coincidentes
    legendas = []
    for idx, pos in enumerate(posicoes):
        if pos == partida or contagem[pos] > 1:
            legendas.append(plt.Rectangle((0,0),1,1, color="gold",
                label=f"Sapo {idx+1} — bloco {pos} (coincide com partida)"))
        else:
            legendas.append(plt.Rectangle((0,0),1,1, color=cores_sapos[idx],
                label=f"Sapo {idx+1} — bloco {pos}"))
    
    legendas.append(plt.Rectangle((0,0),1,1, color="blue",
        label=f"Partida — bloco {partida}"))
    
    plt.legend(handles=legendas, loc="upper right")
    plt.tight_layout()
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
    resultados = []  
    
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
    print("\n")
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
        print("  4) Tolerância (saltos configuráveis) ")        
        print("  5) Adicionar Sapos ")   
        print("  0) Sair                             ")
        print("\n" )

        escolha = input("Opção: ").strip()

        if escolha == "1":
            blocos = ler_blocos()
            distancia, partida = solucao(blocos)
            print(f"\nDistância: {distancia} | Partida: bloco {partida}")
            print("\n")   

        elif escolha == "2":
            correr_testes()

        elif escolha == "3":
            blocos = ler_blocos()
            mostrar_grafico(blocos)
            print("\n")  
            
        elif escolha == "4":
            blocos = ler_blocos()
            tolerancia = int(input("Tolerância (0 = regras originais): "))
            distancia, partida = solucao(blocos, tolerancia)
            print(f"\nCom tolerância {tolerancia}:")
            print(f"Distância: {distancia} | Partida: bloco {partida}")  
            mostrar_grafico(blocos, tolerancia)
            
        elif escolha == "5":
            blocos = ler_blocos()
            n_sapos = int(input("Quantos sapos? (mínimo 2): "))
            tolerancia = int(input("Tolerância (0 = regras originais): "))
            distancia, partida, posicoes = solucao_n_sapos(blocos, n_sapos, tolerancia)
            print(f"\n{n_sapos} sapos | Distância: {distancia} | Posições: {posicoes}")    
            mostrar_grafico(blocos, tolerancia, n_sapos)

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

# Testes de cores gráficos
mostrar_grafico([2,6,8,5])
mostrar_grafico([1,5,5,2,6])
mostrar_grafico([1])

# Chamar função Menu para utilizador usar
menu()

