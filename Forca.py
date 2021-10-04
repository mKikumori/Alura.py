 
    imprime_mensagem_inicial()
    palavra_secreta = define_palavra_secreta()
    palavra_acertada = formatacao_letras_secretas(palavra_secreta)

    enforcou = False
    acertou = False
    errou = 0

    print(palavra_acertada)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra:")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            sequencia = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    palavra_acertada[sequencia] = letra
                sequencia += 1
        else:
            errou += 1

        enforcou = errou == len(palavra_secreta)
        acertou = "_" not in palavra_acertada
        print(palavra_acertada)

    print("Fim de jogo")

    
    
    
    
    
   def imprime_mensagem_inicial():
    print("-//-//-//-//-//-//-//-//-//-//-//")
    print("   Bem vindo ao jogo de Forca!   ")
    print("-//-//-//-//-//-//-//-//-//-//-//")


def define_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def formatacao_letras_secretas(palavra_secreta):
    return ["_" for letra in palavra_secreta]
