#!/usr/bin/env python
# coding: utf-8

# Ejercicio 2
#     Matias Melivilu

# In[ ]:


print("tus dos primeros numeros son el piso y los dos ultimos la posicion c:")
numero_departamento = input("ingresa el numero de tu departamento a escojer")
numdepa1 = (numero_departamento[0]+numero_departamento[1])
numdepa1 =int(numdepa1)
numdepa2 = (numero_departamento[2]+numero_departamento[3])
numdepa2 = int(numdepa2)
if((numdepa1==1)and((numdepa2==0)or(numdepa2==4))):
    valor1=(100/100)*80
    print("tu precio de departamento es: ",valor1)
elif((numdepa1==20)and((numdepa2==0)or(numdepa2==4))):
    valor2=(400/100)*80
    print("tu precio de departamento es: ",valor2)
elif((1<numdepa1<20)and((numdepa2==0)or(numdepa2==4))):
    valor3=(250/100)*80
    print("tu precio de departamento es: ",valor3)
elif((numdepa1==1)and((numdepa2==7)or(numdepa2==3))):
    valor4=(100/100)*115
    print("tu precio de departamento es: ",valor4)
elif((numdepa1==20)and((numdepa2==7)or(numdepa2==3))):
    valor5=(250/100)*115
    print("tu precio de departamento es: ",valor5)
elif((1<numdepa1<20)and((numdepa2==7)or(numdepa2==3))):
    valor6=(250/100)*115
    print("tu precio de departamento es: ",valor6)
elif((numdepa1==1)and((numdepa2==1)or(numdepa2==2)or(numdepa2==5)or(numdepa2==6))):
    valor7=(100/100)*100
    print("tu precio de departamento es: ",valor7)
elif((numdepa1==20)and((numdepa2==1)or(numdepa2==2)or(numdepa2==5)or(numdepa2==6))):
    valor8=(400/100)*100
    print("tu precio de departamento es: ",valor8)
elif((1<numdepa1<20)and((numdepa2==1)or(numdepa2==2)or(numdepa2==5)or(numdepa2==6))):
    valor9=(250/100)*100
    print("tu precio de departamento es: ",valor9)

