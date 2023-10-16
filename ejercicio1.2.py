"""
1.2 => recibe horas y coste y retorna el importe total.
"""
def importe(horas,coste):
    horas=int(input("Introduce las horas del importe: "))
    coste=float(input("Ahora su coste: "))
    return print(f"El importe total es:{horas*coste}€")
print(importe(horas=int,coste=float))