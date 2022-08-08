"""
Pós-Graduação em Desenvolvimento de Sistemas com Python
             LÓGICA DE PROGRAMAÇÃO ESP
               MAPA - JOGO DA FORCA
       ALUNO: LEONARDO HENRIQUE MARIN KIST
"""


import random
import os

lista =[
    "PARALELEPIPEDO",
    "GRAMADO",
    "CARRO",
    "FERRARI",
    "MOTOCICLETA",
    "FUTSAL",
    "OTORINOLARINGOLOGISTA",
    "ESPIAO",
    "RAMBO",
    "METALLICA",
    "CALIPSO",
    "CHIMBINHA",
    "FORRO",
    "SAMBA",
    "MOZART",
    "BETHOVEN",
    "MAQUINA"
]

#FUNÇÃO PARA LIMPAR A TELA
def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#FUNÇÃO PARA CADA TELA DA FORCA
def tela(erros, tentativas, letras):
    if erros == 0:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||          ERROS: " + str(erros))
        print("||          LETRAS ESCOLHIDAS: " + letras)
        print("||          ")
        print("||          A forca já está montada!")
        print("||          ")
        print("||          ")

    if erros == 1:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||   (_)    ERROS: " + str(erros))
        print("||          LETRAS ESCOLHIDAS: " + letras)
        print("||          ")
        print("||          Os preparativos estão sendo feitos!")
        print("||          ")
        print("||          ")

    if erros == 2:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||   (_)    ERROS: " + str(erros))
        print("||    |     LETRAS ESCOLHIDAS: " + letras)
        print("||    |     ")
        print("||          Seus minutos estão contados!")
        print("||          ")
        print("||          ")

    if erros == 3:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||   (_)    ERROS: " + str(erros))
        print("||    |     LETRAS ESCOLHIDAS: " + letras)
        print("||    |     ")
        print("||   /      Cada segundo mais próximo!")
        print("||  /       ")
        print("||          ")

    if erros == 4:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||   (_)    ERROS: " + str(erros))
        print("||    |     LETRAS ESCOLHIDAS: " + letras)
        print("||    |     ")
        print("||   / \    Começando a contagem regressiva... 3")
        print("||  /   \   ")
        print("||          ")

    if erros == 5:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||   (_)    ERROS: " + str(erros))
        print("||   /|     LETRAS ESCOLHIDAS: " + letras)
        print("||  / |     ")
        print("||   / \    Parece que já era pra você... 2")
        print("||  /   \   ")
        print("||          ")

    if erros == 6:
        limpar_tela()
        print(20 * "+" + "JOGO DA FORCA" + 20 * "+")
        print("========    TENTATIVAS: " + str(tentativas))
        print("||   (_)    ERROS: " + str(erros))
        print("||   /|\    LETRAS ESCOLHIDAS: " + letras)
        print("||  / | \   ")
        print("||   / \    Quase enforcado, se errar, perdeu!... 1")
        print("||  /   \   ")
        print("||          ")
       
    if erros == 7:
        limpar_tela()
        print("||                                                          ||")
        print("|| GGGGGG  AAAAA  MM   MM  EEEE   OOOOO V     V  EEEE RRRR  ||")
        print("|| G       A   A  M M M M  E      O   O V     V  E    R  R  ||")
        print("|| G  GGG  AAAAA  M  M  M  EEE    O   O  V   V   EEE  RRR   ||")
        print("|| G    G  A   A  M     M  E      O   O   V V    E    R R   ||")
        print("|| GGGGGG  A   A  M     M  EEEE   OOOOO    V     EEEE R  R  ||")
        print("||                                                          ||")
        
#MENU INICIAL DA FORCA
def menu_inicial():
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("========                                     ")
    print("||   (_)    FFFFF OOOOO RRRRR CCCCC AAAAAA   ")
    print("||   /|\    F     O   O R   R C     A    A   ")
    print("||  / | \   FFFF  O   O RRRR  C     AAAAAA   ")
    print("||   / \    F     O   O R  R  C     A    A   ")
    print("||  /   \   F     OOOOO R   R CCCCC A    A   ")
    print("||                                           ")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

#VARIAVEIS UTILIZADAS PARA QUEBRAR OS LOOPS E PROSSEGUIR OU ENCERRAR A APLICAÇÃO
jogo = "inicio"
prosseguir = "continue"

