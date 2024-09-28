"""
a = float(input('Digite o valor de a: '))
if a == 0:
    print("O valor de a, deve ser diferente de 0")
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print("Sem raízes reais, a equação não é de segundo grau!")
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

        print("x1: {}, x2: {}".format(x1, x2))
"""

combustivel = input("Informe qual o combustível usado, alcool ou gasolina: ")
litros = float(input("Informe quantos litros foram abastecidos: "))

if litros <= 0:
    print("Quantidade inválida!")
    
elif combustivel == "alcool":
    valor_a = 2.90

    if litros <= 20:
        valor = (valor_a * litros) * 0.97
    else: 
        valor = (valor_a * litros) * 0.95
    print("O valor a ser pago é", valor)

elif combustivel == "gasolina":
    valor_g = 3.30

    if litros <= 20:
        valor = (valor_g * litros) * 0.96
    else:
        valor = (valor_g * litros) * 0.94
    print("O valor a ser pago é", valor)

else:
    print("Combustível inválido, selecione gasolina ou alcool")