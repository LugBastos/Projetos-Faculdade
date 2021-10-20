#Entrada de dados
segunda = int(input("Informe a pontuação de Segunda-feira: "))
terca = int(input("Informe a pontuação de Terça-feira: "))
quarta = int(input("Informe a pontuação de Quarta-feira: "))
quinta = int(input("Informe a pontuação de Quinta-feira: "))
sexta = int(input("Informe a pontuação de Sexta-feira: "))
#Verificação condicional e retorno
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f"Segunda-feira teve o maior número de votos! ({segunda})")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print(f"Terça-feira teve o maior número de votos! ({terca})")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print(f"Quarta-feira teve o maior número de votos! ({quarta})")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print(f"Quinta-feira teve o maior número de votos! ({quinta})")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print(f"Sexta-feira teve o maior número de votos! ({sexta})")
else:
    print("Tivemos um empate! Veja os critérios de desempate.")
