## Ejercicio 1: Nombres claros y significativos

El siguiente código funciona, pero los nombres de variables y funciones son confusos.

    Refactorízalo para que sea más legible.

```python
def f(x, y):
    z = x * y
    if z > 100:
        return z / 10
    else:
        return z + 10

a = 12
b = 9
print(f(a, b))
```

## Ejercicio 2: Eliminar código duplicado

El siguiente código repite la misma lógica. 

    Refactorízalo para evitar duplicación.

```python
def calcular_descuento_producto1(precio):
    return precio - (precio * 0.1)

def calcular_descuento_producto2(precio):
    return precio - (precio * 0.8)
```

## Ejercicio 3: Separación de responsabilidades

Divide este código en funciones más pequeñas y con una responsabilidad clara.

```python
def procesar_ventas(ventas):
    total = 0
    for venta in ventas:
        print("Procesando venta:", venta)
        total += venta
    print("Total de ventas:", total)
    promedio = total / len(ventas)
    print("Promedio de venta:", promedio)
```

## Ejercicio 4: Comentarios innecesarios vs útiles

El siguiente código tiene comentarios redundantes o confusos.

    Refactoriza la función para seguir todos los estándares.

```python
# Esta función suma dos números
def suma(a, b):
    # Suma los dos parámetros
    resultado = a + b  # guarda el resultado
    # Devuelve el resultado
    return resultado
```

## Ejercicio 5: Manejo claro de errores

Refactoriza este código para manejar los errores correctamente y con mensajes claros.

```python
def dividir(a, b):
    return a / b

print(dividir(10, 0))
```

## Ejercicio 6: Efectos secundarios

Arregla este código para que se comporte de manera correcta.

```python
total = 0

def agregar_venta(monto):
    global total
    total += monto
    print("Venta agregada:", monto)
```

## Ejercicio 7: Espagueti

Refactoriza esta desgracia para que sea buen código.

```python
usuarios = ["ana", "luis", "carlos"]
edades = [19, 30, 17]

for i in range(len(usuarios)):
    if edades[i] >= 18:
        print(usuarios[i], "es mayor de edad")
    else:
        print(usuarios[i], "es menor de edad")
```

# Ejercicio 9: Buscar duplicados

Escribe una función que reciba una lista y devuelva una nueva lista con los valores duplicados.

Una vez terminado:

    Analiza su complejidad usando bigO

    Piensa si existe alguna forma de hacerlo mejor y trata de implementarla
