if __name__ == '__main__':
    vector = []
    for i in range(1, 11):
        n = int(input("Insira um número: "))
        vector.append(n)
    vector.reverse()
    for i in vector:
        print(i)