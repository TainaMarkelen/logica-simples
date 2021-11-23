if __name__ == '__main__':
    #entradas
    quantidade_minima = int(input("Informe quantidade mínima: "))
    quantidade_maxima = int(input ("Informe quantidade maxima: "))
    #processamento
    soma = quantidade_minima + quantidade_maxima
    divisao = soma / 2
    #saída
    print ("O estoque médio é {0}".format(divisao))