if __name__ == '__main__':
    #variáveis
    vector1 = []
    vector2 = []
    soma = []
    #entrada/processamento
    for i in range (1, 11):
        valor1 = int(input("Informe um valor para o primeiro vetor: "))
        vector1.append(valor1)
        valor2 = int(input("Informe um valor para o segundo vetor: "))
        vector2.append(valor2)
        soma.append(valor1 + valor2)
    for s in soma:
        print(s)