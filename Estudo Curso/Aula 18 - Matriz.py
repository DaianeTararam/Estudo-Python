#como preencher uma Matriz
#    0   1
'''M = [
    [10, 2],    #0
    [21, 13],   #1
    [7, 9]      #2
]
print(M)'''

L1 = [10, 2]
L2 = [21, 13]
L3 = [7, 9]

M = [L1]
M.append(L2)
M.insert(2, L3)

print(M)

#Matriz aleatória
import random

while True:
    lin = int(input("Informe a quantidade de linhas da matriz: "))
    col = int(input("Informe a quantidade de colunas da matriz: "))
    if lin > 0 and col > 0:
        M = []                       
        for i in range(lin):  
            LINHA = []     
            for j in range(col):
                num = random.randint(1, 21)
                LINHA.append(num)
            M.append(LINHA)
        break

for i in range (lin):
    for j in range(col):
        print(M[i][j], end = " ")
    print(" ")