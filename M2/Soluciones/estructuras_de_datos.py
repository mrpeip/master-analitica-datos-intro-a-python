# Ejercicio 1
numeros = list(range(1, 11))

# Mostrar números pares
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print("Pares:", pares)

# Suma y media
suma = 0
for n in numeros:
    suma += n
media = suma / len(numeros)
print("Suma:", suma)
print("Media:", media)

# Alternativa
suma = sum(numeros)
media = suma / len(numeros)

# Invertir sin reverse() ni slicing
invertida = []
for n in numeros:
    invertida.insert(0, n)
print("Lista invertida:", invertida)

# Alternativa mas clara
invertida = []
for i in range(len(numeros)-1, -1, -1):
    invertida.append(numeros[i])

# Extra: cuadrados
cuadrados = []
for n in numeros:
    cuadrados.append(n*n)
print("Cuadrados:", cuadrados)

# Ejercicio 2

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Por filas:")
for fila in matriz:
    print(fila)

print("\nPor columnas:")
for col in range(3):
    for fila in range(3):
        print(matriz[fila][col], end=" ")
    print()

# Suma diagonal
suma_diag = 0
for i in range(3):
    suma_diag += matriz[i][i]
print("\nSuma diagonal:", suma_diag)

# Extra: transponer
transpuesta = []
for col in range(3):
    nueva_fila = []
    for fila in range(3):
        nueva_fila.append(matriz[fila][col])
    transpuesta.append(nueva_fila)

print("Transpuesta:", transpuesta)

# Ejercicio 3

coordenada = (4, 5, 9)

x, y, z = coordenada
print(x, y, z)

# Intento de modificar (genera error si descomentas la linea de abajo)
# coordenada[0] = 10   # No se puede modificar

def calcular(a, b):
    suma = a + b
    resta = a - b
    return (suma, resta)

resultados = calcular(8, 3)
print(resultados)

# Ejercicio 4
edades = {"Ana": 28, "Luis": 35, "Eva": 42}

# Añadir persona
edades["Mario"] = 31

# Incrementar edades
for nombre in edades:
    edades[nombre] += 1

# Mostrar > 30
for nombre, edad in edades.items():
    if edad > 30:
        print(nombre, edad)

# Extra
mayores_30 = {n:e for n, e in edades.items() if e > 30}
print(mayores_30)

# Ejercicio 5
agenda = {
  "Ana": {"tel": "1234", "email": "ana@mail.com"},
  "Luis": {"tel": "5678", "email": "luis@mail.com"}
}

agenda["Eva"] = {"tel": "9999", "email": "eva@mail.com"}
agenda["Ana"]["email"] = "nuevo_ana@mail.com"

# Mostrar teléfonos
for nombre, datos in agenda.items():
    print(nombre, "=>", datos["tel"])

# Extra: buscar por email
email_buscado = "eva@mail.com"
for nombre, datos in agenda.items():
    if datos["email"] == email_buscado:
        print("Encontrado:", nombre)

# Ejercicio 6

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión: elementos de A ∪ B
union = A | B
print("Unión:", union)

# Intersección: elementos comunes A ∩ B
interseccion = A & B
print("Intersección:", interseccion)

# Diferencia: elementos de A que no están en B → A - B
diferencia = A - B
print("Diferencia:", diferencia)

# Subconjunto
print("{1, 2} es subconjunto de A?", {1, 2}.issubset(A))

# Extra: eliminar duplicados con un set
lista = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = set(lista)
print(sin_duplicados)


# Ejercicio 7

estudiantes = [
  {"nombre": "Ana", "notas": [7, 8, 9]},
  {"nombre": "Luis", "notas": [5, 6, 7]},
  {"nombre": "Eva", "notas": [9, 9, 10]}
]

# Calcular media de cada estudiante
for est in estudiantes:
    est["media"] = sum(est["notas"]) / len(est["notas"])

# Obtener el estudiante con media más alta
mejor = max(estudiantes, key=lambda e: e["media"])
print("Mejor estudiante:", mejor["nombre"], "Media:", mejor["media"])

# Extra: ordenar por media (descendente)
ordenados = sorted(estudiantes, key=lambda e: e["media"], reverse=True)
print(ordenados)


# Ejercicio 8

import re

texto = "Mi número es 123-456-789 y el de Ana es 987-654-321."

