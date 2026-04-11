"""
Interface gráfica — Problema dos Sapos
janela Tkinter como alternativa ao menu de terminal - biblioteca referenciada nas referências úteis do enunciado
"""

# Imports
import tkinter as tk
from tkinter import messagebox
from projeto_individual import solucao_n_sapos

def calcular():
    # Obtém o texto digitado na caixa de entrada e remove espaços extras nas pontas
    texto = entrada_blocos.get().strip()
    # Se o campo estiver vazio, interrompe a função
    if not texto: return
    try:
        blocos = [int(x) for x in texto.split()] # Converte a string de números (ex: "2 6 8") numa lista de inteiros [2, 6, 8]
        # Usa valores padrão (2 sapos, 0 tolerância) para o básico
        distancia, partida, posicoes = solucao_n_sapos(blocos, 2, 0)
        resultado_var.set(f"Distância máxima: {distancia}\nPartida: bloco {partida}") # Atualiza a variável de texto da interface com o resultado obtido
    except ValueError:
        messagebox.showerror("Erro", "Usa só números inteiros.")

# Personalização da Janela Principal
janela = tk.Tk()
janela.title("Problema dos Sapos - Base") # Define o título que aparece na barra superior
janela.geometry("400x300") # Define o tamanho da janela

tk.Label(janela, text="Blocos (espaçados):").pack(pady=10) # Rótulo (Label) informativo para instruir o utilizador
entrada_blocos = tk.Entry(janela, width=30) # Caixa de Entrada (Entry) onde o utilizador escreve os números
entrada_blocos.pack()

tk.Button(janela, text="Calcular", command=calcular, bg="#4CAF50", fg="white").pack(pady=20) # Botão que executa a função 'calcular' quando é pressionado

resultado_var = tk.StringVar(value="—") # Variável que atualiza o texto automaticamente
tk.Label(janela, textvariable=resultado_var, font=("Arial", 11)).pack()

janela.mainloop() # Mantém a janela aberta e à espera de interações do utilizador (cliques, teclado)