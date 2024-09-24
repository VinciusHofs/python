"""
nota1 = float(input("informe a primeira nota "))
nota2 = float(input("informe a segunda nota "))
nota3 = float(input("informe a terceira nota "))
nota4 = float(input("informe a quarta nota "))

media = (nota1+nota2+nota3+nota4)/4
if media >=7:
    print("Aprovado!")
else:
    print("Aluno em exame!")
    notaexame = float(input("informe a nota do exame "))
    media2 = (media + notaexame)/2
    if media2 >=5:
        print("Aprovado")
    else:
        print("Reprovado")
"""

"""
horasmes = int(input("informe a quantidade de horas trabalhadas no mês "))
sh = float(input("informe o valor da hora "))
if horasmes  > 200:
    horaextra = horasmes - 200
    salariototal = sh*200 + horaextra*sh*1.5
else: 
    salariototal = horasmes * sh

print("salario total", salariototal)
"""

"""
a = float(input("informe lado do triângulo "))
b = float(input("informe lado do triângulo "))
c = float(input("informe lado do triângulo "))

if a<(b+c) and b<(a+c) and c<(b+a):
    print ("é triângulo")
    if a==b==c:
        print("equilátero")
    elif a!=b!=c:
        print("escaleno")
    else:
        print("isósceles")
else:
    print("medidas não formam triângulo")
"""


sm = float(input("informe o valor do salário mínimo "))
st = float(input("informe o salário bruto "))
quantidadesm = st/sm
if quantidadesm<3:
    reajuste = 0.5
elif quantidadesm>=3 and quantidadesm<=10:
    reajuste = 0.2
elif quantidadesm>10 and quantidadesm<=20:
    reajuste = 0.15
else:
    reajuste = 0.1
novosal = st + st*reajuste
print("novo salário", novosal)