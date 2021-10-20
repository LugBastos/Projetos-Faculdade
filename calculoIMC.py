import math
#Entrada de dados
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a su altura: "))
imc = peso / (altura * altura)
#Verificação condicional e retorno
if imc < 16.00:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Baixo peso Grau III")
elif imc > 16.00 and imc < 16.99:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Baixo peso Grau II")
elif imc > 17.00 and imc < 18.49:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Baixo peso Grau I")
elif imc > 18.50 and imc < 24.99:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Peso ideal")
elif imc > 25.00 and imc < 29.99:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Sobrepeso")
elif imc > 30.00 and imc < 34.99:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Obesidade Grau I")
elif imc > 35.00 and imc < 39.99:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Obesidade Grau II")
elif imc > 40.00:
    print("Valor IMC: {0:.2f}".format(imc))
    print("Classificação: Obesidade Grau II")
