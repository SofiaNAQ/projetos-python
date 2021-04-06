#Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo
#que permita a entrada das seguintes informações: a) o número total de mercadorias no estoque; b) o
#valor de cada mercadoria. Ao final imprimir o valor total em estoque e a média de valor das
#mercadorias
contador = 0
soma = 0
media = 0

total = int(input('Digite o número de mercadorias: '))
while contador < total:
    valor = int(input('Digite o preço da mercadoria: '))
    soma = soma + valor
    contador = contador + 1
else:
    media = soma/total
    print('A média de preço é: ',media)
