idade_alunos = []

idade_alunos.append(17)
idade_alunos.append(23)
idade_alunos.append(19)
idade_alunos.append(22)
idade_alunos.append(19)

#Contando a quantidade de elementos da lista
print(len(idade_alunos))

#Houve quantas ocorrencias do elemento
print(idade_alunos.count(19))

#Encontrando o menor da lista
print("Menor idade: {}".format(min(idade_alunos)))

#Encontrando o maior elemento da lista
print("Maior idade: {}".format(max(idade_alunos)))

#calculando a soma dos elementos da lista
print("Soma das idades: {}".format(sum(idade_alunos)))

#Calculando a média
print("Média das idades: {}".format(sum(idade_alunos) / len(idade_alunos)))
