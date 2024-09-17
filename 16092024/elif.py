nomevendedor = input("nome do vendedor ")
valorvenda = float(input("informe o valor da venda "))
if valorvenda>50000:
    comissao = valorvenda * 0.12
elif valorvenda >= 30000 and valorvenda <= 50000:
    comissao = valorvenda * 0.095
elif valorvenda >= 0 and valorvenda < 30000:
    comissao = valorvenda * 0.07
else:
    print("valor venda incorreto, deve ser maior que zero")
if valorvenda >= 0:
    print("A comissão do vendedor é", comissao)
