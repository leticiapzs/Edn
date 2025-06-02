import random
import string

def gerar_senha(comprimento):
    if comprimento < 4:
        print("O comprimento da senha deve ser de pelo menos 4 caracteres para incluir todos os tipos de caracteres.")
        return None

    
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"

    
    senha_lista = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
    for _ in range(comprimento - 4):
        senha_lista.append(random.choice(todos_caracteres))

    
    random.shuffle(senha_lista)

    
    return "".join(senha_lista)

if __name__ == "__main__":
    try:
        comprimento_senha = int(input("Digite a quantidade de caracteres para a senha: "))
        senha_gerada = gerar_senha(comprimento_senha)
        if senha_gerada:
            print("Senha gerada:", senha_gerada)
    except ValueError:
        print("Por favor, digite um número válido para o comprimento da senha.")