vetor = list(range(5))
aux = 0
c = 0

for i in vetor:
	vetor[i] = int(input("Digite um numero: "))
	
def ordena():
	for i in range(4):
		for i in range(4):
			if vetor[i] > vetor[i+1]:
				aux=vetor[i]
				vetor[i]=vetor[i+1]
				vetor[i+1]=aux
	return ordena()
				


#num = int(input("Digite outro número: "))
#vetor.append(num)

#for i in range(5):		
#	if vetor[i] > num:
#		aux = vetor[i]
#		vetor[i] = num
#		num = aux
		