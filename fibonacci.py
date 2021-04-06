qnt = int(input("Escreva quantos valores você quer que apareçam na sequência: "))

vetor = list(range(qnt))
vetor[0] = 0
vetor[1] = 1

i = 1
while i < len(vetor)-1:
	vetor[i+1] = vetor[i]+vetor[i-1]
	i+=1
print(vetor)