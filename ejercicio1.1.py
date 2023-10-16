"""
1.1 => recibe un nombre y retorna una cadena de caracteres con el resultado.

"""
def nombre():
    nom=str(input("Introduce un nombre: "))
    return nom
print(f"Hola {nombre()}")