if __name__ == '__main__':
    e = 0
    m = 0
    #entradas
    p = float(input("Insira o peso dos peixes: "))
    #processamento
    if p > 50:
        e = p - 50
        m = e * 4
    print("Peso: {0}".format(p))
    print("Excesso: {0}".format(e))
    print("Multa: R$ {0:.2f}".format(m))
            
            