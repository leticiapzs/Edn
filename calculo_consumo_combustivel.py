distancia = float(input("Digite a distância percorrida (km): "))
combustivel = float(input("Digite a quantidade de combustível gasto (litros): "))

consumo_medio = distancia / combustivel

print(f"\nDistância percorrida: {distancia:.2f} km")
print(f"Combustível gasto: {combustivel:.2f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
