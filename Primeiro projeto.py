#Sistema De Perguntas e Respostas

print(' +++++++++++++++++++++++ ')
print(' Bem vindo ao nosso quiz! ')
print(' +++++++++++++++++++++++ ')

user = input(' Quer começar? (S/N) ').upper()

if user == "S" :
    print(" Vamos começar...")
elif user == "N":
    print(" Volte mais tarde então...")
else:
    quit()

qtd_acertos = 0

print("1.Qual plataforma faz parte o jogo Lost Ark? \n ( 1 ) UBSOFT \n ( 2 ) GOG \n ( 3 ) STEAM \n ( 4 ) EPIC GAMES \n ")
resposta = int(input(" Digite a sua resposta: "))

if resposta == 3 :
    print(" Você Acertou  👍 ")
    qtd_acertos = qtd_acertos + 1
else:
   print(" Você errou ❌")

print("2.Qual plataforma faz parte o jogo League of Legends ? \n ( 1 ) UBSOFT \n ( 2 ) RIOT GAMES \n ( 3 ) STEAM \n ( 4 ) EPIC GAMES \n ")
resposta = int(input(" Digite a sua resposta: "))

if resposta == 2 :
    print(" Você Acertou  👍 ")
    qtd_acertos = qtd_acertos + 1
else:
   print(" Você errou ❌")

print(f" Você acertou {qtd_acertos} de todas as perguntas.")









