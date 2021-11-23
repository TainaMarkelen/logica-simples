if __name__ ==  '__main__':
    vector = []
    #soma = 0
    for i in range (0, 20):
        n = int(input("Insira {0}/20 para o vetor: ".format(i+1)))
        vector.append(n)
        #soma = soma + n
    print(sum(vector))
        
    