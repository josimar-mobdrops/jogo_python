import random


def jogar():
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 3
    pontos = 1000
    print("**********Game de Adivinhação**********")

    print("Qual o Nível de Dificuldade?")
    print("(1) Fácil \n (2) Médio \n(3) Dificil")

    nivel = int(input("Define o Nível: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        acertou = numero_secreto == chute
        e_maior = chute > numero_secreto
        e_menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("você deve digitar um numero entre 0 e 100")
            continue

        if (acertou):
            print("Você acertou e fez {}".format(pontos))
            break
        else:
            if (e_maior):
                print("Você errou! o seu chute foi maior que o numero secreto")
            elif (e_menor):
                print("Você errou! o seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)  # abs traz o numero absoluto, tirando o valor negativo.
            pontos = pontos - pontos_perdidos

    print("numero secreto é: {}".format(numero_secreto))
    print("fim de jogo")

if(__name__=="__main__"):
    jogar()
