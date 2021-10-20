#Entrada valor
tipo_assinatura = int(input("Qual o tipo de assinatura: (1)Basic / (2)Silver / (3)Gold / (4)Platinum "))
faturamento_anual = float(input("Valor de faturamento anual: R$"))
valor_bonus = 0
#Verificação condicional e retorno
if tipo_assinatura == 1:
    valor_bonus = faturamento_anual * 0.3
    print("O valor do bônus será de: R${0:.2f}".format(valor_bonus))
elif tipo_assinatura == 2:
    valor_bonus = faturamento_anual * 0.2
    print("O valor do bônus será de: R${0:.2f}".format(valor_bonus))
elif tipo_assinatura == 3:
    valor_bonus = faturamento_anual * 0.1
    print("O valor do bônus será de: R${0:.2f}".format(valor_bonus))
elif tipo_assinatura == 4:
    valor_bonus = faturamento_anual * 0.05
    print("O valor do bônus será de: R${0:.2f}".format(valor_bonus))
else:
    print("Valor incorreto.")