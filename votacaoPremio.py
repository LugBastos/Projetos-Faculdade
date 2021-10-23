#Entrade de valores
coloborador1 = int(input("Primeiro colaborador, escolha o console de última geração: (1)PLAYSTATION / (2)XBOX / (3)NINTENDO "))
coloborador2 = int(input("Segundo colaborador, escolha o console de última geração: (1)PLAYSTATION / (2)XBOX / (3)NINTENDO "))
coloborador3 = int(input("Terceiro colaborador, escolha o console de última geração: (1)PLAYSTATION / (2)XBOX / (3)NINTENDO "))
coloborador4 = int(input("Quarto colaborador, escolha o console de última geração: (1)PLAYSTATION / (2)XBOX / (3)NINTENDO "))
coloborador5 = int(input("Quinto colaborador, escolha o console de última geração: (1)PLAYSTATION / (2)XBOX / (3)NINTENDO "))
#Contador de votos
voto_playstation = 0
voto_xbox = 0
voto_nintendo = 0
#Analise votos primeiro colaborador
if coloborador1 == 1:
    voto_playstation = voto_playstation + 1
elif coloborador1 == 2:
    voto_xbox = voto_xbox + 1
elif coloborador1 == 3:
    voto_nintendo = voto_nintendo + 1
#Analise votos segundo colaborador
if coloborador2 == 1:
    voto_playstation = voto_playstation + 1
elif coloborador2 == 2:
    voto_xbox = voto_xbox + 1
elif coloborador2 == 3:
    voto_nintendo = voto_nintendo + 1
#Analise votos terceiro colaborador
if coloborador3 == 1:
    voto_playstation = voto_playstation + 1
elif coloborador3 == 2:
    voto_xbox = voto_xbox + 1
elif coloborador3 == 3:
    voto_nintendo = voto_nintendo + 1
#Analise votos quarto colaborador
if coloborador4 == 1:
    voto_playstation = voto_playstation + 1
elif coloborador4 == 2:
    voto_xbox = voto_xbox + 1
elif coloborador4 == 3:
    voto_nintendo = voto_nintendo + 1
#Analise votos quinto colaborador
if coloborador5 == 1:
    voto_playstation = voto_playstation + 1
elif coloborador5 == 2:
    voto_xbox = voto_xbox + 1
elif coloborador5 == 3:
    voto_nintendo = voto_nintendo + 1
#Desvio condicional vitoria
if voto_playstation > voto_xbox and voto_playstation > voto_nintendo:
    print("***********************************")
    print("PLAYSTATION WIN! Total de votos: {}".format(voto_playstation))
    print("***********************************")
elif voto_xbox > voto_playstation and voto_xbox > voto_nintendo:
    print("***********************************")
    print("XBOX WIN! Total de votos: {}".format(voto_xbox))
    print("***********************************")
elif voto_nintendo > voto_playstation and voto_nintendo > voto_xbox:
    print("***********************************")
    print("NINTENDO WIN! Total de votos: {}".format(voto_nintendo))
    print("***********************************")
else:
    print("Dois consoles tiveram a mesma quantidade de votos.")
    print("Verifique os critérios de desempate.")
