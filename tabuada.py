valor = int(input("Digite um valor: "))
print("==== Tabuada do" , valor,"====")

contador = 0

while contador <= 10:
	res = contador * valor
	print (contador, "x", valor,"=",res)
	contador += 1
print("==== FIM ====")