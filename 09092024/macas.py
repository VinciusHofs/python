macas = int(input("Informe a quantidade de maçãs desejadas "))
preco = 1
total = macas * preco
if macas >= 12:
    print(f"O total a ser pago é {total} reais pelas {macas} maçãs")
elif macas > 0:
    print(f"O total a ser pago é {total+(0.30*macas)} reais pelas {macas} maçãs")
else: 
    print(f"quantidade de maçãs não pode ser negativa")