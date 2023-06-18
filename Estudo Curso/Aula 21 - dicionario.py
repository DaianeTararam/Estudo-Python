#Ordenando o dicionario com base nos valores
from operator import itemgetter
contato = {"@camilaqueiroz": 1.77,
           "@paollaoliveira": 1.70,
           "@sheronmenezes": 1.67,
           "@bruna_ionica": 1.70}

for insta, altura in sorted(contato.items(),key=itemgetter(1)):
    print("{} --> {:.2f}m".format(insta, altura))
print(" ")

#Ordenando de forma reversa
for insta, altura in sorted(contato.items(),key=itemgetter(1), reverse = True):
    print("{} --> {:.2f}m".format(insta, altura))