"""
The Fibonacci sequence is one of the most famous sequences in the world. Fibonacci terms are always equal to the sum of the two terms before them in the sequence, and the first two terms are 1. That is:

1, 1, 2, 3, 5, 8, 13, 21, 34...

However, we are not interested in finding the terms of the Fibonacci sequence, but the terms of the Fibonot sequence!

The Fibonot sequence is made up of the numbers that do not belong to the Fibonacci sequence. More specifically, non-zero positive integers. In ascending order!

Here are the first Fibonot terms:

4, 6, 7, 9, 10, 11, 12, 14, 15...

Your task is to find the Kth Fibonot number.

Input
The input consists of a single integer K (1 ≤ K ≤ 105) specifying the index of the desired Fibonot sequence element.

Exit
A single integer representing the Kth term of the Fibonot sequence.
"""
def fibonot(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return b
print(fibonot(int(input())))