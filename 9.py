print("Nesse programa você irá digitar 10 números e iremos retornar na ordem inversa.")

num1 = int(input("Digite o primeiro número."))

num2 = int(input("Digite o segundo número."))

num3 = int(input("Digite o terceiro número."))

num4 = int(input("Digite o quarto número."))

num5 = int(input("Digite o quinto número."))

num6 = int(input("Digite o sexto número."))

num7 = int(input("Digite o sétimo número."))

num8 = int(input("Digite o oitavo número."))

num9 = int(input("Digite o nono número."))

num10 = int(input("Digite o décimo número."))

lista = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

print ("Lista em ordem: {}".format((list (sorted (lista)))))