#Minhas funções.py
valor_PI = 3.14
#As funções só retornam valor depois que usar a palavra chave return
def saudar():
    print ("Olá")

def saudar_aluno(nome):
    print("Olá, {}.".format(nome))

def calcula_dobro(numero):
    return 2 * numero

def calcula_dobro_triplo(numero):
    return 2 * numero, 3 * numero

def calcula_area_circulo():
    raio = 3
    return valor_PI * pow(raio, 2)

def calcula_comprimento_circulo():
    return 2 * valor_PI * 3

def retorna_maior_menor_media(L):
    menor = min(L)
    maior = max(L)
    media = sum(L) / len (L)
    return menor, maior, media
#   return min(L), max(L), sum(L) / len(L)

def calcula_dobroX_triploY(x, y):
    return 2 * x, 3 * y 

def calcula_IMC(peso, altura, nome = "Prezado(a) "):
    imc = peso / pow(altura, 2)
    return "{}, seu IMC é {:.2f}.".format(nome, imc)

def calcula_distancia_ponto(xA, yA, xB, yB):
    from math import sqrt
    return sqrt((xB - xA) ** 2 + (yB - yA) ** 2)