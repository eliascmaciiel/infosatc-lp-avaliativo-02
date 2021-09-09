
lista = []
lista.append("Thiago")
lista.append("Gabriel")
lista.append("Elias")
lista.append("Augusto")
lista.append("Giordano")
lista.append("Lucas")
lista.append("Nicolas")

nome = input("Digite um nome para verificarmos se ele está na lista: ")


if (nome) in lista:
    print("Sim, está na lista!")
else:
    print("Não está na lista")