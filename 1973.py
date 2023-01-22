#!/usr/bin/python3

n = int(input())
nums = list(map(int, input().split()))

pos, soma, total, continua = 0, 0, sum(nums), True

for i, num in enumerate(nums):
    if num % 2 == 0 and continua:
        ataques = i + 1
        soma += ((i * 2) + 1) - pos
        continua = False
    elif num - 1 == 0 and continua:
        pos = i + 1

if soma > 0:
    total -= soma
else:
    ataques = n
    total -= ataques

print(f"{ataques} {total}")
