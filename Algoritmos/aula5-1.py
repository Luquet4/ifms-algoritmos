lista1 = [1]*2
#lista1.append(10) # adiciona o valor na parte final da lista
lista1.insert(7, 20) # escolhe onde quer inserir 1- elemento indice, 2-  elemento é o que será inserido.


# remover itens da lista -

 # primeira ocorrencia
print(lista1) # index

#funcoes

print(len(lista1))

print(sum(lista1))

print(min(lista1))

print(max(lista1))


# listas aninhadas

lista2 = [[1, 2], [3, 4]]

print(lista2[1][0])

for i in range(2):
    for j in range(2):
        print(lista2[i][j])
        
dias = ('Domingo', 'Sábado', 'Segunda', 'Terça') # tupla imutavel


# keys() para pegar as chaves de dicionarios


# values() para pegar os valores de cada chave do dicionario.