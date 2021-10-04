import random
    print("-//-//-//-//-//-//-//-//-//-//-//")
    print("Bem vindo ao jogo de Adivinhação!")
    print("-//-//-//-//-//-//-//-//-//-//-//")

    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    pontos = 100


    print("Selecione um nível de dificuldade: ")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Nível de dificuldade: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print(f"Tentativa {rodada} de {total_de_tentativas}, {pontos} pontos")
        chute = int(input("Insira um número entre 1 e 50: "))
        print("Número inserido: ", chute)

        if(chute < 1 or chute > 100):
            print("Insira um número entre 1 e 50!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos")
            break
        else:
            if(maior):
                print("Tente novamente! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Tente novamente! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")
