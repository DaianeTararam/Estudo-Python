##for i in range[5]
##   nome = input("Nome: ")
##    t    = float(input("Tempo: "))
##
##   nadadoras.append(nome)
##   tempo.append(t)

#índices --> 0        1            2           3        4
nadadoras = ["Luisa", "Alexandra", "Victória", "Karol", "Beatriz"]
tempo     = [17.3   , 15         , 13        , 19     , 16]

#Informar o nome da melhor e da pior nadadora
#Sintaxe: nome_lista(elemento_procurado)

indice_melhor_tempo = tempo.index(min(tempo))
indice_pior_tempo   = tempo.index(max(tempo))

print("Melhor nadadora é {}".format(nadadoras[indice_melhor_tempo]))
print("Pior nadadora é {}".format(nadadoras[indice_pior_tempo]))