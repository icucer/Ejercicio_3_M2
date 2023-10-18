# Desde modulo datetime importaremos la clase con el mismo nombre (datetime).
from datetime import datetime

# Encabezado y nombre del programa.
print ("\n *******************************")
print ("*  Calculador de años bisiestos *")
print ("\n *******************************")

# Ingresar año inicial y final del rango de búsqueda:
año_nacimiento = int (input ("\nIngresa el año de nacimiento:\n"))
año_muerte = int (input ("\nIngresa el año de muerte, de otra forma ingresa un '0':\n"))

# 1) para el funcionamiento revisar README.md
if(año_muerte == 0):
    año_muerte = datetime.now().year

# 2) para el funcionamiento revisar README.md
lista_años = [año_nacimiento, año_muerte]

# 3) para el funcionamiento revisar README.md
for año in range (año_nacimiento+1, año_muerte):
    lista_años.append(año)

# Creación de variables y asignación de valores.
años_bisiest_siglo = 0
años_bisiest = 0

# Con el siguiente ciclo revisaremos cual din los años que estan en la lista son bisiestos:
for año in lista_años:

    # Con el if se revisarán los años del siglo.
    if año % 100 == 0 and año % 400 == 0:
        años_bisiest_siglo += 1

    # Con elif se revisarán los demás años.
    elif año % 100 != 0 and año % 4 == 0:
        años_bisiest += 1

# Y finalmente imprimiremos por pantalla la cantidad de años bisiestos.
print(f"\nLa cantidad de años bisiestos en este periodo fueron: {años_bisiest_siglo + años_bisiest}\n")