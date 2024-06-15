def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

print("---------------------")
print("Calculadora em Python")
print("---------------------")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("")

escolha = input("Digite a operação que você deseja realizar: ")
n1 = float(input("Digite seu primeiro número: "))
n2 = float(input("Digite seu segundo número: "))

def formatacao(n):
    if n.is_integer():
        return int(n)
    return n

if escolha == '1':
    resultado = adicao(n1, n2)
    print(f'{formatacao(n1)} + {formatacao(n2)} = {formatacao(resultado)}')
elif escolha == '2':
    resultado = subtracao(n1, n2)
    print(f'{formatacao(n1)} - {formatacao(n2)} = {formatacao(resultado)}')
elif escolha == '3':
    resultado = multiplicacao(n1, n2)
    print(f'{formatacao(n1)} * {formatacao(n2)} = {formatacao(resultado)}')
elif escolha == '4':
    resultado = divisao(n1, n2)
    if isinstance(resultado, str):
        print(resultado)  # Erro de divisão por zero
    else:
        print(f'{formatacao(n1)} / {formatacao(n2)} = {formatacao(resultado)}')
else:
    print("Opção inválida.")