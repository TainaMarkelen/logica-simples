if __name__ == '__main__':
    #variáveis
    maior = 0
    #entrada
    n = int(input("Informe um número: "))
    while n != 0:
        if n > maior:
            maior = n
        n = int(input("Informe um número: "))
    print("O maior valor é {0}".format(maior))
            