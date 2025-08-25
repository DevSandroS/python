#criar um programa que calcule a média de três notas fornecidas pelo usuário
#mostrando o resultado final com duas casas decimais.

#inserindo as notas
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

#gerando a média
media = (nota1 + nota2 + nota3)/3

#retornando a média das notas
print(f"A média é: {media:.2f}") 
#Exibimos o resultado da média ao usuário com duas casas decimais utilizando a formatação de string :.2f.

#outro exemplo seria:
#print("A média é %.2f" % media)