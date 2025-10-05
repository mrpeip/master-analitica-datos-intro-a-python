**Ejercicio 1 – Función simple**

Crea una función saludar() que imprima en pantalla "¡Hola, mundo!".

**Ejercicio 2 – Parámetros y argumentos**

Define una función saludo_personal(nombre) que reciba un nombre como parámetro y muestre un saludo personalizado, por ejemplo:

"¡Hola, Ana!"

**Ejercicio 3 – Valor de retorno**

Crea una función area_rectangulo(base, altura) que devuelva el área.


**Ejercicio 4 – Valores por defecto**

Escribe una función potencia(base, exponente=2) que devuelva el resultado de elevar base al exponente.

Si no se proporciona exponente, que use 2 por defecto.

**Ejercicio 5 – Funciones con múltiples retornos**

Crea una función analisis_lista(numeros) que reciba una lista de números y devuelva una lista con:

- El número máximo.

- El número mínimo.

- El promedio.

**Ejercicio 6 - Funciones anidadas**

Crea una función operaciones(a, b) que contenga tres funciones internas: suma, resta, multiplicacion.

Haz que operaciones() devuelva un diccionario con los tres resultados.

**Ejercicio 7 - Funciones recursivas**

Define una función recursiva factorial(n) que calcule el factorial de un número entero positivo.

Ejemplo: factorial(5) → 120.

**Ejercicio 8 - Llamar una función desde otra**

Crea dos funciones:

- cuadrado(n) → devuelve el número al cuadrado.

- doble_cuadrado(n) → usa cuadrado() y devuelve el doble del cuadrado.

Prueba con varios valores.

**Ejercicio 9 - Contador de vocales**

Escribe una función contar_vocales(texto) que devuelva cuántas vocales hay en una cadena.
Luego, crea un programa que pida al usuario frases y muestre el número de vocales hasta que escriba "fin".

**Ejercicio 10 - Adivina el número**

Crea una función comprobar_intento(secreto, intento) que:

devuelva "mayor" si el intento es menor que el secreto,

"menor" si el intento es mayor,

y "acertaste" si son iguales.

El juego no debe terminar hasta que el jugador acierte el número, o se equivoque 4 veces.


**Ejercicio 11 - Ejemplo de POO**

Crea una clase Calculadora con los métodos:

sumar(a, b)

restar(a, b)

multiplicar(a, b)

dividir(a, b)

Crea una instancia de la clase y prueba los métodos.

**Ejercicio 12 - Ejemplo de funcional**

**Parte 1: Aplicar una función usando otra**

Crea una función llamada aplicar_funcion(lista, funcion) que:

Reciba una lista de valores y una función suma.

Cree una nueva lista aplicando esa función a cada elemento.

Devuelva la nueva lista.

**Parte 2: Reutiliza la función con distintos comportamientos**

Crea otras funciones y pásalas como argumento:

restar, multiplicar, dividir.

**Parte 3: Composición de funciones**

Implementa una función:

componer(f, g) 

Que devuelva una nueva función que aplique primero g, luego f.