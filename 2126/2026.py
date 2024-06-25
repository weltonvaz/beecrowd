# -*- coding: utf-8 -*-
def find_subsequences(n1, n2):
    """
    Função para encontrar e contar subsequências contíguas de n1 em n2
    """
    # Converter números para strings para facilitar a manipulação
    str_n1 = str(n1)
    str_n2 = str(n2)
    
    # Comprimento do primeiro número
    len_n1 = len(str_n1)
    
    # Inicializar contador de subsequências e posição da última subsequência
    count = 0
    last_position = -1
    
    # Percorrer n2 para encontrar todas as ocorrências de n1 como uma subsequência contígua
    for i in range(len(str_n2) - len_n1 + 1):
        # Verificar se a substring de n2 corresponde a n1
        if str_n2[i:i+len_n1] == str_n1:
            count += 1
            last_position = i + 1  # Atualizar última posição (índice baseado em 1)
    
    # Retornar o contador e a última posição
    return count, last_position

def main():
    """
    Função principal para lidar com entrada/saída e chamar a função de encontrar subsequências
    """
    case_number = 1

    while True:
        try:
            # Ler o primeiro número
            n1 = input().strip()
            if not n1:
                raise EOFError
            n1 = int(n1)
            
            # Ler o segundo número
            n2 = input().strip()
            if not n2:
                raise EOFError
            n2 = int(n2)
            
            # Encontrar as subsequências
            count, last_position = find_subsequences(n1, n2)
            
            # Imprimir o resultado para cada caso
            print(f"Caso #{case_number}:")
            if count > 0:
                print(f"Qtd.Subsequencias: {count}")
                print(f"Pos: {last_position}")
            else:
                print("Nao existe subsequencia")
            print()
            
            # Incrementar o número do caso para o próximo caso
            case_number += 1
        
        except EOFError:
            break

# Ponto de entrada do script
if __name__ == "__main__":
    main()
