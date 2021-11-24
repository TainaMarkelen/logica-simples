if __name__ == '__main__':
    frutas = ["jabuticaba", "cupu", "graviola"]
    
    # gosto assume o valor das frutas, uma por vez, até percorrer a lista inteira
    for gosto in frutas:
        print("eu adoro " + gosto)
        
    #imprimir os quadrados de todos os números primos da lista  
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for x in primos:
        print (x**2)
        
        
    # contagens
    for i in range(20):
        print(i)
    # não inclui o 20 no final   
    for i in range(10,20):
        print(i)
        
    # conta de 0 a 20 de 3 em 3
    for i in range(0,20,3):
        print(i)
        
    # guardando em variáveis
    pares = range(0,10,2)
    for i in pares:
        print(i)
        
    # de trás para frente, de 5 em 5
    numeros = range(20, 0, -5)
    for i in numeros:
        print(i)
        
    # alterando valores da lista primos, elevando todos os itens a 3
    for i in range(len(primos)):
        primos[i] = primos[i]**3
    print(primos)