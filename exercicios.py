import os

def pedir_num(mensagem="Digite um número: ", type=int):
    while True:
        try:
            num = type(input(mensagem))  
            return num
        except Exception as e:
            limpar_tela(erro=str(e))
            print("Digite um número válido.")

def pedir_texto(mensagem="Digite uma palavra ou Frase: "):
    while True:
        try:
            plv = input(mensagem)
            if plv:
                return plv
            print("Digite uma palavra ou frase somente.")
        except Exception as e:
            limpar_tela(erro=str(e))

def resposta_usuario():
    while True:
        resposta = pedir_num("Deseja realizar o script novamente? Digite 1 para Sim ou 2 para Não: ", type=int)
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


def ex1():
    while True:
        print("(Calculadora de Soma Simples) Receba dois números do usuário e exiba a soma deles.")
        try:
            n1 = pedir_num("Digite o primeiro número: ", type=int)
            n2 = pedir_num("Digite o segundo número: ", type=int)
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
            n1 = pedir_num("\nDigite um número inteiro: ", type=int)
            print("Verificando se o número é impar ou par...", type=int)
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
            temp1 = pedir_num("\nDigite uma temperatura em grau Celsius: ", type=float)
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
            plv = pedir_texto("\nDigite uma palavra: ").strip()
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
            n1 = pedir_num("\nDigite um número Inteiro para ver sua tabuada do 1-10: ", type=int)
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
                num = pedir_num(f"Digite a {i}° nota: ", type=float)
                notas.append(num)
            media = sum(notas) / len(notas)
            print(f"A média aritmética das notas é {media:2f}")
            if not resposta_usuario():
                break  
        except Exception as e:
            limpar_tela(erro=str(e))
            

def ex7():
    while True:
        print("(Inversor de String) Receba uma palavra e exiba-a invertida")
        try:
            plv = pedir_texto("\nDigite uma palavra: ")
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
            resp = pedir_num("\nDigite um range para inserir na lista: ", type=int)
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
            nome = pedir_texto("\nDigite seu nome: ")
            idd = pedir_num("\nDigite sua idade: ", type=int)
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
            base = pedir_num("\nDigite o valor da base do retângulo: ", type=float)
            altura = pedir_num("\nDigite o valor da altura do retângulo: ", type=float)
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
            frase = pedir_texto("\nDigite uma frase: ").lower().split()
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
            n1 = pedir_num("Digite o valor inicial: ", type=int)
            n2 = pedir_num("Digite o valor final: ", type=int)
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
            resp = pedir_num("\nEscolha uma opção - \n1 - Adicionar aluno à lista \n2 - Editar aluno \n3 - Calcular médias \n", type=int)
            if resp == 1:
                nome = pedir_texto("\nDigite o nome do aluno: ")
                alunos.append({'nome': nome, 'notas': [], 'media': 0})
                for i in range(1, 4):
                    nota = pedir_num(f"\nDigite a '{i}°' nota do(a) {nome}: ", type=float)
                    alunos[-1]['notas'].append(nota)
            elif resp == 2:
                nome_al = pedir_texto("\nDigite o nome do aluno que deseja editar: ").lower()
                editar_al = [aluno for aluno in alunos if nome_al == aluno['nome'].lower()]
                
                if editar_al:
                    print("\nAlunos encontrados:")
                    for indice, aluno in enumerate(editar_al, start=1):
                        print(f"{indice}. Nome: {aluno['nome']}, Notas atuais: {aluno['notas']}")

                    escolha = pedir_num("\nDigite o número do aluno que deseja editar: ", type=int)
                    
                    if 1 <= escolha <= len(editar_al):
                        aluno_escolhido = editar_al[escolha - 1]
                        print(f"\nEditando notas para {aluno_escolhido['nome']}")
                        aluno_escolhido['notas'].clear()
                        
                        for i in range(1, 4):
                            nota = pedir_num(f"\nDigite a '{i}°' nota: ", type=float)
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
            



ex13()