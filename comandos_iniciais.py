print("Hello, World!") #Texto

print(3 + 4) #Soma

print("Olá, " + "mundo!") #Concatenação

input("Digite algo: ") #Entrada de dados

print("Olá, " + input("Digite seu nome: ") + "!") #Entrada de dados e concatenação

# Criar um programa que o usuário digita o nome e ele conta quantas letras tem o nome

nome = input("Digite seu nome: ")
print(f"Seu nome tem {len(nome)} letras.") #len conta o número de caracteres em uma string

# Criar um programa que o usuário digita dois números e o programa mostra a soma, subtração, multiplicação e divisão desses números

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
if num2 != 0:
    print(f"Divisão: {num1 / num2}")
else:    print("Divisão por zero não é permitida.")