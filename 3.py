print("Nesse programa você irá digitar 5 números e iremos retornar a soma deles.")

n1 = int(input("Digite o primeiro valor."))

n2 = int(input("Digite o segundo valor."))

n3 = int(input("Digite o terceiro valor."))

n4 = int(input("Digite o quarto valor."))

n5 = int(input("Digite o quinto valor."))
 
lista = [n1, n2, n3, n4, n5]

soma = sum(lista)

print("Números: {}".format(lista))

print ("Soma: {}".format(soma))