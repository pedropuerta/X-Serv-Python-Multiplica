#!/usr/bin/python3

#Ejercicio 13.3

for numero1 in range(11)[1:11]:
    print ("Tabla del " + str(numero1))
    print ("----------")
    for numero2 in range(11)[1:11]: 
        print(str(numero1) + " por " + str(numero2) + " es " + str(numero1 * numero2))
    

