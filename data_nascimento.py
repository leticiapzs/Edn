import datetime

def calcular_idade_em_dias(ano_nascimento: int) -> int:
  """
  Calcula a idade de uma pessoa em dias, considerando a data atual.
  O cálculo é feito a partir de 1º de Janeiro do ano de nascimento fornecido
  até a data de hoje.

  Parâmetros:
  ano_nascimento (int): O ano de nascimento da pessoa.

  Retorna:
  int: O número de dias vividos desde 1º de Janeiro do ano de nascimento até hoje.

  Levanta:
  TypeError: Se o ano_nascimento não for um inteiro.
  ValueError: Se o ano_nascimento for inválido (ex: futuro, < 1, ou > 9999).
  """
  if not isinstance(ano_nascimento, int):
    raise TypeError("O ano de nascimento deve ser um número inteiro.")

  hoje = datetime.date.today() # Data de hoje: 2025-05-30

  if ano_nascimento > hoje.year:
    raise ValueError("O ano de nascimento não pode ser no futuro.")
  
  if not (1 <= ano_nascimento <= 9999):
    raise ValueError(f"Ano de nascimento inválido ({ano_nascimento}). Deve estar entre 1 e 9999.")

  data_nascimento_referencia = datetime.date(ano_nascimento, 1, 1)
  
  diferenca_em_dias = (hoje - data_nascimento_referencia).days
  
  return diferenca_em_dias

# --- Seção de interação com o usuário ---
if __name__ == "__main__":
  try:
    ano_digitado_pelo_usuario = input("Digite o ano de nascimento da pessoa (ex: 1990): ")
    # Tenta converter a entrada para um número inteiro
    ano_nascimento_usuario = int(ano_digitado_pelo_usuario)
    
    # Chama a função para calcular a idade em dias
    idade_em_dias_resultado = calcular_idade_em_dias(ano_nascimento_usuario)
    
    data_atual_formatada = datetime.date.today().strftime("%d/%m/%Y") # Data atual formatada
    
    print(f"\nConsiderando a data de hoje ({data_atual_formatada}), uma pessoa nascida em (1º de Janeiro de) {ano_nascimento_usuario} possui {idade_em_dias_resultado} dias de vida.")

  except ValueError as ve:
    # Captura erros de conversão (se o usuário não digitar um número)
    # ou erros da lógica da função (ano inválido)
    print(f"Erro: {ve}. Por favor, insira um ano válido.")
  except TypeError as te:
    # Captura erros de tipo, embora o int() já possa levantar ValueError antes.
    print(f"Erro de tipo: {te}.")
  except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")