#Entrada de dados
movimentacoes = int(input("Quantas transações foram realizadas neste dia: "))
#Variaveis
valor = 0
valor_total = 0
valor_medio = 0
for i in range(1, movimentacoes + 1):
    valor = float(input("Qual foi o valor da {}ª operação: R$".format(i)))
    valor_total = valor + valor_total
    valor_medio = valor_total / movimentacoes
print("O valor total gasto foi de R${0:.2f}".format(valor_total))
print("O valor médio foi de R${0:.2f}".format(valor_medio))
