'''Construa um programa que receba o sexo e a idade de alunos de uma turma. considere que o usuário não sabe a quantidade de alunos na turma.
Ao fim, o programa deve exibir a quantidade de rapazes acima de 10 anos,
e a média de idades das moças. Para encerrar o programa, informe uma idade negativa.'''

sexo = input("Informe o sexo do aluno [F│M]: ")
idade = int(input("Informe a idade: "))
rapazes_maiores = 0
soma_idades_mocas = 0
mocas = 0

while True:
    if idade < 0:
        break

    if sexo.upper() == "M":
        if idade > 18:
            rapazes_maiores += 1
    elif sexo.upper() == "F":
        soma_idades_mocas += idade
        mocas += 1
    else:
        print("Opção de sexo inválida.")
media = 0
if mocas > 0:
    media = soma_idades_mocas / mocas
 

print("Rapazes acima de 18 anos: {}".format(rapazes_maiores))
print("Média de idade das moças: {}".format(media))
