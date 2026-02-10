# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite a porcentagem do bônus recebido: "))
# 4) Calcule o valor do bônus final
kpi = 1000 + salario + (salario * bonus)
# 5) Imprima cálculo do KPI para o usuário
print(kpi)
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome}, seu KPI é: {kpi:.2f}") # :.2f formata o número para 2 casas decimais
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?