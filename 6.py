lista = []
lista.append("Thiago")
lista.append("Gabriel")
lista.append("Elias")
lista.append("Augusto")
lista.append("Giordano")
lista.append("Lucas")
lista.append("Nicolas")

lista_nova = lista.copy()

verif = input("Digite um nome para verificarmos qual a posição nele na lista. ")

print("{} está na posição {} da lista.".format (verif, lista_nova.index(verif)))