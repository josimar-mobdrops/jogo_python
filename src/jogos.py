import adivinhacao
import forca


def escolha_jogo():
    print("************************************")
    print("**********Escolha seu jogo**********")
    print("************************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o Jogo?\n"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()

    elif (jogo == 2):
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolha_jogo()
