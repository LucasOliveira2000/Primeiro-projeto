
#Exercicio #047 - contagem de pares
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for n in range(2 , 50, +2):
    print(n, end=' ')
print(' Fim ')

#Exercicio 049 - tabuada v2.0
#Refaça o exercicio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
#utilizando um laço for

num = int(input(' Digite um número: '))
for c in range(1, 11):
    print(' {} x {:2} = {}'.format(num , c, num*c,))
print(' Fim ')


#Exercício #057 - Validação de Dados
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str(input(' Informe seu sexo : [M/F] ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input(' Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(' Sexo {} registrado com sucesso.'.format(s))
i = int(input(' Informe a sua idade : '))
while i >100 :
    i = int(input(' Idade inválida. Por favor, digite novamente: '))
print(' Idade {} anos registrada com sucesso.'.format(i))
