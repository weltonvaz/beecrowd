def verificar_troco(N, M):
    notas = [2, 5, 10, 20, 50, 100]
    troco = M - N

    # Verifica todas as combinações de duas notas
    for i in range(len(notas)):
        for j in range(i, len(notas)):
            if notas[i] + notas[j] == troco:
                return "possible"
    
    return "impossible"

def main():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        print(verificar_troco(N, M))

# Exemplo de execução
main()
