'''lindas = []
lindas.append("Fátima Bernardes")     #0
lindas.append("Paolla de Oliveira")   #1
lindas.append("Sheron Menezes")       #2
lindas.insert(1, "Iza")

for elas in range(4):
    print(lindas[elas])'''

lindas = []

while True:
    nome = input("Digite o nome de uma linda: ")
    lindas.append(nome)

    resp = input("Deseja continuar? [S│N] ")
    if resp.upper() == "N":
        break

for nome in lindas:
    print(nome)
    