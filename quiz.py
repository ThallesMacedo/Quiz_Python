print("Bem vindo ao quiz, meu projeto de desenvolvimento")
resposta = input("Quer começar? [SIM/NÃO] ") #RECEBENDO A RESPOSTA DO USUARIO
resposta_usuario = resposta.upper() #TRATANDO A RESPOSTA DEIXANDO A LETRA MAIUSCULA

print(resposta_usuario)

if resposta_usuario != "SIM":
    print("Encerrando o Quiz, até mais...")
    quit()

print("Começando...")