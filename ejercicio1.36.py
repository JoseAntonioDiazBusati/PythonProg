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
