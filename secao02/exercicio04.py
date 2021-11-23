if __name__ == '__main__':
    #Entradas
    horas_trabalhadas = int(input("Quantas horas você trabalhou no mês? R: "))
    valor_hora = float(input("Quanto você ganha por hora? R: "))
    #Processamento
    salário = horas_trabalhadas * valor_hora
    #Saída
    print("Neste mês você vai receber R$ {0:.2f}".format(salário))