#Entrada de dados
alimentos_dia = int(input("Quantidade de alimentos consumidos no dia: "))
i = 1 #Variavel controladora
calorias = 0
calorias_totais = 0
#Loop Entrada de valores caloricos
while i < alimentos_dia + 1:
    calorias = int(input("Qual é o valor calórico do {}º alimento: ".format(i)))
    calorias_totais = calorias_totais + calorias
    i += 1
print("O total de calorias consumido no dia foi de: {}kcal".format(calorias_totais))
