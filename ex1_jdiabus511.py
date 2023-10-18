"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio

Escribe "Introduzca un numero"
Leer numero
Si numero es < 0 o > 10 entonces
    Escribe "¡No puede ser negativo o mayor de 10!"
Sino
    Si numero%2==0 entonces
        Escribe "Es un numero par"
    Sino
        Escribe "Es un numero impar"

Fin
"""
#EJEMPLO DEL CODIGO RESULTANTE

#Escribe "Introduzca un numero"
#Leer numero
numero=int(input("Introduzca un numero: "))
#Si numero es < 0 o > 10 entonces
if numero<0 or numero>10:
    #Escribe "¡No puede ser negativo o mayor de 10!"
    print("¡No puede ser negativo o mayor de 10!")
#Sino
else:
    #Si numero%2==0 entonces
    if numero%2==0:
        #Escribe "Es un numero par"
        print("Es par")
    #Sino
    else:
        #Escribe "Es un numero impar"
        print("Es impar")