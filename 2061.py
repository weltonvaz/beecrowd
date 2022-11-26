# -*- coding: utf-8 -*-
'''
Sua tarefa é descobrir com quantas abas que o navegador de Péricles ficou, sabendo o número inicial de abas e a sequência de ações de Péricles. As
ações podem ser fechou (quando Péricles fechou uma aba) ou clicou (quando Péricles clicou em uma propaganda).

Entrada
A entrada é iniciada por uma linha contendo dois números inteiros positivos, N e M (0 < N, M < 500), representando o número inicial de abas e o número
de ações de Péricles. Cada linha subsequente contém uma ação (fechou ou clicou). Naturalmente, o número de abas é sempre maior ou igual a zero.

Saída
A saída deve ser uma linha contendo o número final de abas.
'''
n, m = [int(x) for x in input().split()]
while n <= 0 and m <= 0 or m > 500:
    n, m = [int(x) for x in input().split()]

acoes = list()
for x in range(0,m):
    acoes.append(input())

for y in range(0,m):
    if y == 'fechou':
        n = (n+2)-1
    elif y == 'clicou':
        n += 1
print(n)   