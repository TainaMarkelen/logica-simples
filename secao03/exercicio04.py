if __name__ == '__main__':
    #entradas
    altura = float(input("Informe sua altura: "))
    sexo = (input("Informe seu sexo (m/f): "))
    #processamento
    if sexo.lower() == 'm':
        peso_ideal = (altura * 72.7) - 58
    elif sexo.lower() == 'f':
        peso_ideal = (altura * 62.1) - 44.7
    else:
        peso_ideal = 0
        print("Sexo não reconhecido")
    #saída
    print("Seu peso ideal é: {0:.2f}".format(peso_ideal))
        
    