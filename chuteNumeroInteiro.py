#Entrada de dados
chute = int(input("Digite um número inteiro: "))
#Variaveis // valor fibonacci e número anterior
fibonacci = 0
num_anterior = 1
#Loop valores fibonacci
while chute != fibonacci:
    fibonacci_old = fibonacci
    fibonacci = fibonacci + num_anterior
    num_anterior = fibonacci_old
    #Condição valor
    if chute == fibonacci:
       print("Ação bem sucedida!")
    elif fibonacci > chute:
        print("A Ação falhou...")
        break
