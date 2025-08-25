#preço de cada item do menu do restaurante

#dados do cliente
print("Bem vindo(a) ao restaurante do Seu Menino!\n")
nome_cliente = input("Qual o seu nome? \n")

#declaração de preços
hamburguer = 23.90
babata_frita = 12.00
refrigerante = 9.50
milk_shake = 18.90
cafezinho = 7.00
coxinha = 9.00
norget = 5.50

#retornando o valor dos itens:
print(f"Olá {nome_cliente}! Este é o menu: \n")
print(f"Hamburguer: R${hamburguer:.2f}")
print(f"Bata frita: R${babata_frita:.2f}")
print(f"Refrigerante: R${refrigerante:.2f}")
print(f"Milk shake: R${milk_shake:.2f}")
print(f"Norget (5 unidades): R${norget:.2f}")
print(f"Cafezinho: R${cafezinho:.2f}")
print(f"Coxinha: R${coxinha:.2f} \n")


#definição da quantidade
quantidade_hamburguer = int(input("Quantidade de hamburguers: "))
quantidade_batata_frita = int(input("Quantidade de batata-fritas: "))
quantidade_refrigerante = int(input("Quantidade de refrigerantes: "))
quantidade_milk_shake = int(input("Quantidade de milk shakes: "))
quantidade_cafezinho = int(input("Quantidade de cafezinhos: "))
quantidade_coxinha = int(input("Quantidade de coxinhas: "))
quantidade_norget = int(input("Quantidade de norgets: "))

#retornando o preço total
preco_total = (hamburguer * quantidade_hamburguer) + (babata_frita * quantidade_batata_frita) + (refrigerante * quantidade_refrigerante) + (milk_shake * quantidade_milk_shake)
print(f"{nome_cliente}, o valor do seu pedido é de R$ {preco_total:.2f}")
