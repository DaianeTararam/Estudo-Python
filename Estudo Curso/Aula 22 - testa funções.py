from Aula22 import *

'''saudar()
saudar_aluno("Você")
print(calcula_dobro(3))
dobro, triplo = calcula_dobro_triplo(3)
print(dobro)
print (triplo)
print(calcula_area_circulo())
print(calcula_comprimento_circulo())'''

'''L= [7, 2, 3, 4]
menor, maior, media = retorna_maior_menor_media(L)
print("Menor elemento: {}".format(menor))
print("Maior elemento: {}".format(maior))
print("Media dos elementos: {}".format(media))'''

'''varX = 5
varY = 7
dobroX, triploY = calcula_dobroX_triploY(varX, varY)
print("Dobro de {} = {}".format(varX, dobroX))
print("Triplo de {} = {}".format(varY, triploY))'''

print(calcula_IMC(84, 1.82))

xA = float(input("Digite  o valor da coordenada X do ponto A: "))
yA = float(input("Digite  o valor da coordenada Y do ponto A: "))
xB = float(input("Digite  o valor da coordenada X do ponto A: "))
yB = float(input("Digite  o valor da coordenada Y do ponto A: "))

dAB = calcula_distancia_ponto(xA, yA, xB, yB)
print ("A distância entre os pontos A e B é {:.2f}.".format(dAB))