# Calcular los años bisiestos con los datos ingresados por el usuario a través del teclado:
***
### Requerimientos del ejercicio:

1) Pedir al usuario que ingrese el año de nacimiento.
2) Y también le pediremos el año de muerte; si la persona está con vida, ingresa 0.
***
## A continuacion dejare algunos fragmentos del codigo donde se explica el funccionamiento ya que los commentarios complica mucho la lectura del codigo:
***
- 1) Con la estructura condicional 'if', revisamos si el usuario ingresó un 0. Si la condición se cumple, vamos a reemplazar el 0 por el año en el cual se ejecutará el programa (si lo ejecutamos en 2023, se asignará el año actual).
```
if(año_muerte == 0):
    año_muerte = datetime.now().year
```
***
- 2) Crearemos una lista donde guardaremos los años a revisar, desde el año de nacimiento hasta el año de muerte.
```
lista_años = [año_nacimiento, año_muerte]
```
***
- 3) Con el ciclo 'for', se realizan ingresos de elementos intermedios mediante la instrucción 'append', en otras palabras, rellenaremos los años faltantes que se encuentran entre el año de nacimiento y el año de la muerte o hasta el año presente.
```
for año in range (año_nacimiento+1, año_muerte):
    lista_años.append(año)
```