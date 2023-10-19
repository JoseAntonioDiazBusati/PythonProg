"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 365 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 12 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio

Escribe "Introduce los dias trabajados: "
Lee dias
Mientras dias sea menor que cero entonces:
    Escribe "*** Error - el valor no puede ser negativo ***"
    Lee dias
año=dias//360
dias_mes=dias%360
mes=dias_mes//30
dias_restantes=dias_mes%30
Si año es uno entonces:
    Escribe "Ha cotizado {año} año,",end=""
Sino:
    "Ha cotizado {año} años,",end=""
Si mes es uno entonces:
    Escribe " {mes} mes,",end=""
Sino:
    Escribe " {mes} meses,",end=""
Si día es uno entonces:
    Escribe " {día_restante} día.",end=""
Sino:
    Escribe " {dia_restante} días.",end=""
  
Fin
"""
dias=int(input("Introduce los dias trabajados: "))
while dias<0:
    print("*** Error - el valor no puede ser negativo ***")
    dias=int(input("Introduce los dias trabajados: "))
año=dias//360
dias_mes=dias%360
mes=dias_mes//30
dias_restantes=dias_mes%30  
if año==1:
    print(f"Ha cotizado {año} año,",end="")
else:
    print(f"Ha cotizado {año} años,",end="")
if mes==1:
    print(f" {mes} mes,",end="")
else:
    print(f" {mes} meses,",end="")
if dias_restantes==1:
    print(f" {dias_restantes} día.",end="")
else:
    print(f" {dias_restantes} días.",end="")