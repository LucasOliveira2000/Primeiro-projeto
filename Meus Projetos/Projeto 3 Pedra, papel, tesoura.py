print(' -= ' * 8)
print(' > Bem vindo ao nosso jogo! <')
print(' -= ' * 8)


user = input(" \n Você quer começar agora? \n [ S ] para entrar  \n [ N ] para sair \n Resposta : ").upper()

if user == "S" :
    print(" \n ")
    print(" Vamos começar (っ▀¯▀)つ ")
    print(" \n ")
elif user == "N":
    print(" Volte mais tarde então...")
else:
    quit()

import random

# Enquanto for verdadeiro
while True:

    # Lista com as opções
    escolha = [" Pedra ", " Papel ", " Tesoura "]

    #Jogada do computador
    jogada_pc = random.choice(escolha)


    # Váriavel jogador faz uma pergunta para o user
    jogador = int(input(" > Escolha uma opção abaixo ! < \n [ 0 ] Pedra \n [ 1 ] Papel \n [ 2 ] Tesoura \n [ 3 ] Sair \n > Resposta: "))

    # Se jogador apertar 3 o programa sai
    if jogador ==  3 :
        print(" \n ")
        print(" > Volte mais tarde 🥺! < ")
        break

    # Se jogador escolher alguma coisa que não esteja dentro da lista ' escolha ❌ '
    elif jogador not in escolha:
        print(" \n ")
        print(" Opção inválida ❌ , tente novamente mais tarde.")
        break


    if jogador == jogada_pc :
        resultado = " Empatou 🥺."

    elif jogador ==  0  and jogada_pc ==  2 :
        print(" Você ganhou 👍. Pedra quebra a tesoura! ")


    elif jogador ==  1 and jogada_pc ==  0 :
        print(" Você ganhou 👍. Papel embrulha a pedra! ")


    elif jogador ==  2  and jogada_pc ==  1 :
        print(" Você ganhou 👍 . Tesoura corta o papel! ")

    else:
        print(f" Computador jogou {jogada_pc}. Você perdeu ❌ ")
























































