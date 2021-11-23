if __name__ == '__main__':
    #variáveis
    valor_hora = 10.00
    valor_hora_excedente = 20.00
    e = 0
    #entradas
    c = int(input("Insira o código: "))
    n = float(input("Insira as horas trabalhadas: "))
    if n > 50:
        e = (n - 50) * valor_hora_excedente
        salário = (50 * valor_hora) + e
        print("Salário total: R$ {0:.2f}".format(salário))
        print("Extra: R$ {0:.2f}".format(e))
    else:
        salário = (n * valor_hora)
        print("Salário total R$ {0:.2f}".format(salário))
        print("Extra R$ {0:.2f}".format(e))
    