if __name__ == '__main__':
    #variáveis
    vector = [] #lista vazia
    pairs = [] #lista vazia
    for n in range(1, 6):
        n = int(input("Informe um valor:  "))
        vector.append(n) #vector recebe n
        if n > 0 and n % 2 == 0:
            pairs.append(n) #pairs recebe n
    for p in pairs: #print only pairs
        print(p)
    
        
