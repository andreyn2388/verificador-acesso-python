# Projeto: Verificador de Acesso
# Objetivo: Treinar if e else em Python

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
documento = input("Você tem documento? (sim ou nao): ")

if idade >= 18:
    if documento == "sim":
        print(nome, "pode entrar")
    else:
        print(nome, "não pode entrar (sem documento)")
else:
    print(nome, "não pode entrar (menor de idade)")
