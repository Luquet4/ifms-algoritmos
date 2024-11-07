from random import choice

acertos = 0

lista_frutas = ['banana', 'uva', 'pera', 'melancia']
palavra_secreta = choice(lista_frutas)

lista_secreta = ['_' for x in palavra_secreta]

enforcou = acertou = False

while not enforcou and not acertou:
        print(lista_secreta)
        print(palavra_secreta)
        chute = input('Digite uma letra:').lower()

        for i, letra in enumerate(palavra_secreta):
            if chute == letra:
                lista_secreta[i] = chute
                acertos += 1
        if acertos == len(palavra_secreta):
            acertou = True
        else:
            continue