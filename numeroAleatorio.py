from random import randint
from time import sleep

computador = randint(0, 5)
jogador = int(input("Digite um número: "))

print("PROESSANDO... \n")
sleep(3)

if jogador == computador:
    print (f"Você venceu, eu pensei no número {computador}")
else: 
    print(f"Você perdeu! eu pensei no número {computador} e não no número {jogador}")
    