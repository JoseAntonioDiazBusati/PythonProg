"""
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y 
cuantos números existen entre ellos dos.
El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
El pseudocódigo debes incluirlo como comentarios en el programa de Python.

Inicio
    Leemos num1
    Leemos num2
    Si num1 es igual a num2 mostramos "Los numeros no pueden ser iguales"
    Sino num1 es mayor que num2 mostramos "num2 es menor"
    Sino "num1 es menor"
fin
"""
#Leemos num1
num1=int(input("Introduce un numero: "))
#Leemos num2
num2=int(input("Añade otro más: "))
#Si num1 es igual a num2 mostramos "Los numeros no pueden ser iguales"
if num1==num2:
    print("Error. No pueden ser iguales")
#Si num1 es mayor que num2 mostramos "num2 es menor"
elif num1>num2:
    print(f"{num2} es menor y hay una diferencia de {num1-num2} numeros enteros.")
#Sino "num1 es menor"
else:
    print(f"{num1} es menor y hay una diferencia de {num2-num1} numeros enteros")