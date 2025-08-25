#Peça uma frase ao usuário e diga quantas palavras tem nela.

#inserção de dados
usuario = input("Qual seu nome: ")
frase = input(f"Olá {usuario}! por favor, insira a frase desejada: ") #peça uma frase ao usuário. 
palavras = frase.split() #split() separa a string em uma lista de palavras.
total_pavras = len(palavras) #len() conta a quantidade de elementos em uma lista. palavras é uma lista.
#imprime o resultado
print(f"{usuario}, o total de pavras é: {total_pavras}!")


