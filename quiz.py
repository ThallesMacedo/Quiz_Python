print("Bem vindo ao quiz, meu projeto de desenvolvimento")
resposta = input("Quer começar? [SIM/NÃO] ") #RECEBENDO A RESPOSTA DO USUARIO
resposta_usuario = resposta.upper() #TRATANDO A RESPOSTA DEIXANDO A LETRA MAIUSCULA

print(resposta_usuario)

if resposta_usuario != "SIM":
    print("Encerrando o Quiz, até mais...")
    quit()
score =  0

print("Começando...")

#1º Pergunta
print("Para que serve o Git? \n (A) Editar imagens \n (B) Controlar versões de código \n (C) Criar jogos \n")
r1 = input("Resposta: ")
r1maiuscula = r1.upper()

if r1maiuscula == "B":
    print("Correto!")
    score = score +1
else:
    print("Incorreto!")

#2º Pergunta
print("Qual comando inicia um repositório Git? \n (A) git start \n (B) git init \n (C) git create \n")
r2 = input("Resposta: ")
r2maiuscula = r2.upper()

if r2maiuscula == "B":
    print("Correto!")
    score = score +1
else:
    print("Incorreto!")

#3º Pergunta
print("Qual comando mostra o estado dos arquivos? \n (A) git log \n (B) git status \n (C) git check \n")
r3 = input("Resposta: ")
r3maiuscula = r3.upper()

if r3maiuscula == "B":
    print("Correto!")
    score = score +1
else:
    print("Incorreto!")

#4º Pergunta
print("Qual comando adiciona arquivos para o commit? \n (A) git add \n (B) git push \n (C) git pull \n")
r4 = input("Resposta: ")
r4maiuscula = r4.upper()

if r4maiuscula == "A":
    print("Correto!")
    score = score +1
else:
    print("Incorreto!")

#5º Pergunta
print("Git e GitHub são a mesma coisa? \n (A) Sim \n (B) Não \n (C) Às vezes \n")
r5 = input("Resposta: ")
r5maiuscula = r5.upper()

if r5maiuscula == "B":
    print("Correto!")
    score = score +1
else:
    print("Incorreto!")

print(f"Sua pontuação foi de: {score} pontos")