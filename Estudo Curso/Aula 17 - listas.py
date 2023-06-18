produtos = []
while True:
    nome = input("Nome: ")
    produtos.append(nome)
    resp = input("Deseja continuar? [S│N]")
    if resp.upper() == "N":
        break

#produtos = ["Lápis", "Borracha", "Régua", "Apontador"]
'''qtde_elem = len(produtos)

for ind in range(qtde_elem):
    print ("{} --> {}".format(ind, produtos[ind]))'''

for indice, valor in enumerate(produtos):
    print ("{} --> {}".format(indice, valor))