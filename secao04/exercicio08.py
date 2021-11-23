# Avaliação e reparo de mouses

if __name__ == '__main__':
    def1 = 0
    def2 = 0
    def3 = 0
    def4 = 0
    total = 0
    i = int(input("Insira a identificação: "))
    while i != 0:
        print("1 = necessidade de esfera")
        print("2 = necessidade de limpeza")
        print("3 = necessidade de troca do cabo ou conector")
        print("4 = quebrado")
        defeito = int(input("Informe o defeito: "))
        if defeito == 1:
            def1 = def1 + 1
        elif defeito == 2:
            def2 = def2 + 1
        elif defeito == 3:
            def3 = def3 + 1
        elif defeito == 4:
            def4 = def4 + 1
        total += 1
        i = int(input("Insira a identificação: "))
    p1 = def1 / total * 100.0
    p2 = def2 / total * 100.0
    p3 = def3 / total * 100.0
    p4 = def4 / total * 100.0
    print ("Quantidade de mouses: {0}".format(total))
    print("Situação                                      Quantidade     Percentual")
    print("1 = necessidade de esfera                       {0}           {1:.2f}%".format(def1, p1))
    print("2 = necessidade de limpeza                      {0}           {1:.2f}%".format(def2, p2))
    print("3 = necessidade de troca de cabo ou conector    {0}           {1:.2f}%".format(def3, p3))
    print("4 = quebrado                                    {0}           {1:.2f}%".format(def4, p4))
    
    