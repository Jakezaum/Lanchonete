print("Seja bem-vindo(a) à Maluche Burguer!") #1ªIdentificação
print("------------------- Cardápio --------------------")
print("Código |         Produto         | Valor (R$)")
print("  100  |        X-Burguer        |    7,00")
print("  101  |        X-Salada         |    8,00")
print("  102  |          X-Egg          |    9,00")
print("  103  |      X-Calabresa        |    12,00")
print("  104  |        X-Bacon          |    12,00")
print("  105  |        X-Frango         |    14,00")
print("  106  |         X-Tudo          |    18,00")
print("  200  |    Refrigerante Lata    |    5,00")
print("  201  |     Refrigerante 2L     |    12,00")
print("  202  |       Suco 250mL        |    4,00")
print("  203  |          Água           |    2,00")
print("-------------------------------------------------")

RU4393710 = 0 #2ªIdentificação - Acumulador do preço dos pedidos
#Inicio do pedido
while True:
    item = int(input("Qual o código do produto desejado? "))
    if item != 100 and item != 101 and item != 102 and item != 103 and item != 104 and item != 105 and item != 106 and item != 200 and item != 201 and item != 202 and item != 203:
        print("O código inserido não existe. Tente novamente.")
        continue #se houver erro do cliente na escolha ele volta ao input item
#Códigos
    if item == 100:
        print("Você pediu um X-Burguer no valor de 7,00 R$.")
        RU4393710 += 7
    elif item == 101:
        print("Você pediu um X-Salada no valor de 8,00 R$.")
        RU4393710 += 8
    elif item == 102:
        print("Você pediu um X-Egg no valor de 9,00 R$.")
        RU4393710 += 9
    elif item == 103:
        print("Você pediu um X-Calabresa no valor de 12,00 R$.")
        RU4393710 += 12
    elif item == 104:
         print("Você pediu um X-Bacon no valor de 12,00 R$.")
         RU4393710 += 12
    elif item == 105:
        print("Você pediu um X-Frango no valor de 14,00 R$.")
        RU4393710 += 14
    elif item == 106:
        print("Você pediu um X-Tudo no valor de 18,00 R$.")
        RU4393710 += 18
    elif item == 200:
        print("Você pediu um Refrigerante Lata no valor de 5,00 R$.")
        RU4393710 += 5
    if item == 201:
        print("Você pediu um Refrigerante 2L no valor de 12,00 R$.")
        RU4393710 += 12
    elif item == 202:
        print("Você pediu um Chá Gelado no valor de 4,00 R$.")
        RU4393710 += 4
    elif item == 203:
        print("Você pediu uma Água no valor de 2,00 R$.")
        RU4393710 += 2
#Continuando
    print("Deseja pedir mais alguma coisa?\n1 - Sim\n2 - Não")
    at = int(input(">> "))
    if at == 1:
        continue #Caso o cliente queira seguir pedindo (1) ele volta a while
    else:
        print("O total a ser pago é: {},00 R$." .format(RU4393710))
        print("Agradecemos pelo seu pedido e preferência. Volte sempre!")
        break