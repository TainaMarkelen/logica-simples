if __name__ == '__main__':
    #entradas
    n = int(input("Informe um número: "))
    #processamento
    if n % 2 == 0:
        if n > 0:
            print("O número {0} é par e positivo".format(n))
        else:
            print("O número {0} é par e negativo".format(n))
    else:
        if n > 0:
            print("O número {0} é ímpar e positivo".format(n))
        else:
            print("O número {0} é ímpar é negativo".format(n))