#Entrada de dados
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
bpm = int(input("Digite a medida de batimentos por minuto (BPM): "))
#Verifiar condições e retornar dado
if idade <= 2 and bpm >= 120 and bpm <= 140:
    print(f"{nome}, seus batimentos cardiácos ({bpm} BPM) estão dentro do limite estipulado pelo Ministério da Saúde.")
elif idade >= 8 and idade <= 17 and bpm >= 80 and bpm <= 100:
    print(f"{nome}, seus batimentos cardiácos ({bpm} BPM) estão dentro do limite estipulado pelo Ministério da Saúde.")
elif idade >= 18 and idade <= 65 and bpm >= 70 and bpm <= 80:
    print(f"{nome}, seus batimentos cardiácos ({bpm} BPM) estão dentro do limite estipulado pelo Ministério da Saúde.")
elif idade > 65 and bpm >= 50 and bpm <= 60:
    print(f"{nome}, seus batimentos cardiácos ({bpm} BPM) estão dentro do limite estipulado pelo Ministério da Saúde.")
else:
    print(f"{nome}, seus batimentos por minuto, ({bpm} BPM) estão fora do padrão estipulado pelo Ministério da Saúde.")
    print("Procure o seu médico.")
