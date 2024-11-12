"""
soma = 0
a = int(input('informe um valor: '))
b = int(input('informe outro valor: '))

if a > b:
    a,b = b,a # Esta estrutura me permite trocar os valores de a e b sem criar uma variável auxiliar

for i in range (a+1,b):
    if i%2==0:
        soma = soma + i**3 
print('soma dos pares ao cubo é ',soma)
"""

"""
valor = float(input('informe o valor: '))

for i in range(1,13):
    juros = round(valor*0.005,2)
    valor = juros + valor
    print('rendimento no mês', i, '=', '%.2f' % valor) 
"""


div = 0
numero = int(input('informe um número: '))

for i in range(numero):
    if i%2==0:
        div += i
if div == 0:
    print('é primo')
else: 
    print('não é primo')