# Extraer teléfonos
patron = r"\d{3}-\d{3}-\d{3}"
telefonos = re.findall(patron, texto)
print(telefonos)

# Extraer primeros 3 dígitos
patron_prefijo = r"(\d{3})-\d{3}-\d{3}"
prefijos = re.findall(patron_prefijo, texto)
print(prefijos)

# Extra: reemplazar teléfonos
anonimizado = re.sub(patron, "***-***-***", texto)
print(anonimizado)


# Ejercicio 9

import re

def es_email_valido(email):
    patron = r"^[\w\.-]+@[\w-]+\.(com|es)$"
    return re.match(patron, email) is not None

print(es_email_valido("ana@mail.com"))  # True
print(es_email_valido("mal_email@mail")) # False

# Extra: subdominios
def es_email_valido_sub(email):
    patron = r"^[\w\.-]+@([\w-]+\.)+(com|es)$"
    return re.match(patron, email) is not None

print(es_email_valido_sub("nombre@sub.dominio.com"))  # True

# Ejercicio 10


import re

datos = [
  "Ana, 29, ana@mail.com",
  "Luis, 35, luis@empresa.es",
  "Eva, 42, eva123@dominio.com"
]

usuarios = []

# Regex con 3 grupos de captura: nombre, edad y email
patron = r"^(\w+),\s*(\d+),\s*([\w\.-]+@[\w\.-]+\.\w+)$"

for linea in datos:
    coincidencia = re.match(patron, linea)
    if coincidencia:
        nombre, edad, email = coincidencia.groups()  # Extraemos los 3 grupos
        usuario = {
            "nombre": nombre,
            "edad": int(edad),  # Convertimos a int para comparar numéricamente
            "email": email
        }
        usuarios.append(usuario)

print("Usuarios procesados:", usuarios)

# Mostrar usuarios mayores de 30
print("\nUsuarios mayores de 30:")
for u in usuarios:
    if u["edad"] > 30:
        print(u)

# Extra: ordenar por edad descendente
usuarios_ordenados = sorted(usuarios, key=lambda x: x["edad"], reverse=True)
print("\nOrdenados por edad:", usuarios_ordenados)

# Ejercicio 11
import numpy as np

# Array del 1 al 10
arr = np.arange(1, 11)
print("Array:", arr)

# Cuadrado vectorizado (más eficiente que un bucle)
cuadrado = arr ** 2
print("Cuadrado:", cuadrado)

# Estadísticas básicas
print("Suma:", arr.sum())
print("Media:", arr.mean())
print("Desviación estándar:", arr.std())

# Extra: normalización de array aleatorio
rand_arr = np.random.rand(10)   # valores entre 0 y 1
norm = (rand_arr - rand_arr.mean()) / rand_arr.std()  # Normalización Z-score
print("\nArray aleatorio:", rand_arr)
print("Normalizado:", norm)

# Ejercicio 12
import numpy as np

# Matriz 3x4 con enteros aleatorios entre 0 y 9
mat = np.random.randint(0, 10, (3, 4))
print("Matriz:\n", mat)

# Suma por filas (axis=1) y columnas (axis=0)
print("Suma filas:", mat.sum(axis=1))
print("Suma columnas:", mat.sum(axis=0))

# Máximo y posición
max_val = mat.max()
pos = np.unravel_index(mat.argmax(), mat.shape)  # Convierte índice plano a coordenadas
print("Valor máximo:", max_val, "en posición:", pos)

# Extra: centrar datos restando media de cada columna
media_col = mat.mean(axis=0)
centrada = mat - media_col  # broadcasting: resta cada media a su columna correspondiente
print("\nMatriz centrada:\n", centrada)

# Ejercicio 13

import numpy as np

arr = np.array([3, 7, 2, 9, 4, 10, 5])
print("Original:", arr)

# Elementos > 5
mayores_5 = arr[arr > 5]
print("Mayores que 5:", mayores_5)

# Reemplazar impares por 0
arr_mod = arr.copy()
arr_mod[arr_mod % 2 != 0] = 0  # condición booleana
print("Impares reemplazados por 0:", arr_mod)

# Ordenar de mayor a menor
ordenado = np.sort(arr)[::-1]
print("Ordenado desc:", ordenado)

# Extra: máscara de valores originales > 5
mask = arr > 5
print("Máscara mayores que 5:", mask)
