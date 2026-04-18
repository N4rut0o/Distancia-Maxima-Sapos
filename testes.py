"""
Testes do Projeto Individual — Problema dos Sapos
Ficheiro separado para manter o código principal limpo
"""

import time
import unittest
import pandas as pd

from projeto_individual import solucao, solucao_n_sapos, classificar_tempo


class TestProblemaSapos(unittest.TestCase):
    def test_exemplo_1(self):
        self.assertEqual(solucao([2, 6, 8, 5]), (2, 1))

    def test_exemplo_2(self):
        self.assertEqual(solucao([1, 5, 5, 2, 6]), (3, 1))

    def test_lista_vazia(self):
        self.assertEqual(solucao([]), (0, 0))

    def test_um_bloco(self):
        self.assertEqual(solucao([7]), (0, 0))

    def test_todos_iguais(self):
        self.assertEqual(solucao([4, 4, 4, 4]), (3, 0))

    def test_crescente(self):
        self.assertEqual(solucao([1, 2, 3, 4, 5]), (4, 0))

    def test_decrescente(self):
        self.assertEqual(solucao([5, 4, 3, 2, 1]), (4, 4))

    def test_com_tolerancia(self):
        # com tolerância 1, o sapo consegue descer 1 unidade
        self.assertEqual(solucao([5, 4, 3, 2, 1], tolerancia=1), (4, 0))

    def test_n_sapos_base(self):
        distancia, partida, posicoes = solucao_n_sapos([1, 5, 5, 2, 6], 2)
        self.assertEqual(distancia, 3)
        self.assertEqual(partida, 1)
        self.assertEqual(posicoes, [1, 4])

    def test_n_sapos_varios(self):
        distancia, partida, posicoes = solucao_n_sapos([1, 5, 5, 2, 6], 4)
        self.assertEqual(distancia, 3)
        self.assertEqual(partida, 1)
        self.assertEqual(posicoes, [1, 2, 3, 4])

    def test_n_sapos_um(self):
        distancia, partida, posicoes = solucao_n_sapos([2, 6, 8, 5], 1)
        self.assertEqual(distancia, 2)
        self.assertEqual(partida, 1)
        self.assertEqual(posicoes, [1])

    def test_classificar_tempo(self):
        self.assertEqual(classificar_tempo(0.000003), "Rápido")
        self.assertEqual(classificar_tempo(0.0000045), "Normal")
        self.assertEqual(classificar_tempo(0.00001), "Lento")


def demonstracao_resultados():
    testes = [
        {"nome": "Exemplo 1", "blocos": [2, 6, 8, 5], "esperado": 2},
        {"nome": "Exemplo 2", "blocos": [1, 5, 5, 2, 6], "esperado": 3},
        {"nome": "Todos iguais", "blocos": [1, 1, 1, 1], "esperado": 3},
        {"nome": "Decrescente", "blocos": [5, 4, 3, 2, 1], "esperado": 4},
        {"nome": "Crescente", "blocos": [1, 2, 3, 4, 5], "esperado": 4},
    ]

    resultados = []

    for teste in testes:
        inicio = time.perf_counter()
        distancia, partida = solucao(teste["blocos"])
        fim = time.perf_counter()
        tempo_execucao = fim - inicio

        resultados.append({
            "teste": teste["nome"],
            "blocos": str(teste["blocos"]),
            "distancia": distancia,
            "partida": partida,
            "valor_esperado": teste["esperado"],
            "correto": distancia == teste["esperado"],
            "tempo": tempo_execucao,
            "classificacao": classificar_tempo(tempo_execucao),
        })

    df = pd.DataFrame(resultados)
    print("\n--- RESULTADOS DOS TESTES ---")
    print(df)

    print("\n--- TESTE COM 10^5 BLOCOS ---")
    blocos_grandes = list(range(1, 100001))
    inicio = time.perf_counter()
    distancia, partida = solucao(blocos_grandes)
    fim = time.perf_counter()
    print(f"Distância: {distancia} | Partida: {partida} | Tempo: {fim - inicio:.5f}s")


if __name__ == "__main__":
    print("A correr testes automáticos...\n")
    unittest.main(exit=False)

    demonstracao = input("\nQueres ver a tabela de demonstração? (s/n): ").strip().lower()
    if demonstracao == "s":
        demonstracao_resultados()

# pode ser alterado / deveria estar no topo como professor mencionou 
TAMANHO_LISTA = 10 ** 5
 
# lista aleatória em vez de só crescente — mais representativo de casos reais
random.seed(42) # ter a mesma seed faz com que outros possam correr os mesmos testes e obter exatamente os mesmos resultados!
blocos_grandes = [random.randint(1, 100) for _ in range(TAMANHO_LISTA)]
inicio = time.perf_counter()
distancia, _ = solucao(blocos_grandes)
fim = time.perf_counter()
print(f"distância: {distancia} | tempo: {fim - inicio:.5f}s")
