
import random

velocidade = input("Escreva a velocidade do veiculo:")
if velocidade == "":
    print("A velocidade não foi fornecida")
    print("Como nenhum numéro foi informado será gerado uma velocidade aléatoria.")
    n = random.randint(1,120)
    
    if n > 90:
        multa = (n - 90) *7 
        print(f"Sua velocidade foi de {n}km/h. \nVocê esta acima do limite velocidade permitida e por isso foi multado em {multa} reais.")
    elif n < 30:
        print(f"Sua velocidade foi de {n}km/h. \nA velocidade do veiculo está muito lenta, deve mudar de mão.")
else:
    velocidade = int(velocidade)

    if velocidade > 90:
        multa = (velocidade - 90) *7 
        print(f"Voce esta acima do limite velocidade permitida e por isso foi multado em {multa} reais")
    elif velocidade < 30:
        print("A velocidade do veiculo está muito lenta, deve mudar de mao")

