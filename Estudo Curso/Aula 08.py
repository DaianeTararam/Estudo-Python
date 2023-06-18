print("COVID-19")

suspeitos = 0
num_pac = int(input("Informe a quantidade de pacientes:"))
cont = 0
while cont < num_pac:
    tosse = int(input("Está com tosse? \n1. Sim \n2. Não \nResp.: "))
    febre = int(input("Está com febre? \n1. Sim \n2. Não \nResp.: "))
    resp = int(input("Dificuldade para respirar? \n1. Sim \n2. Não \nResp.: "))

    if tosse ==1 and febre == 1 and resp ==1:
       suspeitos += 1 #suspeitos = suspeitos + 1

    cont += 1

print("Suspeitos de COVID-19: {}".format(suspeitos))

