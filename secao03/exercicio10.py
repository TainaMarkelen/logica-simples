if __name__ == '__main__':
    #entradas
    idade = int(input("Informe uma idade: "))
    #processamento
    if idade >= 5 and idade <= 7:
        print("infantil-a")
    elif idade >= 8 and idade <= 11:
        print("infantil-b")
    elif idade >=12 and idade <=13:
        print("juvenil-a")
    elif idade >= 14 and idade <= 17:
        print("juvenil-b")
    elif idade >= 18:
        print("adultos")