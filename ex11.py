import string

usuario=input("Insira um nome de usuario: ")
senha=(input("Insira uma senha para a conta: "))
if len(usuario)< 12:
    print("O nome de usuario tem que ter no minimo 12 caracteres!!!!")
    exit()
elif len(senha)< 8 and type(senha==string):
    print("A senha e curta demais, precisa ter no minimo 8 caracteres!!!")
elif not senha.isalpha():
    print("A senha não pode conter caracteres especiais")
else:
    print("Sua conta foi criada com sucesso.")