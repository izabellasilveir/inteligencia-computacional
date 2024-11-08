# -*- coding: utf-8 -*-
"""analise_walksat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rQdRRUxW2Y29NZZrPCVNF1YEll8Lt7_A
"""

import random
import matplotlib.pyplot as plt

ALFABETO = 'ABCDEGHIJKLMNOPQRSUVWXYZ'

def seleciona_literais(quantidade, alfabeto=ALFABETO):
    sol = ""
    while len(sol) < quantidade:
        car = random.choice(alfabeto)
        if car not in sol:
            sol+=car
    return sol

# m  - numero de clausulas
# n  - número de símbolos

def gera_clausulas(m,n,fn = 3,  alfa = ALFABETO):
    if n > len(alfa):
        return 'Erro: Número de símbolos maior que o alfabeto'
    expressao = ""
    for  i in range(m):
        literais = seleciona_literais(fn)
        clausula = literais[0]
        for l in literais[1:]:
            modificador = random.choice(["","not"])
            if modificador == "not":
                lit = modificador + f"({l})"
            else:
                lit = f"{l}"
            clausula += " or "  + lit
        clausula = f"({clausula})"
        expressao += clausula + " and "
    return expressao[:-5]

def avalia_satisfabilidade(expressao):
    try:
        return eval(expressao)
    except:
        return False

def probabilidade_satisfacao(m, n, num_iteracoes=100):
    proporcao_satisfatorias = []
    for _ in range(num_iteracoes):
        expressao = gera_clausulas(m, n)
        satisfatoria = avalia_satisfabilidade(expressao)
        if satisfatoria:
            proporcao_satisfatorias.append(1)
        else:
            proporcao_satisfatorias.append(0)
    return sum(proporcao_satisfatorias) / num_iteracoes

def plot_probabilidade_satisfacao(m, n, max_iteracao=1000):
    razoes = [i / 10 for i in range(1, max_iteracao + 1)]
    probabilidades = []
    for razao in razoes:
        probabilidades.append(probabilidade_satisfacao(int(m * razao), n))
    plt.plot(razoes, probabilidades)
    plt.xlabel('Razão m/n')
    plt.ylabel('Probabilidade de Satisfação')
    plt.title('Probabilidade de uma Expressão em 3FN ser Satisfeita')
    plt.show()

plot_probabilidade_satisfacao(10, 5)