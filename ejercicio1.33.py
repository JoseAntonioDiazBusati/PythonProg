"""
Inicio

	Escribe "Dame 3 números: "
	Lee n1
	Lee n2
	Lee n3
	
	Si (n1 < n2 and n1 < n3) entonces
		Si (n2 < n3) entonces
			Escribe n1 + " " + n2 + " " + n3
		Sino
			Escribe n1 + " " + n3 + " " + n2
	Sino
		Si (n2 < n1 and n2 < n3) entonces
			Si (n1 < n3) entonces
				Escribe n2 + " " + n1 + " " + n3
			Sino
				Escribe n2 + " " + n3 + " " + n1
		Sino
			Si (n3 < n1 and n3 < n2) entonces
				Si (n1 < n2) entonces
					Escribe n3 + " " + n1 + " " + n2
				Sino
					Escribe n3 + " " + n2 + " " + n1

Fin
"""
num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro numero: "))
num3=int(input("Introduce un ultimo numero: "))
if (num1<num2)and (num1<num3):
	if num2<num3:
		print(f"{num1},{num2},{num3}")
	else:
		print(f"{num1},{num3},{num2}")
else:
	if (num2<num1)and (num2<num3):
		if num1<num3:
			print(f"{num2},{num1},{num3}")
		else:
			print(f"{num2},{num3},{num1}")
	else:
		if (num3<num1)and (num3<num2):
			if num1<num2:
				print(f"{num3},{num1},{num2}")
			else:
				print(f"{num3},{num2},{num1}")