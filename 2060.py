# -*- coding: utf-8 -*-
'''
Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver. Desta vez, Bino gerou uma lista
de números e perguntou ao Cino quantos números da lista são múltiplos de 2, 3, 4 e 5.
Esse desafio pode parecer simples, porém, quando a lista contém muitos números, Cino se confunde e acaba errando alguns cálculos.
Para ajudar Cino, faça um programa para resolver o desafio de Bino.

Entrada
A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando a quantidade de números na lista de Bino.

A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da lista de Bino.

Saída
Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da saída nos exemplos,
pois ela deve ser seguida rigorosamente.
'''

n = int(input())
wert = [int(x) for x in input().split()]

count2, count3, count4, count5 = 0, 0, 0, 0

for x in wert:
    if x % 2 == 0:
        count2 += 1
    if x % 3 == 0:
        count3 += 1
    if x % 4 == 0:
        count4 += 1
    if x % 5 == 0:
        count5 += 1

print(f"{count2} Multiplo(s) de 2")
print(f"{count3} Multiplo(s) de 3")
print(f"{count4} Multiplo(s) de 4")
print(f"{count5} Multiplo(s) de 5")