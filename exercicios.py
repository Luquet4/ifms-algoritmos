import os
import random


def pedir_input(mensagem, type=str):  
    while True:
        try:
            valor = type(input(mensagem))
            return valor
        except Exception as e:
            limpar_tela(erro=str(e))
            print(f"Digite um valor válido para o tipo {type.__name__}.")

def resposta_usuario():
    while True:
        resposta = pedir_input("Deseja realizar o script novamente? Digite 1 para Sim ou 2 para Não: ", type=int)
        if resposta == 1:
            limpar_tela()
            return True
        elif resposta == 2:
            print("Até mais!")
            return False    
        else:
            print("Opção inválida! Digite 1 para Sim ou 2 para Não.")

def limpar_tela(erro=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    if erro:
        print(f"Erro! {erro}")

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def criterio_frequencia(item):
    return item[1]

def ex1():
    while True:
        print("(Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles.")
        try:
            n1 = pedir_input("Digite o primeiro número: ", type=int)
            n2 = pedir_input("Digite o segundo número: ", type=int)
            soma = n1+n2
            print(f"A soma dos números digitados é {soma}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex2():
    while True:
        print("(Verificador de Número Par ou Ímpar) Peça ao usuário um número inteiro e informe se ele é par ou ímpar.")
        try:
            n1 = pedir_input("\nDigite um número inteiro: ", type=int)
            print("Verificando se o número é impar ou par...")
            res = n1 % 2
            if res == 0:
                print(f"O número {n1} é par!")
            else:
                print(f"O número {n1} é impar!")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex3():
    while True:
        print("(Conversor de Temperatura) Receba uma temperatura em graus Celsius e converta para Fahrenheit usando a fórmula:")
        try:
            temp1 = pedir_input("\nDigite uma temperatura em grau Celsius: ", type=float)
            res = temp1 * 1.8 + 32
            print(f"A temperatura digitada {temp1} em Fahrenheit é {res}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex4():
    while True:
        print("(Contador de Caracteres em uma Palavra) Solicite uma palavra do usuário e exiba quantos caracteres ela possui.")
        try:
            plv = pedir_input("\nDigite uma palavra: ", type=str).strip()
            cont = len(plv)
            print(f"A palavra digitada tem {cont} letras.")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            
def ex5():
    while True:
        print("(Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10).")
        try:
            n1 = pedir_input("\nDigite um número Inteiro para ver sua tabuada do 1-10: ", type=int)
            for i in range(1, 11):
                result = n1*i
                print(f"Tabuada - {n1} x {i} = {result}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex6():
    while True:
        print("(Cálculo de Média Aritmética) Peça três notas de um aluno e calcule a média aritmética delas.")
        try:
            notas = []
            for i in range(1, 4):
                num = pedir_input(f"Digite a {i}° nota: ", type=float)
                notas.append(num)
            media = sum(notas) / len(notas)
            print(f"A média aritmética das notas é {media:.2f}")
            if not resposta_usuario():
                break  
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex7():
    while True:
        print("(Inversor de String) Receba uma palavra e exiba-a invertida")
        try:
            plv = pedir_input("\nDigite uma palavra: ", type=str)
            print(f"\nA palavra {plv} invertida é {plv[::-1]}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex8():
    while True:
        print("(Contagem de Números em uma Lista) Dada uma lista de números, exiba quantos números ela contém.")
        try:
            lista = []
            resp = pedir_input("\nDigite um range para inserir na lista: ", type=int)
            print("\nInserindo números na lista...")
            for i in range(resp):
                lista.append(i)
            quant = len(lista)
            print(f"A lista {lista} contém {quant} números.")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex9():
    while True:
        print("(Verificador de Maioridade) Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.")
        try:
            nome = pedir_input("\nDigite seu nome: ", type=str)
            idd = pedir_input("\nDigite sua idade: ", type=int)
            if idd >= 18:
                print(f"\n{nome}, você tem {idd} anos e é maior de idade!")
            else:
                print(f"\n{nome}, você tem {idd} anos e é menor de idade!")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex10():
    while True:
        print("(Calculadora de Área de Retângulo) Receba a base e a altura de um retângulo e exiba a área dele usando a fórmula.")
        try:
            base = pedir_input("\nDigite o valor da base do retângulo: ", type=float)
            altura = pedir_input("\nDigite o valor da altura do retângulo: ", type=float)
            area = base*altura
            print(f"A área do retângulo é {area}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex11():
    while True:
        print("(Contador de Palavras Únicas) Peça ao usuário uma frase e, em seguida, conte quantas palavras únicas ela possui (sem considerar maiúsculas e minúsculas).")
        try:
            frase = pedir_input("\nDigite uma frase: ", type=str).lower().split()
            palavras_unicas = set(frase)
            for palavra in palavras_unicas:
                contagem = frase.count(palavra)
                if contagem == 1:
                    print(f"\nA palavra '{palavra}' é única na frase!")
                else:
                    print(f"\nA palavra '{palavra}' se repetiu {contagem} vezes na frase.")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex12():
    while True:
        print("(Números Primos em um Intervalo) Receba um intervalo de números do usuário (por exemplo, entre 10 e 50) e retorne uma lista com todos os números primos dentro desse intervalo.")
        try:
            n1 = pedir_input("Digite o valor inicial: ", type=int)
            n2 = pedir_input("Digite o valor final: ", type=int)
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
            limpar_tela(erro=str(e))
            


def ex13():
    alunos = [
        {'nome': 'Lucas', 'notas': [7.5, 6, 9], 'media': 0}, 
        {'nome': 'Alex', 'notas': [4.5, 8, 10], 'media': 0}, 
        {'nome': 'Beto',  'notas': [7, 7, 5], 'media': 0},
        {'nome': 'Laura',  'notas': [10, 10, 10], 'media': 0},
        {'nome': 'Maria',  'notas': [1, 1, 1], 'media': 0},
    ]

    media_alunos = []

    while True:
        print("\n(Média com Notas Maiores que a Média)")
        try:
            resp = pedir_input("\nEscolha uma opção - \n1 - Adicionar aluno à lista \n2 - Editar aluno \n3 - Calcular médias \n", type=int)
            if resp == 1:
                nome = pedir_input("\nDigite o nome do aluno: ", type=str)
                alunos.append({'nome': nome, 'notas': [], 'media': 0})
                for i in range(1, 4):
                    nota = pedir_input(f"\nDigite a '{i}°' nota do(a) {nome}: ", type=float)
                    alunos[-1]['notas'].append(nota)
            elif resp == 2:
                nome_al = pedir_input("\nDigite o nome do aluno que deseja editar: ").lower()
                editar_al = [aluno for aluno in alunos if nome_al == aluno['nome'].lower()]
                
                if editar_al:
                    print("\nAlunos encontrados:")
                    for indice, aluno in enumerate(editar_al, start=1):
                        print(f"{indice}. Nome: {aluno['nome']}, Notas atuais: {aluno['notas']}")

                    escolha = pedir_input("\nDigite o número do aluno que deseja editar: ", type=int)
                    
                    if 1 <= escolha <= len(editar_al):
                        aluno_escolhido = editar_al[escolha - 1]
                        print(f"\nEditando notas para {aluno_escolhido['nome']}")
                        aluno_escolhido['notas'].clear()
                        
                        for i in range(1, 4):
                            nota = pedir_input(f"\nDigite a '{i}°' nota: ", type=float)
                            aluno_escolhido['notas'].append(nota)
                        print(f"\nNovas notas de {aluno_escolhido['nome']} - notas: {aluno_escolhido['notas']}")
                    else:
                        print("\nOpção inválida!")
                else:
                    print("\nNenhum aluno encontrado com esse nome.")
            elif resp == 3:
                for aluno in alunos:
                    notas = aluno['notas']
                    aluno['media'] = sum(notas) / len(notas) if notas else 0
                    media_alunos.append(aluno['media'])
                    media_geral = sum(media_alunos) / len(media_alunos) if media_alunos else 0

                print(f"\nA média geral dos alunos é: {media_geral:.2f}")
                media_acima = [aluno for aluno in alunos if aluno['media'] > media_geral]
                media_abaixo = [aluno for aluno in alunos if aluno['media'] <= media_geral]
                
                print("\nAlunos com média acima da média geral:")
                for aluno in media_acima:
                    print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")
                
                print("\nAlunos com média abaixo ou igual à média geral:")
                for aluno in media_abaixo:
                    print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex14():
    while True:
        print("(Verificador de Palíndromos)")
        try:
            plv = pedir_input("Digite uma palavra: ", type=str)
            if plv == plv[::-1]:
                print(f"{plv} é um palíndromo!")
            else:
                print(f"{plv} Não é um palíndromo! {plv[::-1]}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex15():
    tentativas = 7
    num_aleatorio = random.randint(1, 100)
    venceu = False
    while tentativas > 0 and not venceu:
        print("(Jogo de Adivinhação)")
        try:
            n1 = pedir_input("Digite um número inteiro: ", type=int)
            if n1 == num_aleatorio:
                print("Parabéns, você acertou!!")
                venceu = True
            elif n1 > num_aleatorio:
                tentativas -= 1
                print(f"Quase lá!... Você digitou um número maior que o número secreto! Agora você tem {tentativas} tentativas.")
            elif n1 < num_aleatorio:
                tentativas -= 1
                print(f"Quase lá!... Você digitou um número menor que o número secreto! Agora você tem {tentativas} tentativas.")
            if tentativas == 0 and not venceu:
                print(f"Você perdeu! O número secreto era {num_aleatorio}")
        except Exception as e:
            limpar_tela(erro=str(e))

def ex16():
    while True:
        print("(Calculadora de Fatorial Recursiva)")
        try:
            num = pedir_input("Digite um número inteiro: ", type=int)
            resultado = fatorial(num)
            print(f"O fatorial de {num} é {resultado}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex17():
    while True:
        print("(Ordenação de Lista com Números Negativos e Positivos)")
        try:
            lista_num = []
            for _ in range(10):
                lista_num.append(random.randint(-25, 25))
            print(f"\nLista normal - {lista_num}")
            lista_num.sort()
            print(f"Lista ordenada - {lista_num}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex18():
    while True:
        print("(Soma de Diagonais de uma Matriz Quadrada)")
        try:
            matriz = [[12, 23], [43, 41]]
            diag_principal = matriz[0][0] + matriz[1][1]
            diag_secundaria = matriz[0][1] + matriz[1][0]
            print(f"\nA matriz é - {matriz}")
            print(f"\nA soma das diagonais é: PRINCIPAL: '{diag_principal}' SECUNDÁRIA: '{diag_secundaria}' e a soma de AMBAS as diagonais é - {diag_principal + diag_secundaria}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex19():
    while True:
        print("(Contador de Caracteres de uma Frase) ")
        try:
            caracteres_frase = {}
            frase = pedir_input("Digite uma frase: ", type=str).lower()
            for caracter in frase:
                if caracter in caracteres_frase:
                    caracteres_frase[caracter] += 1
                else:
                    caracteres_frase[caracter] = 1
            print(f"\nEsses são os caracteres - {caracteres_frase}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex20():
    while True:
        print("(Gerador de Números da Sequência de Fibonacci)")
        try:
            num = pedir_input("Digite um número: ", type=int)
            lista_fib = [0, 1]

            while len(lista_fib) < num:
                proximo_num = lista_fib[-1] + lista_fib[-2]
                lista_fib.append(proximo_num)

            print(f"Sequência de Fibonacci com {num} números: {lista_fib}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex21():
    while True:
        print("(Remoção de Elementos Duplicados)")
        try:
            lista_num = [1, 1, 2, 2, 3, 3, 5, 5, 10, 10, 20, 20, 12, 12, 15, 15]
            lista_unica = []
            print(f"A lista atualmente é esta - {lista_num}")
            for num in lista_num:
                if num not in lista_unica:
                    lista_unica.append(num)
            print(f"E a lista com as remoções e mantendo a ordem é - {lista_unica}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex22():
    while True:
        print("(Contagem de Vogais e Consoantes)")
        try:
            frase = pedir_input("Digite uma frase: ", type=str)
            lista_vogais = ["a", "e", "i", "o", "u"]
            contagem = {"Vogais": {}, "Consoantes": {}}
            for caracter in frase:
                if not caracter.isalpha():
                    continue

                if caracter in lista_vogais:
                    contagem["Vogais"][caracter] = contagem["Vogais"].get(caracter, 0) + 1
                else:
                    contagem["Consoantes"][caracter] = contagem["Consoantes"].get(caracter, 0) + 1
            
            print(f"Aqui está a lista de contagens - {contagem}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex23():
    while True:
        print("(Calculadora Básica com Estruturas Condicionais)")
        try:
            n1 = pedir_input("Digite o primeiro número: ", type=float)
            n2 = pedir_input("Digite o segundo número: ", type=float)
            resp = pedir_input("Digite a operação que deseja realizar: \n 1- Adição \n 2- Subtração \n 3- Multiplicação \n 4- Divisão\n", type=int)
            match resp:
                case 1:
                    print(f"{n1} + {n2} = {n1+n2}")
                case 2:
                    print(f"{n1} - {n2} = {n1-n2}")
                case 3:
                    print(f"{n1} x {n2} = {n1*n2}")
                case 4:
                    print(f"{n1} / {n2} = {n1/n2}")
                case _:
                    print("Opção invalida!")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex24():
    while True:
        print("(Verificação de Anagrama)")
        try:
            plv = pedir_input("Digite uma palavra: ", type=str).lower()
            plv2 = pedir_input("Digite outra palavra: ", type=str).lower()
            if len(plv) != len(plv2):
                print(f"{plv} & {plv2} NÃO são um anagrama.")
            elif sorted(plv) == sorted(plv2):
                print(f"{plv} & {plv2} SÃO um anagrama.")
            else:
                print(f"{plv} & {plv2} NÃO são um anagrama.")
                    
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex25():
    while True:
        print("(Filtro de Números Pares em uma Lista)")
        try:
            lista_num = [random.randint(1, 100) for _ in range(10)]
            lista_par = [num for num in lista_num if num % 2 == 0]

            print(f"\nLista padrão - {lista_num}")
            print(f"\nLista de pares - {lista_par}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex26():
    while True:
        print("(Mesclagem de Dois Dicionários)")
        try:
            d1 = {k: random.randint(1, 10) for k in ["a", "b", "c"]}
            d2 = {k: random.randint(1, 10) for k in ["b", "c", "d"]}
            resultado = {key: d1.get(key, 0) + d2.get(key, 0) for key in (d1 | d2)}
            print(f"\nDict 1 - {d1}\n")
            print(f"\nDict 2 - {d2}\n")
            print(f"\nResultado - {resultado}\n")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex27():
    while True:
        print("(Contador de Palavras Frequentes)")
        try:
            dic = {}
            txt = pedir_input("Digite um texto: ", type=str).lower().split()
            for palavra in txt:
                if palavra in dic:
                    dic[palavra] += 1
                else:
                    dic[palavra] = 1
            lista_plv = list(dic.items())
            lista_plv.sort(key=criterio_frequencia, reverse=True)
            print(f"\nAqui está as palavras mais repetidas - {lista_plv[:5]}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))

def ex28():
    while True:
        print("(Verificador de Sudoku)")
        try:
            sudoku = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ]
            
            valido = True

            for linha in sudoku:
                if len(set(linha)) != 9:
                    valido = False
                    break

            if valido:
                for col in range(9):
                    coluna = [sudoku[row][col] for row in range(9)]
                    if len(set(coluna)) != 9:
                        valido = False
                        break

            if valido:
                for i in range(0, 9, 3):
                    for j in range(0, 9, 3):
                        subgrid = []
                        for x in range(i, i + 3):
                            for y in range(j, j + 3):
                                subgrid.append(sudoku[x][y])
                        if len(set(subgrid)) != 9:
                            valido = False
                            break
            if valido:
                print("O Sudoku é válido!")
            else:
                print("O Sudoku NÃO é válido!")

            if not resposta_usuario():
                break

        except Exception as e:
            limpar_tela(erro=str(e))


def ex29():
    while True:
        print("(Remoção de Elementos Duplicados de uma Lista Aninhada)")
        try:
            lista_anin = [[1, 2, 2, 4 ,4], [5, 5, 2, 10, 10], [20, 20, 12, 14]]
            lista_final = [list(set(sublista)) for sublista in lista_anin]
            print(f"\nAqui está a lista com duplicados - {lista_anin}")
            print(f"\nAqui está a lista sem duplicados - {lista_final}")
            if not resposta_usuario():
                break
        except Exception as e:
            limpar_tela(erro=str(e))


def navegar_exercicios():
    while True:
        try:
            exercicios = {
                1: ex1,
                2: ex2,
                3: ex3,
                4: ex4,
                5: ex5,
                6: ex6,
                7: ex7,
                8: ex8,
                9: ex9,
                10: ex10,
                11: ex11,
                12: ex12,
                13: ex13,
                14: ex14,
                15: ex15,
                16: ex16,
                17: ex17,
                18: ex18,
                19: ex19,
                20: ex20,
                21: ex21,
                22: ex22,
                23: ex23,
                24: ex24,
                25: ex25,
                26: ex26,
                27: ex27,
                28: ex28,
                29: ex29,
            }
            numero_exercicio = pedir_input("\nDigite o número do exercício (1-29) ou 0 para sair: ", type=int)
            if numero_exercicio == 0:
                break
            elif numero_exercicio in exercicios:
                exercicios[numero_exercicio]()
            else:
                limpar_tela()
                print("Número de exercício inválido!.")
        except ValueError:
            print("Digite um número válido.")


navegar_exercicios()