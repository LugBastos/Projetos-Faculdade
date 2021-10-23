#Entrada de dados
minutos = int(input("Digite os minutos: "))
#Variaveis de controle
multiplicador = minutos
fatorial = 1
#Loop dos multiplicadores para p cálculo fatorial
while multiplicador > 0:
    fatorial = multiplicador * fatorial
    multiplicador -= 1
print("A senha necessária para o desbloqueio é: LIBERDADE{}".format(fatorial))