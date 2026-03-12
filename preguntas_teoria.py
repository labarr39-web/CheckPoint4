# Teoria 1
print('Pregunta teoría 1')
lista=['Uno', 2, 'Tres', ['A', 'B', 'C', 'D'], 'Cinco']
tupla=('Uno', 2, 'Tres', ['A', 'B', 'C', 'D'], 'Cinco')
#tupla[3]= [20] # Esto da error
tupla[3][1]='J'

print(tupla)



# Teoría 3
print('Pregunta teoría 3')
lista=[1,'dos',3.5,['A', 'B', 'C', 'D']]

diccionario= {
    'primero': 1,
    'segundo': 'dos',
    'tercero': 3.5,
    'cuarto' : ['A', 'B', 'C', 'D'],
}

print(lista[3])
print(diccionario['cuarto'])

diccionario['cuarto'] = 'String'
print(diccionario)


# Teoría 4
print('Pregunta teoría 4')

lista=[1, 2, 3, 4]
lista_ordenada=sorted(lista, reverse=True)
print(lista)
print(lista_ordenada)

lista.sort(reverse=True)
print(lista)


# Ejercicio 5
variable=5
variable *=2
variable=variable*2



