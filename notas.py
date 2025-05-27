notas_da_turma = []

print("--- Sistema de Registro de Notas ---")
print("Digite as notas dos alunos (0 a 10).")
print("Para finalizar e calcular a média, digite 'fim'.")
print("-" * 35)

while True:
    entrada = input("Digite a próxima nota: ")

    if entrada.lower().strip() == 'fim':
        break

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            notas_da_turma.append(nota)
            print(f"Nota {nota:.1f} registrada com sucesso.")
        else:
            print("Atenção: A nota deve estar entre 0 e 10.")

    except ValueError:
        print("Atenção: Entrada inválida. Por favor, digite um número ou 'fim'.")

print("-" * 35)

if len(notas_da_turma) > 0:
    media = sum(notas_da_turma) / len(notas_da_turma)
    
    print("Registro finalizado.")
    print(f"Total de notas válidas inseridas: {len(notas_da_turma)}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada para calcular a média.")