"""
Interface gráfica — Problema dos Sapos
janela Tkinter como alternativa ao menu de terminal - biblioteca referenciada nas referências úteis do enunciado
"""

# Imports
import tkinter as tk
from tkinter import messagebox
from projeto_individual import solucao_n_sapos

def calcular():
    # Obtém o texto escrito na caixa de entrada e remove espaços extras nas pontas
    texto = entrada_blocos.get().strip()
    # Se o campo estiver vazio, interrompe a função
    if not texto: return
    try:
        blocos     = [int(x) for x in texto.split()] # Converte a string de números (ex: "2 6 8") numa lista de inteiros [2, 6, 8]
        tolerancia = int(entrada_tolerancia.get() or 0) # lê o campo tolerância e agora o utilizador pode colocar qualquer valor
        n_sapos    = int(entrada_sapos.get() or 2)      # lê o campo n_sapos e agora o utilizador pode colocar qualquer valor
        distancia, partida, posicoes = solucao_n_sapos(blocos, n_sapos, tolerancia)
        alturas = [blocos[p] for p in posicoes] # alturas de cada bloco onde os sapos ficam (índice → altura)
        resultado_var.set(f"Distância: {distancia} | Partida: bloco {partida}\nPosições: {posicoes}\nAlturas: {alturas}") # Atualiza a variável de texto da interface com o resultado obtido
    except ValueError:
        messagebox.showerror("Erro", "Usa só números inteiros.")

# necessário para evitar que o Python execute o menu de projeto_individual.py ao importá-lo
if __name__ == "__main__":

    # Personalização da Janela Principal
    janela = tk.Tk()
    janela.title("Problema dos Sapos - Base") # Define o título que aparece na barra superior
    janela.geometry("420x360")  # Define o tamanho da janela
    janela.resizable(False, False)

    tk.Label(janela, text="Blocos (separados por espaço):").pack(pady=(15, 2)) # Rótulo (Label) informativo para instruir o utilizador
    entrada_blocos = tk.Entry(janela, width=30) # Caixa de Entrada (Entry) onde o utilizador escreve os números
    entrada_blocos.pack()

    # Tolerância
    tk.Label(janela, text="Tolerância (padrão: 0):").pack(pady=(10, 2))
    entrada_tolerancia = tk.Entry(janela, width=10)
    entrada_tolerancia.insert(0, "0")
    entrada_tolerancia.pack()

    # campo n_sapos
    tk.Label(janela, text="Número de sapos (padrão: 2):").pack(pady=(10, 2))
    entrada_sapos = tk.Entry(janela, width=10)
    entrada_sapos.insert(0, "2")
    entrada_sapos.pack()

    tk.Button(janela, text="Calcular", command=calcular, bg="#4CAF50", fg="white").pack(pady=20) # Botão que executa a função 'calcular' quando é pressionado

    resultado_var = tk.StringVar(value="—") # Variável que atualiza o texto automaticamente
    tk.Label(janela, textvariable=resultado_var, font=("Arial", 11), justify="center").pack()

    janela.mainloop() # Mantém a janela aberta à espera de interações do utilizador