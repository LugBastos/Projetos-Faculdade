#Variaveis para calculo de media
nota_aluno_impar_total = 0
nota_aluno_par_total = 0
total_alunos = 6 #Variavel de com o total de alunos
#Entrada de dados alunos impares
print("**********VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES**********")
for i in range (1,total_alunos+1,2):
    nota_aluno_impar = input("POR FAVOR, INSIRA A NOTA DO {}º ALUNO: ".format(i))
    while nota_aluno_impar == "":
        print("Nota inválida, digite novamente.")
        nota_aluno_impar = input("POR FAVOR, INSIRA A NOTA DO {}º ALUNO: ".format(i))
    nota_aluno_impar_total = nota_aluno_impar_total + float(nota_aluno_impar)
    media_impar = float(nota_aluno_impar_total / (total_alunos / 2))
#Entrada de dados alunos pares
print(("**********VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES**********"))
for i in range (2,total_alunos+1,2):
    nota_aluno_par = input("POR FAVOR, INSIRA A NOTA DO {}º ALUNO: ".format(i))
    while nota_aluno_par == "":
        print("Nota inválida, digite novamente.")
        nota_aluno_par = input("POR FAVOR, INSIRA A NOTA DO {}º ALUNO: ".format(i))
    nota_aluno_par_total = nota_aluno_par_total + float(nota_aluno_par)
    media_par = float(nota_aluno_par_total / (total_alunos / 2))
#Teste condicional, de qual média é maior
if media_impar > media_par:
    print("Os alunos ímpares tiveram a média maior do que os alunos pares.")
    print("Alunos Ímpares: {:.1f}".format(media_impar))
    print("Alunos Pares: {:.1f}".format(media_par))
elif media_par > media_impar:
    print("Os alunos pares tiveram a média maior do que os alunos impares.")
    print("Alunos Pares: {:.1f}".format(media_par))
    print("Alunos Ímpares: {:.1f}".format(media_impar))
else:
    print("Os alunos das duas turmas empataram no valor da média.")
    print("Alunos Ímpares: {:.1f}".format(media_impar))
    print("Alunos Pares: {:.1f}".format(media_par))