#Aqui foi estudado o comando break
print("COVID-19")

suspeitos = 0
while True:
    tosse = int(input("Está com tosse? \n1. Sim \n2. Não \nResp.: "))
    febre = int(input("Está com febre? \n1. Sim \n2. Não \nResp.: "))
    resp = int(input("Dificuldade para respirar? \n1. Sim \n2. Não \nResp.: "))

    if tosse ==1 and febre == 1 and resp ==1:
       suspeitos += 1 #suspeitos = suspeitos + 1

    resp = input("Ainda há pacientes a serem atendidos[S│N]? ")
    if resp.upper() =="N":
        break

print("Suspeitos de COVID-19: {}".format(suspeitos))

