#Lê o salário da pessoa e fornece um empréstimo

valor_da_casa = float(input("Valor da casa: R$"))
salario_da_pessoa = float(input("Seu salário: R$"))
anos_de_financiamento = int(input("Anos de financiamento: "))
prestacao_da_casa = valor_da_casa / (anos_de_financiamento * 12)
minimo_do_salario = salario_da_pessoa * 30/100

print(f"para pagar uma casa de {valor_da_casa:.2f} em {anos_de_financiamento} anos, a prestação será de {prestacao_da_casa:.2f}")

if prestacao_da_casa <= minimo_do_salario:
    print("Empréstimo CONCEDIDO.")
else:
    print("Empréstimo REPROVADO.")
