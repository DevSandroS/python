#Par ou ìmpar
#Escreva um programa que peça um número ao usuário e diga se ele é par ou ímpar.

#inserção de dados:
usuario = input("Insira seu nome: ")
numero = int(input("Insira um numero: "))

#verificação de dados inseridos:
if numero % 2 == 0 and numero != 0: #retorna numero par
    print(f"Olá {usuario}, o número que você inseriu é par.")
elif numero % 2 != 0 and numero != 0: #retorna número ímpar
    print(f"Olá {usuario}, o número que você inseriu é ímpar.")
else: #solicita ao usuário um novo número.
    print(f"Por favor {usuario}, insira um número diferente de zero.")