import math
from decimal import Decimal


# Ejercicio 1
print('--- Ejercicio 1 ---')
print('')

lista=['Uno', 2, 'Tres', ['A', 'B', 'C', 'D'], 5.45]

tupla=('Uno', 2, 'Tres', ['A', 'B', 'C', 'D'], 'Cinco')

numero_flotante= 14.56

numero_entero=17

numero_decimal=Decimal(45.37)

diccionario= {
    'primero': 1,
    'segundo': 'dos',
    'tercero': 3.5,
    'cuarto' : ['A', 'B', 'C', 'D'],
}

print(type(lista))
print(type(tupla))
print(type(numero_flotante))
print(type(numero_entero))
print(type(numero_decimal))
print(numero_decimal)
print(type(diccionario))



# Ejercicio 2
print('')
print('--- Ejercicio 2 ---')
print('')

float_up = math.ceil(numero_flotante)
print(f'número flotante: {numero_flotante}')
print(f'número redondeado al alza : {float_up}')



# Ejercicio 3
print('')
print('--- Ejercicio 3 ---')
print('')

sqrt_flotante = math.sqrt(numero_flotante)
print(f'La raiz cuadrada de {numero_flotante} es {sqrt_flotante}')



# Ejercicio 4
print('')
print('--- Ejercicio 4 ---')
print('')

diccionario_item = list(diccionario.items())[0]
print(diccionario_item)



# Ejercicio 5
print('')
print('--- Ejercicio 5 ---')
print('')

tupla_elemento_2 = tupla[1]
print(tupla_elemento_2)



# Ejercicio 6
print('')
print('--- Ejercicio 6 ---')
print('')

lista.append('Elemento añadido')
print(lista)



# Ejercicio 7
print('')
print('--- Ejercicio 7 ---')
print('')

lista[0]="elemento reemplazado"
print(lista)



# Ejercicio 8
print('')
print('--- Ejercicio 8 ---')
print('')

lista_2 = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']

lista_2.sort()
print(lista_2)



# Ejercicio 9
print('')
print('--- Ejercicio 9 ---')
print('')

tupla += ('nuevo elemento',)
print(tupla)
