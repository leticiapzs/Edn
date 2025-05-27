contador_pares = 0
contador_impares = 0

print("--- Verificador de Pares e Ímpares ---")
print("Digite números inteiros. Para encerrar, digite 'fim'.")
print("-" * 40)

while True:
    entrada_usuario = input("Digite um número: ")

    if entrada_usuario.lower().strip() == 'fim':
        break

    try:
        numero = int(entrada_usuario)

        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            contador_pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            contador_impares += 1

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

print("-" * 40)
print("Programa finalizado.")
print(f"Total de números pares inseridos: {contador_pares}")
print(f"Total de números ímpares inseridos: {contador_impares}")