#!/usr/bin/python3

def encontrar_posicoes(nums):
    """Encontra as posições do primeiro número par e do primeiro 1 na lista."""
    pos_par, pos_um = None, None
    for i, num in enumerate(nums):
        if num % 2 == 0 and pos_par is None:
            pos_par = i
        if num == 1 and pos_um is None:
            pos_um = i
        if pos_par is not None and pos_um is not None:
            break
    return pos_par, pos_um

def calcular_ataques_e_total(nums, pos_par, pos_um):
    """Calcula o número de ataques e o total restante."""
    total = sum(nums)
    ataques = len(nums)  # Valor padrão se não houver número par

    if pos_par is not None:
        ataques = pos_par + 1
        soma = pos_par * 2 + 1  # Correção na fórmula da soma
        total -= soma
    return ataques, total

# Leitura da entrada
n = int(input())
nums = list(map(int, input().split()))

# Cálculo das posições e dos resultados
pos_par, pos_um = encontrar_posicoes(nums)
ataques, total = calcular_ataques_e_total(nums, pos_par, pos_um)

# Saída
print(f"{ataques} {total}")


