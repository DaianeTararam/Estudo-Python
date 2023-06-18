a = 1
b = -3
c = -10

delta = b* b -4 * a * c
if (delta > 0):
    print ("#1")
elif (delta == 0):
    print("#2")
elif (delta < 0):
    print("#3")
else:
    print("#4")


ALUNOS={21: ["Ana", 1.7],
        14: ["Carlos", 1.82],
        46: ["Henrique", 1.57]
        }
DADOS = ALUNOS.get(46)
print (DADOS[1])



def calcula_area(base, altura):
    area = (base * altura)

print(calcula_area(5, 2))