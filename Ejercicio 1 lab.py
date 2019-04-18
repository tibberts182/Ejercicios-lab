#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1
#     Matias Melivilu

# In[ ]:


rut = (input("ingrese su rut sin puntos ni digito verificador: "))
longitud = len(rut)
long = longitud
x=0
y=2
suma=0
while(x<longitud): 
    suma = y*(int(rut[long-1]))+suma
#    print(y)
    long-=1
    y+=1
    if(x==5):
        y=2
    x+=1
    print(suma)
entero = suma//11
resto = suma%11
print(entero,resto)
if(11-resto==10):
    print("K")
elif(11-resto==11):
    print("0")
else:
    print(11-resto)

