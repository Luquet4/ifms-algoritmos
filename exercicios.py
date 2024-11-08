import os


def resposta_usuario():
    while True:
        resposta = int(input("Deseja realizar o script novamente? Digite 1 para Sim ou 2 para Não: "))
        if resposta == 1:
            limpar_tela()
            return True
        elif resposta == 2:
            print("Até mais!")
            return False    
        else:
            print("Opção inválida! Digite 1 para Sim ou 2 para Não.")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ex1():
    while True:
        print("(Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles.")
        try:
            n1 = float(input("\nDigite um número: "))
            n2 = float(input("Digite outro número: "))
            soma = n1+n2
            print(f"A soma dos números digitados é {soma}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"Erro! {e}")

def ex2():
    while True:
        print("(Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar.")
        try:
            n1 = int(input("\nDigite um número inteiro: "))
            print("Verificando se o número é impar ou par...")
            res = n1 % 2
            if res == 0:
                print(f"O número {n1} é par!")
            else:
                print(f"O número {n1} é impar!")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex3():
    while True:
        print("(Conversor de Temperatura) Receba uma temperatura em graus Celsius e converta para Fahrenheit usando a fórmula:")
        try:
            temp1 = float(input("\nDigite uma temperatura em grau Celsius: "))
            res = temp1 * 1.8 + 32
            print(f"A temperatura digitada {temp1} em Fahrenheit é {res}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex4():
    while True:
        print("(Contador de Caracteres em uma Palavra) Solicite uma palavra do usuário e exiba quantos caracteres ela possui.")
        try:
            plv = input("\nDigite uma palavra: ").strip()
            cont = len(plv)
            print(f"A palavra digitada tem {cont} letras.")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")
def ex5():
    while True:
        print("(Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10).")
        try:
            n1 = int(input("\nDigite um número Inteiro para ver sua tabuada do 1-10: "))
            for i in range(1, 11):
                result = n1*i
                print(f"Tabuada - {n1} x {i} = {result}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex6():
    while True:
        print("(Cálculo de Média Aritmética) Peça três notas de um aluno e calcule a média aritmética delas.")
        try:
         n1 = int(input("\nDigite a nota 1: "))
         n2 = int(input("Digite a nota 2: "))
         n3 = int(input("Digite a nota 3: "))
         media = n1+n2+n3 / 3
         print(f"A média aritmética das notas é {media}")
         if not resposta_usuario():
                break  
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex7():
    while True:
        print("(Inversor de String) Receba uma palavra e exiba-a invertida")
        try:
            plv = input("\nDigite uma palavra: ")
            res = "".join(reversed(plv))
            print(f"\nA palavra {plv} invertida é {res}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex8():
    while True:
        print("(Contagem de Números em uma Lista) Dada uma lista de números, exiba quantos números ela contém.")
        try:
            lista = []
            resp = int(input("\nDigite um range para inserir na lista: "))
            print("\nInserindo números na lista...")
            for i in range(resp):
                lista.append(i)
            quant = len(lista)
            print(f"A lista {lista} contém {quant} números.")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex9():
    while True:
        print("(Verificador de Maioridade) Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.")
        try:
            nome = input("\nDigite seu nome: ")
            idd = int(input("\nDigite sua idade: "))
            if idd >= 18:
                print(f"\n{nome}, você tem {idd} anos e é maior de idade!")
            else:
                print(f"\n{nome}, você tem {idd} anos e é menor de idade!")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex10():
    while True:
        print("(Calculadora de Área de Retângulo) Receba a base e a altura de um retângulo e exiba a área dele usando a fórmula.")
        try:
            base = float(input("\nDigite o valor da base do retângulo: "))
            altura = float(input("\nDigite o valor da altura do retângulo: "))
            area = base*altura
            print(f"A área do retângulo é {area}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex11():
    while True:
        print("(Contador de Palavras Únicas) Peça ao usuário uma frase e, em seguida, conte quantas palavras únicas ela possui (sem considerar maiúsculas e minúsculas).")
        try:
            frase = input("\nDigite uma frase: ")
            palavras = frase.lower().split()

            palavras_unicas = set(palavras)

            for palavra in palavras_unicas:
                contagem = palavras.count(palavra)
                if contagem == 1:
                    print(f"\nA palavra '{palavra}' é única na frase!")
                else:
                    print(f"\nA palavra '{palavra}' se repetiu {contagem} vezes na frase.")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")

def ex12():
    while True:
        print("(Números Primos em um Intervalo) Receba um intervalo de números do usuário (por exemplo, entre 10 e 50) e retorne uma lista com todos os números primos dentro desse intervalo.")
        try:
            n1 = int(input("Digite o valor inicial: "))
            n2 = int(input("Digite o valor final: "))
            lista_primos = []
            for i in range(n1, n2 + 1):
                mult = 0
                if i > 1:
                    for divisor in range(2, i):
                        if i % divisor == 0:
                            mult+=1
                if mult == 0 and i != 1:
                    lista_primos.append(i)
            print(f"Os números primos entre {n1} e {n2} são: {lista_primos}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela()
            print(f"ERRO! {e}")