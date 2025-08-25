#Peça uma frase ao usuário e diga quantas palavras tem nela.

#inserção de dados
usuario = input("Qual seu nome: ")
frase = input(f"Olá {usuario}! por favor, insira a frase desejada: ")
palavras = frase.split()
total_pavras = len(palavras)
#lógica do programa
print(f"Olá {usuario}! o total de pavras é: {total_pavras}.")

