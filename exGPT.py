
"""
Exercício 2
 Peça dois números ao usuário e mostre:

    A soma

    A subtração

    A multiplicação

    A divisão com 2 casas decimais
"""

#inserindo os numeros:
numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

#realizando a soma:
soma = numero1 + numero2
print("A soma é ", soma)

#realizano a subtração:
sub = numero1 - numero2
print("A subtração é ", sub)

#realizando a multiplicação:
multiplicaçao = numero1 * numero2
print("A multiplicação é ", multiplicaçao)

#divisão com duas casas decimais:
divisão = numero1/numero2
if numero2 != 0:
    divisao = numero1 / numero2
    print(f"A Divisão com duas casas é {divisao:.2f}")
else:
    print("Não é possível dividir por zero!")


"""
Exercício 3:
Peça um número ao usuário e diga se ele é:

    Positivo

    Negativo

    Zero
"""

#usuário digita o número:
num = int(input("Digite um número qualquer: "))

#retornando o tipo:
if (num < 0):
    print("O número é negativo.")
elif(num > 0):
    print("O número é positivo.")
else:
    print("O número é neutro.")



"""
Exercício 4:
Peça a idade do usuário e diga se ele é:

    Menor de idade

    Maior de idade
"""
idade_usuario = int(input("Digite sua idade: "))

if(idade_usuario < 18):
    print("Menor de idade.")
else:
    print("Maior de idade.")