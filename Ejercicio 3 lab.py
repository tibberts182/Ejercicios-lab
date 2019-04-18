#!/usr/bin/env python
# coding: utf-8

# Ejercicio 3
#     Matias Melivilu

# In[ ]:


angulo1 = float(input("ingresa el primer angulo del triangulo: "))
angulo2 = float(input("ingresa el segundo angulo del triangulo: "))
angulo3 = (angulo1+angulo2-180)*-1
if(angulo1+angulo2+angulo3!=180):
    print("tus anuglos ingresados no son validos para un triangulo :c ")
elif((angulo1>90)and(angulo2<90)and(angulo3<90))or((angulo1<90)and(angulo2>90)and(angulo3<90))or((angulo1<90)and(angulo2<90)and(angulo3>90)):
   print("tu triangulo es obstusangulo")
elif((angulo1==90)or(angulo2==90)or(angulo3==90)):
    print("tu triangulo es recto")
elif((angulo1<90)and(angulo2<90)and(angulo3<90)):
    print("tu triangulo es acutangulo")

