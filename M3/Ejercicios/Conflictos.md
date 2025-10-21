## Paso 1: Crear main

Crea una nueva rama desde main y llamala main_con_conflicto.

Clona la rama main_con_conflicto en local.

Añade este código:

```python
def suma(a, b):
    resultado = a + b
    print(f"La suma de {a} + {b} = {resultado}")
    return resultado

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

```

Guarda los cambios en un commit, y haz push a main_con_conflicto en GitHub.

## Paso 2: Crea dos nuevas ramas

Crea una nueva rama desde main_con_conflicto y llamala feature1.

Crea otra nueva rama desde main_con_conflicto y llamala feature2.

## Paso 3: Cambios en feature1

Modifica el código de la rama feature1 como veas.

Guarda los cambios en un commit, y haz push a feature1 en GitHub.

## Paso 4: Cambios en feature2

Modifica el código de la rama feature2 como veas, pero de manera distinta a feature1.

Guarda los cambios en un commit, y haz push a feature2 en GitHub.

## Paso 5: Unir feature1 con main_con_conflicto

Desde GitHub, crea una Pull Request desde feature1 a main_con_conflicto y mergea los cambios.

## Paso 6: Unir feature2 con main_con_conflicto

Desde GitHub, crea una Pull Request desde feature2 a main_con_conflicto y observa el resultado.

## Paso 7: Resolviendo conflictos

Resuelve los conflictos de las dos maneras que vimos.