print("Bem vindo ao quiz, meu projeto de desenvolvimento")
resposta = input("Quer começar? [SIM/NÃO] ") #RECEBENDO A RESPOSTA DO USUARIO
resposta_usuario = resposta.upper() #TRATANDO A RESPOSTA DEIXANDO A LETRA MAIUSCULA

print(resposta_usuario)

if resposta_usuario != "SIM":
    print("Encerrando o Quiz, até mais...")
    quit()

print("Começando...")

#1º Pergunta
print("Para que serve o Git? \n (A) Editar imagens \n (B) Controlar versões de código \n (C) Criar jogos \n")
r1 = input("Resposta: ")

if r1 == "A":
    print("Correto!")
else:
    print("Incorreto!")

#2º Pergunta
print("Qual comando inicia um repositório Git? \n (A) git start \n (B) git init \n (C) git create \n")
r2 = input("Resposta: ")

if r2 == "B":
    print("Correto!")
else:
    print("Incorreto!")

#3º Pergunta
print("Qual comando mostra o estado dos arquivos? \n (A) git log \n (B) git status \n (C) git check \n")
r3 = input("Resposta: ")

if r3 == "B":
    print("Correto!")
else:
    print("Incorreto!")

#4º Pergunta
print("Qual comando adiciona arquivos para o commit? \n (A) git add \n (B) git push \n (C) git pull \n")
r4 = input("Resposta: ")

if r4 == "A":
    print("Correto!")
else:
    print("Incorreto!")

#5º Pergunta
print("Git e GitHub são a mesma coisa? \n (A) Sim \n (B) Não \n (C) Às vezes \n")
r5 = input("Resposta: ")

if r5 == "B":
    print("Correto!")
else:
    print("Incorreto!")