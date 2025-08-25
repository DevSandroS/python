#converte um numero para base binaria, octal, ou hexadecimal

numero_do_usuario = int(input("Digite um numero para ser convertido: "))

print('''ESCOLHA UMA OPÇÃO:
      [ 1 ] BINARIO
      [ 2 ] OCTAL
      [ 3 ] HEXADECIMAL''')

opcao_escolhida = int(input("Opção: "))

if opcao_escolhida == 1:
    print('{} convertido para BINARIO é {}'.format(numero_do_usuario, bin(numero_do_usuario) [2:]))
elif opcao_escolhida == 2:
    print(f'O número {numero_do_usuario} em OCTAL é {oct(numero_do_usuario)[2:]}')
elif opcao_escolhida == 3:
    print(f'O número {numero_do_usuario} em HEXADECIMAL é {hex(numero_do_usuario)[2:]}')
else:
    print('Número inválido.')