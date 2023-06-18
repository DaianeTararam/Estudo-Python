numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))
numero3 = float(input("Digite o 3º número: "))

soma = numero1 + numero2
dobro = numero3 * 2

print(numero1)
print(numero2)
print("Soma = {}".format(soma))
#A função format permite que o resultado seja impresso entre as chaves.

print("Dobro = {:.2f}".format(dobro))
#:.2f aparece o resultado com apenas 2 casas decimais


#O resultado não é um cálculo, pois em python, o resultado foi transformado em string.
#Existem valores de conversão
#usando a função int, convertemos para inteiro e podemos calcular
