from datetime import date

while True:
    try:
        # Lê a entrada do usuário e converte para inteiros
        mes, dia = map(int, input().split())

        # Cria objetos de data para a data atual e o Natal
        data_atual = date(2024, mes, dia)
        natal = date(2024, 12, 25)
        
        # Calcula a diferença em dias entre o Natal e a data atual
        diferenca = (natal - data_atual).days

        # Verifica e imprime a mensagem apropriada com base na diferença em dias
        if diferenca == 0:
            print("E natal!")
        elif diferenca == 1:
            print("E vespera de natal!")
        elif diferenca < 0:
            print("Ja passou!")
        else:
            print(f"Faltam {diferenca} dias para o natal!")
    
    # Termina o loop ao encontrar o fim do arquivo (EOF)
    except EOFError:
        break

