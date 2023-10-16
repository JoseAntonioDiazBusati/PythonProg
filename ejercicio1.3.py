"""
1.4 => NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.
"""
def farenheit():
    grados=float(input("Introduce grados Farenheit: "))
    return grados*0.32
print(f"Esos grados farenheit equivalen a {farenheit()}ºC")