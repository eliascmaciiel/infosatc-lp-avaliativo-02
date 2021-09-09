#Exercício 7


#a)

#Lista A
lista_filmes = []
lista_filmes.append("Harry Potter")
lista_filmes.append("Velozes e Furiosos")

print("Lista de filmes: {}".format(lista_filmes))
print("")



#Lista B
lista_jogos = []
lista_jogos.append("Counter Strike")
lista_jogos.append("FIFA")

print("Lista de jogos: {}".format(lista_jogos))
print("")



#Lista C
lista_livros = []
lista_livros.append("Diário de um Banana")
lista_livros.append("Volta ao mundo em 80 dias")

print("Lista de livros: {}".format(lista_livros))
print("")



#Lista D
lista_esportes = []
lista_esportes.append("Futebol")
lista_esportes.append("Vôlei")

print("Lista de esportes: {}".format(lista_esportes))
print("")



#b)

lista_geral = lista_filmes + lista_jogos + lista_livros + lista_esportes

print("Lista Geral: {}".format(lista_geral))
print("")



#c)

info = int(input("A lista de livros tem {} itens, escreva qual item deseja ver. ".format(len(lista_livros))))

info = info - 1   

print (lista_livros[info])
print("")

#d)

print(lista_esportes)

rem = int(input("A lista de esportes tem {} itens, escreva qual item deseja remover. ".format(len(lista_esportes))))

rem = rem - 1

del lista_esportes[rem]
print("Nova lista de esportes: {}".format(lista_esportes))

#e)

lista_geral.append("Disciplinas")

print(lista_geral)