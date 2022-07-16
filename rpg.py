from pickle import FALSE
import random

print("Bem vindo ao Rpg, escolha uma das duas classes para começar: ")
print(f"[1] Mago \n[2] Guerreiro")
classe = int(input("Escolha uma opção: "))
if classe == 1:
    poder = random.randint(7, 15)
    vida = 38
    vidamostro = 20

    print('''Para começar escolha uma ação:
[1] Atacar
[2] Defender
[3] Curar
[4] Descansar
[5] Sair
    ''')
    escolha = int(input("E aí? Qual você vai escolher? -> "))
    ataqueplayer = False
    while vida >= 0 or escolha == 5:

        if escolha == 1:
            if poder < 1: 
                print("Você não tem poder o suficiente para atacar, você terá que descansar no próximo turno")
            else:
                ataque = random.randint(1, 20)
                poder -= 2
                if ataque > 12:
                    dano = random.randint(3, 10)
                    if dano == 10:
                        print("A SUA ROLADA FOI CRÍTICA!")

                        print(f"Você deu {dano} de dano no Monstro!")
                        vidamostro -= dano
                        ataqueplayer = True
                else:
                    print("Você errou o ataque, espere o turno do monstro para ver se ele vai conseguir defender!")
                ataqueplayer = False

            

        elif escolha == 2:
            defender = True
            print("No turno do Monstro, você defenderá!")
            poder -= 1
        elif escolha == 3:
            if vida > 38:
                vida = 38
            else:
                vida += 2
            print("Você recupera 2 de Vida.")
        elif escolha == 4:
            descanso = random.randint(1, 5)
            poder += descanso
            print(f"Você senta numa fogueira e se sente revigorado. Você recuperou {descanso} de poder. ")
        else:
            exit()

        print("\n\n\n\n\n -=-=-=-= TURNO DO MONSTRO -=-=-=-= ")

        escolhamonstro = random.randint(1, 2)

        if escolhamonstro == 1:
            if ataqueplayer == False:
                esquiva = random.randint(1, 20)
                if esquiva > 12:
                    print("O monstro conseguiu defender e não tomou nenhum dano.")
                else:
                    dano = random.randint(3, 10)
                    if dano == 10:
                        print("A SUA ROLADA FOI CRÍTICA!")
                    print(f"O monstro não conseguiu defender e ele tomará {dano}")
                    vidamostro -= dano

            if escolha == 2:
                print("Você defendeu e não tomou nenhum dano.")
            else:
                print(f"O mostro acabou de te atacar e você receber 3 de dano.")
                vida -= 3

        elif escolhamonstro == 2:
            if ataqueplayer == False:
                esquiva = random.randint(1, 20)
                if esquiva > 12:
                    print("O monstro conseguiu defender e não tomou nenhum dano.")
                else:
                    dano = random.randint(3, 10)
                    if dano == 10:
                        print("A SUA ROLADA FOI CRÍTICA!")
                    print(f"O monstro não conseguiu defender e ele tomará {dano}")
                    vidamostro -= dano
            elif ataqueplayer == True:
                print("O player acertou o ataque e o montro não pode fazer nada!")

        print(f'''\n\n\n\n\n=-=-=-=-=-=-= STATUS DO TURNO =-=-=-=-=-=-=
        \nVida do Player -> {vida}
Poder do Player -> {poder}        
Vida do Monstro -> {vidamostro}
        ''')

        if vidamostro < 0:
            matou = ("Você derrotou o monstro, o que você deseja fazer?\n[1] Continuar\n [2] Sair\n Sua resposta: ")
            if matou == 2:
                exit()
            elif matou == 1:
                vida += 5
                vidamostro += 30

            print("\n\n\n\n\n-=-=-=-= TURNO DO PLAYER -=-=-=-= ")
            print('''Escolha uma ação:
        [1] Atacar
        [2] Defender
        [3] Curar
        [4] Descansar
        [5] Sair
        ''')
        escolha = int(input("E aí? Qual você vai escolher? -> "))

        



        



        
    

elif classe == 2:
    poder = random.randint(5,10)    
