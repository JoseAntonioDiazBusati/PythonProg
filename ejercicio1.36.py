"""
Inicio

	Escribe "¿Cuántas notas vas a introducir? "
	Lee total
	
	Mientras (total < 1 o total > 100) hacer
		Escribe "Error - el número de notas debe ser un número entero entre 1 y 100"
		Escribe "¿Cuántas notas vas a introducir? "
		Lee total

	Escribe "Dame las " + total + " notas del curso: "
	
	media = 0
	cont = 1
	Mientras (cont <= 10) hacer
		Lee nota
		media = media + nota
		cont = cont + 1

	media = media / total
	Escribe "La media es " + media
	
Fin
"""
total=int(input("¿Cuantas notas vas a introducir?: "))
while(total<1 and total>0):
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    total=int(input("¿Cuantas notas vas a introducir?: "))
print(f"Dame las {total} notas del curso: ")
media=0
cont=1
while(cont<=10):
    nota=int(input())
    media=media+nota
    cont=cont+1
media=media/total
print(f"La media es {media}")