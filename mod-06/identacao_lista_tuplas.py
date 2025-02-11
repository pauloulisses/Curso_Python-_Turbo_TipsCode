"""def my_function():
    if name == 'Jesus':
        print('Jesus')
    elif name == 'Paulo':
        print('Paulo')
    print('Nada')"""


# A função do range é gera uma sequência
# sera gerado de 1 a 4
a = 1
b = 5
for number in range(a,b):
    print(number)


#Listas: Mutáveis, usadas para coleções que podem mudar.

#Tuplas: Imutáveis, usadas para coleções fixas.

"""Listas são coleções mutáveis e ordenadas de elementos. 
Isso significa que você pode adicionar, remover ou 
modificar itens após a criação da lista."""


lists = ['Arroz', 'Feijão', 'Carne']
for item in lists:
    print(item)


"""
Tuplas são coleções imutáveis e ordenadas de elementos. Isso significa que, 
após a criação, você não pode adicionar, remover ou modificar itens.
"""

lista_compras = ['Maça', 'Banana', 'Leite']
lista_compras.append('Pão')
print(lista_compras)