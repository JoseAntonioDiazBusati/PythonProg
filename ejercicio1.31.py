"""

Introduce un número: 15
Inténtalo otra vez! (1-10): 0
Inténtalo otra vez! (1-10): 5 
Correcto!

Inicio

	Escribe "Introduce un número: "
	Lee num
	
	Mientras (num < 1 or num > 10)
		Escribe "Inténtalo otra vez! (1-10): "
		Lee num
	Escribe "Correcto!"
	
Fin
"""
num=int(input("Introduce un numero: "))
while num<1 or num>10:
    num=int(input("Intentalo de nuevo!! (1-10): "))
print("Correcto")