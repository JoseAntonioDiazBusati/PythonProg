"""
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
El pseudocódigo debes incluirlo como comentarios en el programa de Python.

Inicio

Leemos nombre
si nombre=="" usamos Desconocido
Leemos edad
Si edad es menor o igual que 0 y mayor o igual que 125 mostramos "Error"
Sino mostramos su nombre y edad y los años que le quedan por cumplir"

Fin
"""
#leemos nombre
nombre=str(input("Introduzca su nombre: "))
#Si nombre=="" usamos desconocido
if nombre=="":
    nombre="Desconocido"
#Leemos edad
edad=int(input("Introduzca su edad: "))
#Si edad es menor o igual que 0 y mayor o igual que 125 mostramos "Error"
if edad<0 and edad>125:
    print("Error")
#Sino mostramos su nombre y edad y los años que le quedan por cumplir"
else:
    print(f"Te llamas {nombre} y tienes {edad}, te quedan aún {125-edad} años por cumplir")