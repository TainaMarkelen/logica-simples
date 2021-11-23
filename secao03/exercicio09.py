if __name__ == '__main__':
    #entrada
    p = float(input("Informe o índice de poluição: "))
    #processamento
    if p >= 0.3 and p < 0.4:
        print("Grupo 1: suspender atividades!")
    elif p >= 0.4 and p < 0.5:
        print("Grupos 1 e 2: suspender atividades!")
    elif p >= 0.5:
        print("Todos os grupos: suspender atividades!")
    else:
        print("Níveis de poluíção aceitáveis")