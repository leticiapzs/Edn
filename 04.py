import requests

def consultar_cep():
    cep_input = input("Digite o CEP (apenas números): ").strip()

    if not cep_input.isdigit() or len(cep_input) != 8:
        print("CEP inválido. Por favor, digite 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep_input}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados_cep = response.json()

        if dados_cep.get("erro"):
            print(f"CEP {cep_input} não encontrado.")
            return

        print("\n--- Endereço Encontrado ---")
        print(f"CEP: {dados_cep.get('cep', 'N/A')}")
        print(f"Logradouro: {dados_cep.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados_cep.get('bairro', 'N/A')}")
        print(f"Cidade: {dados_cep.get('localidade', 'N/A')}")
        print(f"Estado: {dados_cep.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API ViaCEP: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    consultar_cep()