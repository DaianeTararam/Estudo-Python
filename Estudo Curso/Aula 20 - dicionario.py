#utilizando dicionário
contato = {"@camilaqueiroz": "Camila Queiroz",
           "@paollaoliveira": "Paolla de Oliveira"}
print(contato["@paollaoliveira"])
print (contato.get("@paollaoliveira"))
print(" ")

#Ordenando os elementos do dicionário
for Instagram, nome in sorted(contato.items()):
    print("{} ---> {}".format(Instagram, nome))
print(" ")

#Incluindo um elemento no dicionário
contato.update({"@paollaoliveira": "Ok"})
contato.update({"@bruna.ionica": "Bruna Marquesine"})
print(contato)
print(" ")

#Descobrindo quantos elementos tem no dicionario 
print("Antes de incluir Sheron Menezes: {}".format(len(contato)))
contato.update({"@sheronmenezes": "Sheron Menezes"})
print("Depois de incluir Sheron Menezes: {}".format(len(contato)))
print(" ")

#Excluindo elementos de um dicionario 
backup = contato.copy()
print(backup)
print(" ")

#Excluindo o último elemento do dicionario
contato.popitem()
print(contato)
print(" ")

#Excluindo elemento com chave especifica
contato.pop("@sheronmenezes")
print(contato)
print(" ")

#Acessando chaves de um dicionario
for Insta in contato.keys():
    print(Insta)
print(" ")

#Acessando valores das chaves
for atriz in contato.values():
    print(atriz)
print(" ")

#Acessando os valores e as chaves
for Insta, atriz in contato.items():
    print("O instagram de {} é {}.".format(atriz, Insta))
print(" ")

#Localizando um elemento no dicionário
insta = input("Digite um instagram: ")
if insta in contato:
    print("Este instagram é de {}".format(contato.get(insta)))
else:
    print("Este instagram não existe.")
print(" ")
#Exemplo de buscas com lista
#             0                 1
instagram = ["@camilaqueiroz", "@paollaoliveira"]
nomes     = ["Camila Queiroz", "Paolla de Oliveira"]

indice = instagram.index("@paollaoliveira")
print(nomes[indice])
