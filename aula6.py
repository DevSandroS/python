#cálculo de IMC

#inserção de dados:
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

#estrutura para cálculo IMC
if altura <= 0 or peso <= 0:
    print("Altura e peso devem ser maiores que zero.")
else:
    
    #calculo do IMC
    imc = peso / (altura ** 2)

    #mostrando resultado
    if imc <= 18.5:
        print(f"{nome}, seu IMC é de {imc:.2f}, considerado abaixo do normal")
    elif imc <= 24.9:
        print(f"{nome}, seu IMC é de {imc:.2f}, considerado normal")
    elif imc <= 29.9:
        print(f"{nome}, seu IMC é de {imc:.2f}, considerado sobrepeso")
    elif imc <= 34.9:
        print(f"{nome}, seu IMC é de {imc:.2f}, considerado obesidade grau 1")
    elif imc <= 39.9:
        print(f"{nome}, seu IMC é de {imc:.2f}, considerado obesidade grau 2")
    else:
        print(f"{nome}, seu IMC é de {imc:.2f}, considerado obesidade 3")