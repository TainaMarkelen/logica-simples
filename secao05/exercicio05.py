if __name__ == '__main__':
    vector = []
    tem_maior_50 = False
    for n in range (0, 10):
        num = int(input("Insira o {0}° número: ".format(n+1)))
        vector.append(num)
    for n in vector:
        if n > 50:
            print("{0} está na {1} posição".format(n, vector.index(n)))
            tem_maior_50 = True    
    if tem_maior_50 == False:
        print("Não há número maior que 50")