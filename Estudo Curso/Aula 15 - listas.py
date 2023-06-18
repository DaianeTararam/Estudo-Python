alunos = ["Leticia"]                   #0
alunos.append("Henrique")              #1
alunos.append("Leticia")               #2
alunos.append("Heitor")                #3
alunos.insert(4, "Ana Clara")          #4
alunos.insert(5, "Paolla de Oliveira") #5
print(alunos)
#Remove o ultimo elemento se vazia (), ou remove o elemento escolhido (2)
'''alunos.pop()
print(alunos)'''
#Removendo apenas o primeiro elemento da lista:
#alunos.remove("Leticia"), nota-se que só remove o 1º e não todos 
#Para a remoção de todos segue o código abaixo
for nome in alunos:
    if nome == "Leticia":
        alunos.remove(nome)
print(alunos)
#Verificando se há um elemento na minha lista
if "Paolla de Oliveira" in alunos:
    print("She is great!!!")
#Remove todos os elementos da lista
alunos.clear()
print(alunos)