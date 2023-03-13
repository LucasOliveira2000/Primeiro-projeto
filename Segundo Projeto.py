print(' +++++++++++++++++++++++ ')
print(' Bem vindo ao nosso site! ')
print(' +++++++++++++++++++++++ ')

perguntas = ["1.Qual plataforma faz parte o jogo Lost Ark?", "2.Qual plataforma faz parte o jogo League of Legends ?",
             "3.Qual a cor do cavalo branco de napoleão?"]
respostas = ["steam", "riot games", "branco"]
pontuacao = 0

user = input(' Quer começar? (S/N) :  ').upper()

if user == "S":
    print(" Vamos começar...")
    print("\n")
elif user == "N":
    print("\n")
    print(" Volte mais tarde então...")
    print("\n")
    quit()
else:
    quit()


for i in range(len(perguntas)):
    while True:
        try:
            resposta = input(perguntas[i])
            if resposta == respostas[i]:
                print("Parabéns, você acertou 👍")
                print("\n")
                pontuacao += 1
                break
            else:
                print("Resposta incorreta ❌")
                print("\n")
                break

        except ValueError:
            print("Digite uma resposta válida!")

print("Fim do quizz. Você acertou", pontuacao, "perguntas!")