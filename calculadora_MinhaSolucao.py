def impressaoInicial():
    print("*************** Python Calculator *************** \n")
    print("Selecione o número da opção desejada: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão \n")


def calculo():
    opcaodesejada = input("Digite sua opção (1/2/3/4): ")

    if opcaodesejada == "1":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"O resultado de {num1} + {num2} = {soma}")

    elif opcaodesejada == "2":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        subtracao = num1 - num2
        print(f"O resultado de {num1} - {num2} = {subtracao}")

    elif opcaodesejada == "3":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        multiplicacao = num1 * num2
        print(f"O resultado de {num1} * {num2} = {multiplicacao}")

    elif opcaodesejada == "4":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        divisao = num1 / num2
        print(f"O resultado de {num1} / {num2} = {divisao}")

    else:
        print("Opção inválida! Digite 1, 2, 3 ou 4.")


impressaoInicial()
calculo()
