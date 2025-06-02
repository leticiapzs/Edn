import requests

def obter_perfil_usuario_aleatorio():
    url = "https://randomuser.me/api/?inc=name,email,location"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        usuario = dados['results'][0]

        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("Perfil de Usuário Aleatório:")
        print(f"  Nome: {nome_completo}")
        print(f"  Email: {email}")
        print(f"  País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao contatar a API: {e}")
    except (KeyError, IndexError):
        print("Erro ao processar os dados do usuário. Formato inesperado da API.")

if __name__ == "__main__":
    obter_perfil_usuario_aleatorio()