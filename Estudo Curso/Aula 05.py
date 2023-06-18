'''Construa um progama que receba a altura e o sexo de uma pessoa. Baseado nas formulas abaixo:
- Homens: (72.7 * altura) - 58.0
- Mulheres: (62.1 * altura) - 44.7'''

sexo = input("Informe p seu sexo [M / F]: ")
altura = float(input("Digite a sua estatura: "))

if sexo.upper() == "F":
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f} Kg".format(peso))
elif sexo.upper() == "M":
    peso = (72.7 * altura) - 58.0
    print("Seu peso ideal é {:.2f} Kg".format(peso))
else:
    print("Opção de sexo inválida!")
