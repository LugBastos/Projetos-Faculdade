#Entrada de dados
valor_bruto = float(input("Informe o valor bruto: R$"))
categoria_assentos = int(input("Informe a categoria: (1)Econômica / (2)Executiva / (3)Primeira classe "))
quantidade_viajantes = int(input("Informe a quantidade de viajantes: "))
#Variáveis cálculo
valor_desconto = 0
valor_liquido = 0
valor_medio = 0
#Verifiar condições e retornar dado com desconto ou não
if categoria_assentos == 1 and quantidade_viajantes == 2:
    valor_desconto = valor_bruto * 0.03
    valor_liquido = valor_bruto - float(valor_desconto)
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(3%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 1 and quantidade_viajantes == 3:
    valor_desconto = valor_bruto * 0.04
    valor_liquido = valor_bruto - float(valor_desconto)
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(4%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 1 and quantidade_viajantes >= 4:
    valor_desconto = valor_bruto * 0.05
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(5%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 2 and quantidade_viajantes == 2:
    valor_desconto = valor_bruto * 0.05
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(5%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 2 and quantidade_viajantes == 3:
    valor_desconto = valor_bruto * 0.07
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(7%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 2 and quantidade_viajantes >= 4:
    valor_desconto = valor_bruto * 0.08
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(8%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 3 and quantidade_viajantes == 2:
    valor_desconto = valor_bruto * 0.10
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(10%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 3 and quantidade_viajantes == 3:
    valor_desconto = valor_bruto * 0.15
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(15%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif categoria_assentos == 3 and quantidade_viajantes >= 4:
    valor_desconto = valor_bruto * 0.20
    valor_liquido = valor_bruto - valor_desconto
    valor_medio = valor_liquido / quantidade_viajantes
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor de desconto(20%): R${0:.2f}".format(valor_desconto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
    print("Valor médio por visitantes: R${0:.2f}".format(valor_medio))
elif quantidade_viajantes == 1:
    valor_liquido = valor_bruto - valor_desconto
    print("O valor bruto foi de: R${0:.2f}".format(valor_bruto))
    print("Valor à pagar: R${0:.2f}".format(valor_liquido))
elif categoria_assentos != 1 or categoria_assentos != 2 or categoria_assentos != 3:
    print("*************************************")
    print("Erro. Valor inserido incorretamente.")
    print("Revise o valor da categoria.")
    print("*************************************")