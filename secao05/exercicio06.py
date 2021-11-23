if __name__ == '__main__':
    vector = []
    codigo = int(input("Informe o código: "))
    if codigo != 0:
        for n in range(0, 5):
            num = float(input("Informe um valor real: "))
            vector.append(num)
        if codigo == 1:
            for n in vector:
                print(n)
        if codigo == 2:
            vector.reverse()
            for n in vector:
                print(n)