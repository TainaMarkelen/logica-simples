if __name__ == '__main__':
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")
    while senha == nome:
        print("A senha não pode ser igual ao nome")
        nome = input ("Informe o nome: ")
        senha = input("Informe a senha: ")