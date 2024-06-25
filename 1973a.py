#!/usr/bin/python3

def calculate_attacks_and_remaining_total(n, nums):
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

    return ataques, total

# Input the number of elements
n = int(input())

# Input the list of numbers
nums = list(map(int, input().split()))

# Calculate the attacks and the remaining total
ataques, total = calculate_attacks_and_remaining_total(n, nums)

# Print the result
print(f"{ataques} {total}")

