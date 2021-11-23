if __name__ == '__main__':
    #variáveis
    p = 0
    i = 0
    #entradas
    número = int(input("Informe um número: "))
    #processamento
    if número % 2 == 0:
        p = número
    else:
        i = número
    print(p)
    print(i)