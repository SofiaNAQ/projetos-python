salario_final_dia: int
salario_final_mes: int
salario_final_hora: int 
salario_final_semana: int

print('=== Esta é uma calculadora freelancer ===')
nivel_servico = input("Você é: \n 1. Sênior \n 2. Pleno \n 3. Júnior")
salario_ideal = int(input("Quanto você deseja ganhar? \n"))
if salario_ideal < 400:
    print('Digite um número maior que 400!')

horas = int(input("Quantas horas trabalha por dia? \n"))
dias_trabalho = int(input("Quantos dias trabalha por semana? \n"))
carga_mensal = (horas*dias_trabalho)*4
resposta = input('Possui algum gasto adicional? S/N \n')

if resposta == 'S' or resposta == 's':
    gasto_add = int(input("Digite o valor do gasto adicional: \n"))
    salario_ideal = salario_ideal + gasto_add
    salario_final_hora = salario_ideal/carga_mensal
    salario_final_dia = salario_ideal/(dias_trabalho*4)
    salario_final_semana = salario_ideal/4
    salario_final_mes = salario_ideal
    print('O valor do seu trabalho por hora é de: ', salario_final_hora, '\n Por dia é de: ',salario_final_dia, '\n Por semana é de: ',salario_final_semana, 
    'Por mês é de: ', salario_ideal)
else:
    salario_final_hora = salario_ideal/carga_mensal
    salario_final_dia = salario_ideal/(dias_trabalho*4)
    salario_final_semana = salario_ideal/4
    salario_final_mes = salario_ideal
    print('O valor do seu trabalho por hora é de: ', salario_final_hora, '\n Por dia é de: ',salario_final_dia, '\n Por semana é de: ',salario_final_semana, 
    'Por mês é de: ', salario_ideal)