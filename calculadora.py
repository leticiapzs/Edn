while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        resultado = 0

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
        else:
            print("Erro: Operação inválida. Por favor, tente novamente.")
            continue

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        break

    except ValueError:
        print("Erro: Entrada não numérica. Por favor, digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Tente novamente.")