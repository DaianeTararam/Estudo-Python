#Criação de uma lista vazia
praias_RN = []

#Inclusão de elementos
#Forma 1
praias_RN = ["Pipa"]
#Forma 2
praias_RN.append("Maracajaú")
praias_RN.append("Genipabu")
#Forma 3
praias_RN.insert(2, "Ponta Negra")

#short está ordenando alfabeticaente
#reverse = True está ordenando alfabeticamente em ordem decrescente
praias_RN.sort(reverse = True) 

#a biblioteca radom e função shuffle serve para embaralhar a ordem
import random
random.shuffle(praias_RN)

for praia in praias_RN:
    print(praia)