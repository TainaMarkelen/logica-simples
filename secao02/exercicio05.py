if __name__ == '__main__':
    #entrada
    altura = float(input("Informe sua altura: "))
    #processamento
    peso_ideal = (altura * 72.7) - 58
    #saída
    print("Seu peso ideal é {0:.2f}".format(peso_ideal))