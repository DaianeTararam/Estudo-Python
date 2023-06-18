'''Escreva um programa que leia duas notas de um aluno de programação. Em seguida, a média
ponderada, com pesos 2 e 3, respectivamente, deve ser calculada. Por fim, o programa deve
imprimir a média obtida.'''

nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))

media = (nota1 * 2 + nota2 * 3) / 5

print("Média = {:.2f}".format(media))



'''Cosntrua um programa que leia uma temperatura em fahrenheit e converta-a para
Celsius. sabe-se que: ºC = (ºF - 32)/1.8'''

fahr = int(input("Digite quantos graus está fazendo em Fahrenheit: "))

celsius = (fahr - 32) / 1.8
print("Os graus Celsius é de  = {:.2f}".format(celsius))

