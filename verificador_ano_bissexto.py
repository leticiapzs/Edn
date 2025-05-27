try:
  ano = int(input("Digite um ano para verificar: "))

  if ano <= 0:
    print("Por favor, digite um ano válido (maior que zero).")
  else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
      print(f"Sim, o ano {ano} é bissexto.")
    else:
      print(f"Não, o ano {ano} não é bissexto.")

except ValueError:
  print("Entrada inválida. Por favor, digite um número de ano válido.")