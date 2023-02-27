#Exercicio 1 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas
#de acordo com o valor digitado.

n = input( 'Qual o seu nome: ')
print('Olá {}. Prazer em te conhecer!'.format(n))

#Exercicio 2 - Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre
#uma mensagem com a data formatada.

d = input(' Me diga o dia do seu nascimento: ')
m = input(' Me diga o mês do seu nascimento: ')
a = input(' Me diga o ano do seu nascimento: ')

print(' Você nasceu no dia {}, no mês {}, no ano {}. Então sua data de nascimento é {}/{}/{}.'.format(d,m,a,d,m,a))

#Exercicio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input(' Digite um número: '))
d = (n * 2)
t = (n * 3)
r = n ** (1/2)
print(' O dobro de {} vale {}.\n O triplo de {} vale {}.\n A raiz quadrada de {} vale {:.2f}.'.format(n,d,n,t,n,r))

#Exercicio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média anual.

av1 = float(input(' Digite a sua primeira nota: '))
av2 = float(input(' Digite a sua segunda nota: '))
av3 = float(input(' Digite a sua terceira nota: '))
av4 = float(input(' Digite a sua quarta nota: '))
av =(av1 + av2 + av3 + av4)/4
print(' A sua média é {}.'.format(av))
if av < 7:
    print(' Você reprovou. ESTUDE MAIS! ')
elif av >= 7:
    print(' Você passou de ano. PARABÉNS! ')

#Exercicio #046 - contagem regressiva

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print(' CABUUMM ')


