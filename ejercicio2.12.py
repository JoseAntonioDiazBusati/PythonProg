peso=int(input("Introduce tu peso en kg: "))
altura=float(input("Ahora introduce su altura en metros: "))
imc=(peso/(altura**2))
print(f"Tu índice de masa corporal es {imc} donde es el índice de masa corporal calculado redondeado con dos decimales {imc:.2f}.")