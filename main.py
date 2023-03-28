#Pedindo as notas do usuário
nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))
nota_4 = float(input("Digite sua quarta nota: "))

#Calculando a média
operação = float(nota_1 + nota_2 + nota_3 + nota_4) / 4

#Imprimindo resultado para o usuário
print("Sua média final é " + str(operação) + ".")