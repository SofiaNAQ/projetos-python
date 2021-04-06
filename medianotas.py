soma = 0
quant = 0
x = 0

alunos = int(input("Quantos alunos? "))
notas = list(range(alunos))

for i in notas:
	notas[i] = int(input("Digite uma nota: "))
	soma = soma + notas[i]

media = soma/10

while x < alunos:
	if notas[x] > media:
		quant += 1
	x+=1

print('A média é de:',media, 'e há',quant, 'alunos acima dela.')