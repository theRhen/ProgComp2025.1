from random import randint

print("----------------------------------------")
print("       ACERTE O NÚMERO ENTRE 1-100")
print("----------------------------------------")

numero_sorteado = randint(1, 100) # sortear um número inteiro aleatório entre 1 e 100

valor_min = 1 # Valor mínimo atual do intervalo (começa em 1, mas vai mudando conforme os palpites)
valor_max = 100 # Valor máximo atual do intervalo (começa em 100, mas vai mudando conforme os palpites)

print("  Tente acertar o número entre", valor_min, "e", valor_max)
print("        VOCÊ POSSUE 4 TENTATIVAS")
print("........................................")

palpite = int(input("1ª TENTATIVA: "))

if palpite == numero_sorteado: # Possibilidade 1 (acerto)
    print("Você acertou!")
    print("........................................")
else: # Possibilidade 2 (erro)
    if palpite > numero_sorteado: # Possibilidade 2.1 (erro) "Palpite maior que numero sorteado"
        valor_max = palpite - 1
    if palpite < numero_sorteado: # Possibilidade 2.1 (erro) "Palpite menor que numero sorteado"
        valor_min = palpite + 1

    print("Agora o número está entre", valor_min, "e", valor_max)
    print("")
    palpite = int(input("2ª TENTATIVA: "))

    #Repetição das demais tentativas de forma aninhada
    
    if palpite == numero_sorteado:
        print("Você acertou!")
        print("........................................")
    else:
        if palpite > numero_sorteado:
            valor_max = palpite - 1
        if palpite < numero_sorteado:
            valor_min = palpite + 1

        print("O número está entre", valor_min, "e", valor_max)
        print("")
        palpite = int(input("3ª TENTATIVA: "))

        if palpite == numero_sorteado:
            print("Você acertou!")
            print("........................................")
        else:
            if palpite > numero_sorteado:
                valor_max = palpite - 1
            if palpite < numero_sorteado:
                valor_min = palpite + 1

            print("O número está entre", valor_min, "e", valor_max)
            print("")
            palpite = int(input("4ª TENTATIVA: "))

            if palpite == numero_sorteado:
                print("Você acertou!")
                print("----------------------------------------")
            else:
                print("Suas tentativas acabaram.")
                print("........................................")
                print("O número era: ", numero_sorteado)
                print("----------------------------------------")
