while True:
    senha = input("Crie uma senha ou digite 'sair' para encerrar: ")

    if senha.lower().strip() == 'sair':
        print("Encerrando o programa.")
        break

    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break
            
    if len(senha) < 8:
        print("❌ Erro: A senha deve ter pelo menos 8 caracteres.")
    elif not tem_numero:
        print("❌ Erro: A senha deve conter pelo menos um número.")
    else:
        print("✅ Senha forte criada com sucesso!")
        break