#BLOCO PRINCIPAL DA APLICAÇÃO
while True:  



    #BLOCO PARA INICIAR E ENCERRAR A APLICAÇÃO
    if jogo == "inicio":
        menu_inicial()
        iniciar = str.upper(input("|| Digite S para iniciar ou E para sair: "))
        while iniciar != "S":
            if iniciar == "S":
                next
            if iniciar == "E":
                prosseguir = "exit"
                break          
            if iniciar != "S" and iniciar != "E":
                iniciar = str.upper(input("|| Digite uma opção válida, S ou E: "))
    elif jogo == "fim":
        finalizar = str.upper(input("|| Deseja jogar de novo? S ou N? "))
        while finalizar != "S":
            if finalizar == "S":
                next
            if finalizar == "N":
                prosseguir = "exit"
                break
            if finalizar != "S" :
                finalizar = str.upper(input("|| Digite uma opção válida, S ou N: "))
    if prosseguir == "exit":
        break

    #LIMPAR A TELA
    limpar_tela()


    #JOGAR SOZINHO OU EM DUPLA
    #SE JOGAR SOZINHO, PEGA A PALAVRA DA LISTA DE PALAVRAS
    #SE JOGAR EM DUPLA, UM JOGADOR IRÁ ESCOLHER A PALAVRA
    print("Você deseja jogar sozinho, ou em dupla?")
    pergunta = str.upper(input("Digite S para sozinho, ou D para jogar em dupla: "))
    while True:
        if pergunta == "S":
            #SORTEIA UMA PALAVRA
            palavra = list(random.choice(lista))
            break
        if pergunta == "D":
            #PERGUNTA AO USUARIO PARA ESCOLHER UMA PALAVRA
            palavra = list(str.upper(input("Digite uma palavra: ")))
            break
        if pergunta != "S" :
            pergunta = str.upper(input("|| Digite uma opção válida, S ou D: "))
  
    #TRANSFORMA A PALAVRA EM TRAÇOS
    ocultar = list(len(palavra)*"_")

    #CONTADOR DE TENTATIVAS E ERROS
    tentativas = 0
    erros = 0
    escolhas = ""

    #EXECUTA ENQUANTO O NÚMERO DE ERROS FOR MENOR QUE 7
    while erros < 7:

        #TELA INICIAL DA FORCA
        tela(erros,tentativas,escolhas)
        
        #BLOCO PARA CONCATENAR AS LETRAS DA LISTA OCULTAR
        exibir = ""
        for i in ocultar:
            exibir += (i + " ")
        print("||          " + exibir)
        print("|| ")

        #INPUT PARA O USUÁRIO
        a = str.upper(input("Digite uma letra: "))  
        
        #MEMORIZA AS OPÇÕES ESCOLHIDAS PELO USUÁRIO
        escolhas = escolhas + " " + a

        #LISTA QUE SERVIRÁ PARA VERIFICAR SE CADA LETRA É IGUAL A LETRA ESCOLHIDA
        verif = list(len(palavra)*"_")

        #BLOCO QUE IRA COMPARAR A LETRA ESCOLHIDA COM CADA LETRA DA PALAVRA
        #CONTADOR IRÁ SERVIR PARA IDENTIFICAR O ÍNDICE DE CADA LETRA
        i = 0
        for letra in palavra:
            #SE A COMPARAÇÃO FOR VERDADEIRA:
            # - IRÁ SUBSTITUIR O TRAÇO PELA LETRA ESCOLHIDA PELO USUÁRIO
            # - IRÁ GRAVAR NA LISTA VERIF A PALAVRA TRUE
            if letra == a:
                ocultar[i] = palavra[i]
                verif[i] = "true"
            #IRA GRAVAR A PALAVRA FALSE NA LISTA VERIF, CASO A CONDIÇÃO NÃO SEJA VERDADEIRA
            else:
                verif[i] = "false"
            #INCREMENTO DO CONTADOR
            i += 1            

        if ocultar != palavra:        
            #BLOCO QUE IRÁ CONTAR QUANTAS COMPARAÇÕES FORAM FALSAS
            y = 0
            for x in verif:
                if x == "false":
                    y += 1

            #VERIFICA O COMPRIMENTO DA STRING DA PALAVRA QUE FOI SORTEADA
            comp = len(palavra)

            #SE O NÚMERO DE ERROS EM "Y" FOR IGUAL AO COMPRIMENTO DA PALAVRA SORTEADA,
            #SIGNIFICA QUE NENHUMA LETRA DA PALAVRA FOI ACERTADA
            #SE NENHUMA OPÇÃO FOR ACERTADA, SERÁ AUMENTADO O CONTADOR DE "TENTATIVAS" E "ERROS"
            if y == comp:
                tentativas += 1
                erros += 1  
            #CASO A COMPARAÇÃO FOR FALSA, SIGNIFICA QUE PELO MENOS UMA LETRA FOI ACERTADA
            #LOGO, SERÁ AUMENTADO O INCREMENTO SO DAS "TENTATIVAS"
            else:
                tentativas += 1

            #SE O NUMERO DE ERROS FOR IGUAL A 7 É FIM DE JOGO
            if erros == 7:
                tela(erros,tentativas,escolhas)
                jogo = "fim"

        #SE O OCULTADO SE TORNAR IGUAL A PALAVRA, GANHA O JOGO
        if ocultar == palavra:
            limpar_tela()
            print("||                                               ||")
            print("|| Y   Y OOOOO U   U    W         W IIIII NN   N ||")
            print("||  Y Y  O   O U   U    W         W   I   N N  N ||")
            print("||   Y   O   O U   U     W   W   W    I   N  N N ||")
            print("||   Y   O   O U   U      W W W W     I   N   NN ||")
            print("||   Y   OOOOO UUUUU       W   W    IIIII N    N ||")
            print("||                                               ||")
            jogo = "fim"
            input("pressione qualquer tecla para continuar ")

            #ENCERRA O CICLO WHILE
            break
        

      
    

        






