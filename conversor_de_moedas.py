valor_em_reais = float(input("Digite o valor em reais (R$): "))

taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

print(f"\nValor em reais: R$ {valor_em_reais:.2f}")
print(f"Valor em dólar: US$ {valor_em_dolar:.2f}")
print(f"Valor em euro: € {valor_em_euro:.2f}")
