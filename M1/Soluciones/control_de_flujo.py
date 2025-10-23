# Ejercicio 1 – Imprimir elementos de una lista
print("Ejercicio 1:")
nombres = ["Ana", "Luis", "Carlos", "María", "Sofía"]
for nombre in nombres:
    print(nombre)
print()

# Ejercicio 2 – Suma de números en una lista
print("Ejercicio 2:")
numeros = [1, 2, 3, 4, 5]
suma = 0
for n in numeros:
    suma += n
print("La suma es:", suma)
print()

# Ejercicio 3 – Contar caracteres
print("Ejercicio 3:")
palabra = input("Introduce una palabra: ")
contador = 0
for letra in palabra:
    contador += 1
print("La palabra tiene", contador, "letras")
print()

# Ejercicio 4 – Multiplicar números
print("Ejercicio 4:")
numeros = [2, 4, 6, 8]
multiplicados = []
for n in numeros:
    multiplicados.append(n * 3)
print("Lista multiplicada:", multiplicados)
print()

# Ejercicio 5 – Filtrar números pares
print("Ejercicio 5:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print("Números pares:")
for n in numeros:
    if n % 2 == 0:
        print(n)
print()

# Ejercicio 6 – Iterar sobre un diccionario
print("Ejercicio 6:")
estudiantes = {
    "Ana": 8,
    "Luis": 4,
    "Carlos": 7,
    "Maria": 3
}
print("Estudiantes aprobados:")
for nombre, nota in estudiantes.items():
    if nota >= 5:
        print(nombre, "ha aprobado con nota", nota)
print()

# Ejercicio 7 – Contar letras en un string
print("Ejercicio 7:")
texto = input("Introduce un texto: ")
contador_a = 0
for letra in texto:
    if letra.lower() == "a":
        contador_a += 1
print("La letra 'a' aparece", contador_a, "veces")
print()

# Ejercicio 8 – Sumar hasta un número con while
print("Ejercicio 8:")
i = 1
suma = 0
while i <= 10:
    suma += i
    i += 1
print("La suma del 1 al 10 es:", suma)
print()

# Ejercicio 9 – Implementar un for tradicional
"""
En C o Java sería algo así:

for(int i=0; i<9; i+=2)
{
    System.out.println(i);
}
"""
for i in range(0, 9, 2):
    print(i)

# Range usa tres parámetros:
# 1. Valor inicial (0)
# 2. Valor final (9)
# 3. Paso (2), que indica cuánto se incrementa i en cada iteración.
print()

# Ejercicio 10 – Invertir una lista
print("Ejercicio 10:")
lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(
    len(lista) - 1,
      -1,
        -1):
    invertida.append(lista[i])
print("Lista invertida:", invertida)
print()

"""
Explicación Ejercicio 11:

len(lista) → devuelve el número de elementos (en este caso, 5).

len(lista) - 1 → es el último índice válido (4, porque los índices empiezan en 0).

El segundo parámetro -1 → indica que el bucle debe parar antes de llegar a -1 (es decir, se detiene en 0).

El tercer parámetro -1 → es el paso, o sea, que el bucle va hacia atrás (restando 1 en cada paso).
"""


# Ejercicio 11 – Ordenar una lista sin usar sort()
print("Ejercicio 11:")
numeros = [5, 2, 8, 1, 3]
# Implementación de ordenación tipo burbuja (bubble sort)
for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print("Lista ordenada:", numeros)
print()


"""
Explicación Ejercicio 11:

El primer bucle for itera sobre cada elemento de la lista.

El segundo bulcle itera desde 0 hasta el tamaño de la lista menos el valor
actual, y menos uno más (porque los últimos elementos ya están ordenados).

Dentro del segundo bucle, se compara el elemento actual con el siguiente.
Si el actual es mayor que el siguiente, se intercambian sus posiciones.
"""