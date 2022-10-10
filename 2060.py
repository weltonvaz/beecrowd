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
Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da saída nos exemplos, pois ela deve ser seguida rigorosamente.
'''
from sympy import divisor_count

n = int(input())
wert = [int(x) for x in input().split()]

print(wert)