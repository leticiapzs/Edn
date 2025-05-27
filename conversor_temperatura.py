valor = float(input("Digite a temperatura: "))
origem = input("Qual a unidade de origem (C, F, K)? ").upper()
destino = input("Para qual unidade deseja converter (C, F, K)? ").upper()

resultado = 0

if origem == destino:
  resultado = valor

elif origem == 'C':
  if destino == 'F':
    resultado = (valor * 9/5) + 32
  elif destino == 'K':
    resultado = valor + 273.15

elif origem == 'F':
  if destino == 'C':
    resultado = (valor - 32) * 5/9
  elif destino == 'K':
    resultado = (valor - 32) * 5/9 + 273.15

elif origem == 'K':
  if destino == 'C':
    resultado = valor - 273.15
  elif destino == 'F':
    resultado = (valor - 273.15) * 9/5 + 32

if resultado != 0 or origem == destino:
    print(f"O resultado é {resultado:.2f} {destino}")
else:
    print("Unidades de origem ou destino inválidas.")