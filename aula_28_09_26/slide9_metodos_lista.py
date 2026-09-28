# Listas são mutáveis.
# Uso de  [].
# Usei o exemplo do Supermercado para aplicar os métodos.

# append == adiciona um elemento final na lista.
precos = [10,5,20,30]
precos.append(40)
print(precos)

# insert == adiciona um elemento em uma posição espefica.
precos = [2, 4, 5, 10, 87] 
print(precos)
precos.insert(0, 15) # adiciona um elemento na posicao 0 por exemplo
print(precos)

# remove == remove um elemento ou valor especifico dentro da lista.
precos = [10, 5, 24, 34, 75, 20, 30]
precos.remove(75)  # removeu o numero 75
print(precos)

#  pop () - parenteses vazio == remove o ultimo elemento de uma lista.
# pop (1) - informando a posição do índice ==  removerá aquele elemento específico.
# Usamos pop quando sabemos o índice do elemento ou quando iremos reutilizar aquele valor removido.
precos = [10, 5, 20, 888, 30]
x = precos.pop()  # guardei o valor removido em uma variável.
print(f'O valor removido foi: {x}')

# count == conta quantas vezes um elemento aparece.
precos = [10, 5, 30, 15, 30, 20, 888, 30]
precos.count(30)  # o valor 30 ocorre 3 vezes.
print(precos.count(30))  

# index == retorna a posicao (índice) do valor que voce busca.
precos = [10, 5, 20, 888, 30]
precos.index(5) # o valor 5 está na posição 1 (começa do 0).
print(precos.index(5)) # aqui mostra o valor 1

# sort == ordena a lista em ordem crescente.
precos = [10,5,20,30]
precos.sort() # parenteses vazio irá executar o método.
print(precos)

# reverse == inverte a ordem dos elementos da lista
precos = [10,5,20,30]
precos.reverse() # inverte detrás para frente
print(precos)
