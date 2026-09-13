frase = 'Curso em Video Python'
print(frase[:6])
print(frase.upper())
print(frase.lower())
print(len(frase))
print(frase.replace('Python', 'C#'))
print('Curso' in frase)
print(frase.find('Video'))
print(frase.split())
print(frase.strip())

preço = float(input('Digite o preço: R$'))
novo = preço - (preço * 5 / 100)
print('O preço com 5% de desconto é R${:.2f}'.format(novo))

salario = float(input('Digite o salário: R$'))
novo_salario = salario + (salario * 15 / 100)
print('O salário com 15% de aumento é R${:.2f}'.format(novo_salario))

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km rodados? '))
preço_total = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(preço_total))