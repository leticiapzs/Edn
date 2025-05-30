def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
  """Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

  Parâmetros:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

  Retorna:
    float: O valor da gorjeta calculada.
  """
  if valor_conta < 0 or porcentagem_gorjeta < 0:
    raise ValueError("O valor da conta e a porcentagem da gorjeta não podem ser negativos.")
  
  gorjeta = (valor_conta * porcentagem_gorjeta) / 100
  return gorjeta