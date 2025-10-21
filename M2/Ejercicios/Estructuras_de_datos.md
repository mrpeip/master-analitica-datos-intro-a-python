## Ejercicio 1: Listas básicas

Crea una lista con los números del 1 al 10.  

    Muestra los números pares.  
    Calcula la suma y la media.  
    Invierte la lista sin usar `reverse()` ni `[::-1]`.

**Extra:** Crea una nueva lista con los cuadrados de los números.


## Ejercicio 2: Matrices (listas de listas)

Crea una matriz 3x3 con los números del 1 al 9.

    Imprime los elementos por filas y columnas.

    Calcula la suma de la diagonal principal.

**Extra:** Transpone la matriz (intercambia filas por columnas).


## Ejercicio 3: Tuplas inmutables

Dada la tupla:

coordenada = (4, 5, 9)

    Desempaqueta la tupla en las variables x, y, z.

    Intenta modificar x y observa qué ocurre.


**Extra:** Usa una tupla para devolver múltiples valores de una función.

## Ejercicio 4: Diccionarios simples

Crea un diccionario con las edades de tres personas.

    Añade una nueva persona.

    Incrementa todas las edades en 1.

    Muestra los nombres de las personas mayores de 30 años.

**Extra:** Usa comprensión de diccionarios para crear un nuevo diccionario con solo los mayores de 30.


## Ejercicio 5: Diccionarios anidados

Crea un diccionario que represente una agenda:

agenda = {
  "Ana": {"tel": "1234", "email": "ana@mail.com"},
  "Luis": {"tel": "5678", "email": "luis@mail.com"}
}

    Añade un nuevo contacto.

    Cambia el email de Ana.

    Muestra todos los teléfonos.

**Extra: Busca un contacto por email.**


## Ejercicio 6: Conjuntos (sets)

Dado:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

    Calcula la unión, intersección y diferencia.

    Comprueba si {1, 2} es subconjunto de A.

**Extra:** Convierte una lista con duplicados en un set para eliminar repeticiones.

## Ejercicio 7: Combinando estructuras

Crea una lista de diccionarios con información de estudiantes:

estudiantes = [
  {"nombre": "Ana", "notas": [7, 8, 9]},
  {"nombre": "Luis", "notas": [5, 6, 7]},
  {"nombre": "Eva", "notas": [9, 9, 10]}
]

    Calcula la nota media de cada estudiante.

    Muestra el nombre del que tiene la media más alta.

**Extra:** Ordena la lista de estudiantes por su nota media.

## Ejercicio 8: Regex básicas

Dado el texto:

texto = "Mi número es 123-456-789 y el de Ana es 987-654-321."

    Usa re.findall() para extraer todos los números de teléfono (formato XXX-XXX-XXX).

    Extrae solo los tres primeros dígitos de cada teléfono.

**Extra:** Reemplaza todos los teléfonos por "***-***-***" usando re.sub().

## Ejercicio 9: Regex con validaciones

Crea una función es_email_valido(email) que devuelva True si el email es válido.

Regla básica:
Debe contener un @ y un dominio tipo .com o .es.

**Extra:** Mejora la expresión para aceptar subdominios (por ejemplo, nombre@sub.dominio.com).


## Ejercicio 10: Ahora todo junto

Escribe un programa que lea una lista de cadenas con datos de usuarios:

datos = [
  "Ana, 29, ana@mail.com",
  "Luis, 35, luis@empresa.es",
  "Eva, 42, eva123@dominio.com"
]

    Usa regex para extraer nombre, edad y email.

    Guarda cada usuario en un diccionario.

    Crea una lista de diccionarios con todos los usuarios.

    Muestra los usuarios mayores de 30 años.

**Extra:** Ordena la lista por edad descendente.

## Ejercicio 11: NumPy - Creación y operaciones básicas

Crea un array con los números del 1 al 10.

    Calcula el cuadrado de todos los elementos sin usar bucles.

    Obtén la suma, la media y la desviación estándar del array.

**Extra:** Crea un array de números aleatorios entre 0 y 1 y normalízalo.

## Ejercicio 12: NumPy - Matrices y ejes

Crea una matriz 3x4 con números enteros aleatorios entre 0 y 9.

    Calcula la suma por filas y por columnas.

    Encuentra el valor máximo y su posición.

**Extra:** Resta la media de cada columna a todos sus elementos (centrado de datos).

## Ejercicio 13: NumPy - Indexación y filtrado

Dado el array:

arr = np.array([3, 7, 2, 9, 4, 10, 5])

    Extrae los elementos mayores que 5.

    Reemplaza los valores impares por 0.

    Ordena el array de mayor a menor.

**Extra:** Crea una máscara booleana que indique cuáles eran los valores originales mayores que 5.