"""
Inicio

	Escribe "Introduce dos números: "
	Lee n1
	Lee n2
	
	opcion = 0
	Mientras (opcion < 1 or opcion > 4) hacer
		Escribe "Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "
		Lee opcion
		Si (opcion < 1 or opcion > 4) entonces
			Escribe "Error - No es una opción correcta (1-4)"
	
	Segun (opcion) entonces
		1:
			Escribe n1 + " + " + n2 + " = " + (n1+n2)
		2:
			Escribe n1 + " - " + n2 + " = " + (n1-n2)
		3:
			Escribe n1 + " * " + n2 + " = " + (n1*n2)
		4:
			Si (n2 == 0) entonces
				Escribe "La división por cero no es posible"
			Sino
				Escribe n1 + " / " + n2 + " = " + (n1/n2)
	
Fin
"""
