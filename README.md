# Distância Máxima dos Sapos 🐸

Projeto Individual de Laboratórios de Estatística II  
Licenciatura em Estatística Aplicada — 2025/2026  
Autor: Luís Filipe Gonçalves

---

## O Problema

Dois sapos estão no mesmo bloco e discutem. Depois da discussão
querem ficar o mais longe possível um do outro — mas só conseguem
saltar para blocos adjacentes que sejam iguais ou mais altos.

O objetivo é descobrir qual é a maior distância a que os dois
sapos conseguem ficar.

---

## Estrutura do Projeto

| Ficheiro | Descrição |
|---|---|
| `projeto_individual.py` | Código principal — algoritmo, gráficos, menu |
| `testes.py` | Testes com pandas, stress test e robustez |
| `comparacao_desempenho.py` | Comparação visual O(n²) vs O(n) |
| `interface_grafica.py` | Interface gráfica em Tkinter |
| `Relatório.pdf` | Relatório completo do projeto |

---

## O que foi implementado

### Base obrigatória
- [x] Movimento básico dos sapos
- [x] Função `solucao(blocos)`
- [x] Funciona para qualquer lista de blocos
- [x] 5+ testes com tempo de execução

### Extras do enunciado
- [x] Mais de 2 sapos — distribuição uniforme pelo intervalo alcançável
- [x] Deixar descer um pouco — tolerância configurável pelo utilizador
- [x] Interface gráfica — matplotlib com cores automáticas, seta de distância e legenda descritiva

### Extras por iniciativa própria
- [x] Menu interativo com validação de inputs
- [x] Análise estatística com pandas — DataFrame, `.apply()`
- [x] Gráfico comparativo O(n²) vs O(n) com tempos reais
- [x] Barra de progresso com `tqdm` — usada para diagnosticar o problema de desempenho com 10⁵ blocos
- [x] Interface Tkinter — sliders para tolerância e N sapos, exemplos predefinidos

---

## Destaque — Optimização do Algoritmo

A versão inicial demorou **473,9 segundos** para uma lista de 10⁵ blocos.  
Após identificar a redundância de cálculo, o algoritmo foi reescrito com arrays pré-calculados.  
Resultado: **0,018 segundos** — uma melhoria de ~26 000×.

---

## Como correr

```bash
# Menu principal
python projeto_individual.py

# Testes
python testes.py

# Interface gráfica
python interface_grafica.py

# Gráfico comparativo O(n²) vs O(n)
python comparacao_desempenho.py
```

---

## Estado: Concluído — abril 2026
