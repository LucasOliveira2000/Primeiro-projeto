#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

'''print(' Alo Mundo. ')'''

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

'''informe_numero = float(input('Digite um número: '))
print(f' O número informado foi {informe_numero} ')'''

#Faça um Programa que peça dois números e imprima a soma.

'''numero1 = float(input(' Digite um número: '))
numero2 = float(input(' Digite outro número: '))
soma = numero1 + numero2
(print(f' A soma dos dois números é {soma}'))'''

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

'''nota1 = float(input(' Digite a sua primeira nota: '))
nota2 = float(input(' Digite a sua segunda nota: '))
nota3 = float(input(' Digite a sua terceira nota: '))
nota4 = float(input(' Digite a sua quarta nota: '))
soma = (nota1 + nota2 + nota3 + nota4)/4
print(f' A sua média é {soma}.')'''

#Faça um Programa que converta metros para centímetros.

'''metros = float(input(' Digite um valor em Metros: '))
conversao = metros * 100
print(' O valor em centímetros é {}'.format(conversao))'''

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#A = π r²
#se o diâmetro for igual a 4 cm, o raio será igual a 4 cm ÷ 2 = 2 cm

'''raio_do_circulo = float(input(' Me informe o raio do circulo: '))
raio = raio_do_circulo / 2
area = 3.14 * raio**2
print(f' O raio do circulo é {raio}. ')
print(f' A área desse circulo é {area}.')'''

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''raio_do_circulo = float(input(' Me informe o raio do circulo: '))
raio = raio_do_circulo / 2
area = 3.14 * raio**2
area2 = area**2
print(f' O raio do circulo é {raio}. ')
print(f' A área desse circulo é {area}.')
print(f' O dobro da área é {area2}. ')'''

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''salario_hora = float(input(' Digite quando você ganha por hora: '))
hora_trabalhada = float(input(' Digite as suas horas trabalhadas no mês: '))
mes = 30
salario = (salario_hora * hora_trabalhada) * mes
print(f'O seu sálario deveria é {salario}. ')'''

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).# °F.

'''graus = float(input(' Digite o grau Fahrenheit: '))
transforma = ((graus - 32) / 9) * 5
print = (f' A transformação em Celsius é {transforma}. ')'''

#Escrever um programa em Python para exibir os números de 1 até 50 na tela.

'''print("\n\t Imprimir os números de 1 até 50 : \n")
for num in range(1,51):
assim, a contagem inicial começa em 1 e termina em 50
            print(num)'''

#Crie um programa em Python que receba uma string como entrada e conte o número de dígitos e letras.

'''texto = input("Entre com uma string: ")
digitos=0
letras=0
for x in texto:
    if x.isdigit():
        digitos=digitos+1
    elif x.isalpha():
        letras=letras+1
    else:
        pass
print("Total de letras: ", letras)
print("Total de Digitos:", digitos)'''