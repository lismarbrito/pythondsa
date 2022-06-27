print("*************** Python Calculator *************** \n")


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


print("\n Selecione o número da opção desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão \n")

opcaodesejada = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if opcaodesejada == "1":
    print("\n")
    print(f"O resultado de {num1} + {num2} = ", adicao(num1, num2))
    print("\n")

elif opcaodesejada == "2":
    print("\n")
    print(f"O resultado de {num1} - {num2} = ", subtracao(num1, num2))
    print("\n")

elif opcaodesejada == "3":
    print("\n")
    print(f"O resultado de {num1} - {num2} = ", multiplicacao(num1, num2))
    print("\n")

elif opcaodesejada == "4":
    print("\n")
    print(f"O resultado de {num1} - {num2} = ", divisao(num1, num2))
    print("\n")
else:
    print("Opção inválida! Digite 1, 2, 3 ou 4.")
