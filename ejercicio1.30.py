"""
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a 
que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
El pseudocódigo debes incluirlo como comentarios en el programa de Python.

Inicio
Leemos num_inicio
Leemos num_incremento
Leemos tot_serie
Si num_incremento = 0  mostramos Error no puede ser menor que 0
Si totserie = 0  mostramos Error no puede ser menor que 0
Mientras 
Final
"""
num_inicio=int(input("Introduce un numero de inicio: "))
num_incremento=int(input("Ahora el incremento: "))
tot_serie=int(input("Por ultimo el total de la serie: "))
cont=1
if(num_incremento==0):
    print("Error no puede ser menor que 0.")
else:
    ser="{num_incremento}-{plus}".format(num_inicio=num_inicio,plus=(num_inicio+num_incremento))
    while(cont<tot_serie-2):
        num_inicio+=num_incremento
        ser="{ser}..{num_incremento}".format(num_inicio=num_inicio,plus=(num_inicio+num_incremento))
        cont+=1
        ser="{ser}-{plus}".format(ser=ser,plus=(num_inicio+num_incremento))