from random import choice

acertos = 0
erros = 0
TENTATIVA = 3

lista_frutas = ('banana', 'uva', 'pera', 'melancia')
palavra_secreta = choice(lista_frutas)
chutes_errados = []

lista_secreta = ['_' for x in palavra_secreta]

enforcou = acertou = False

while not enforcou and not acertou:
    print(lista_secreta)
    print(palavra_secreta)
    chute = input('Digite uma letra:').lower()

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if chute == letra:
                lista_secreta[i] = chute
                acertos += 1
        if acertos == len(palavra_secreta):
            acertou = True
    else:
        erros += 1
        chutes_errados.append(chute)
        print(f"Você errou estas palavras: {chutes_errados}")
        if erros == TENTATIVA:
            print("FORCA")
            enforcou = True