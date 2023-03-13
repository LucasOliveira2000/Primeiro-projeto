print(' +++++++++++++++++++++++++ ')
print(' Bem vindo ao nosso jogo! ')
print(' +++++++++++++++++++++++++')


user = input(" Você quer começar agora? \n ( S ) para entrar  \n ( N ) para sair \n Resposta : ").upper()

if user == "S" :
    print(" \n ")
    print(" Vamos começar (っ▀¯▀)つ ")
    print(" \n ")
elif user == "N":
    print(" Volte mais tarde então...")
else:
    quit()

import random
def jogar():
    jogada = input(" > Escolha pedra, papel ou tesoura: ")
    while jogada.lower() not in [" pedra", "papel", " tesoura "]:
        jogada = input(" Escolha inválida. Escolha pedra, papel ou tesoura: ".lower())
    return jogada.lower()
def jogada_computador():
    jogadas = ["pedra", "papel", "tesoura"]
    return random.choice(jogadas)
def avaliar_jogada(jogada_jogador, jogada_computador):
    if jogada_jogador == jogada_computador:
        print(" Empatou! ")
    elif jogada_jogador == " pedra ":
        if jogada_computador == " papel ":
            print(" Você perdeu! Papel cobre pedra. ")
        else:
            print(" Você ganhou! Pedra quebra tesoura. ")
    elif jogada_jogador == " papel ":
        if jogada_computador == " tesoura ":
            print(" Você perdeu! Tesoura corta papel. ")
        else:
            print(" Você ganhou! Papel cobre pedra. ")
    elif jogada_jogador == " tesoura ":
        if jogada_computador == " pedra ":
            print(" Você perdeu! Pedra quebra tesoura. ")
        else:
            print(" Você ganhou! Tesoura corta papel. ")






