
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))


imc = peso / (altura * altura)


print(f"Seu IMC é: {imc:.2f}")


if imc < 18.5:
  print("Classificação: Abaixo do peso")
elif imc < 25:
  print("Classificação: Peso normal")
elif imc < 30:
  print("Classificação: Sobrepeso")
else:
  print("Classificação: Obeso")