import string

def eh_palindromo(frase: str) -> str:
  caracteres_para_remover = string.punctuation + " "
  frase_limpa = ""
  for char in frase.lower():
    if char not in caracteres_para_remover:
      frase_limpa += char
  
  if frase_limpa == frase_limpa[::-1]:
    return "Sim"
  else:
    return "Não"

entrada_usuario = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
resultado = eh_palindromo(entrada_usuario)
print(f"A entrada '{entrada_usuario}' é um palíndromo? {resultado}")