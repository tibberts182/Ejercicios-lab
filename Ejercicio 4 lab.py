#!/usr/bin/env python
# coding: utf-8

# Ejercicio 4
#     Matias Melivilu

# In[ ]:


nombre = input("ingrese el nombre del clavadista: ")
grado = float(input("ingrese el grado de dificultad: "))
print("ingrese los puntajes de los juezces sabiendo que pueden ser multiplos de 0,5")
y=1
while(y!=0): 
    juez1 = float(input("ingrese el puntaje del juez n1: "))
    y=juez1%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")
y=1
while(y!=0): 
    juez2 = float(input("ingrese el puntaje del juez n2: "))
    y=juez2%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")
y=1
while(y!=0): 
    juez3 = float(input("ingrese el puntaje del juez n3: "))
    y=juez3%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")
y=1
while(y!=0): 
    juez4 = float(input("ingrese el puntaje del juez n4: "))
    y=juez4%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")    
y=1
while(y!=0): 
    juez5 = float(input("ingrese el puntaje del juez n5: "))
    y=juez5%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")
y=1
while(y!=0): 
    juez6 = float(input("ingrese el puntaje del juez n6: "))
    y=juez6%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")        
y=1
while(y!=0): 
    juez7 = float(input("ingrese el puntaje del juez n7: "))
    y=juez7%0.5
    if(y!=0):
        print("ingresa un puntaje valido :c ")        
lista = [juez1,juez2,juez3,juez4,juez5,juez6,juez7]
lista_ordenada = sorted(lista)
#print(lista_ordenada)
lista_sin_mayor_y_menor = [lista_ordenada[1],lista_ordenada[2],lista_ordenada[3],lista_ordenada[4],lista_ordenada[5]]
#print(lista_sin_mayor_y_menor)
suma = ((float(lista_ordenada[1])+float(lista_ordenada[2])+float(lista_ordenada[3])+float(lista_ordenada[4])+float(lista_ordenada[5]))*0.6)
#print(suma)
resultado = suma*grado
print("el puntaje total es: ",resultado)

