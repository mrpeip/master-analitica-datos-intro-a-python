## Ejercicio 1:

Dado este Dataframe:

datos = {
    'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
    'Ventas': [150, 200, 180, 220, 250, 300],
    'Gastos': [80, 90, 85, 100, 110, 120]
}

df_ventas = pd.DataFrame(datos)

Crea un gráfico de línea con matplotlib que muestre Ventas y Gastos por Mes

Usa diferentes colores y agrega una leyenda

## Ejercicio 2:

Dado este DataFrame:

datos_productos = {
    'Producto': ['A', 'B', 'C', 'D', 'E'],
    'Ventas_2023': [450, 320, 580, 210, 390],
    'Ventas_2024': [520, 380, 610, 250, 420]
}

df_productos = pd.DataFrame(datos_productos)

Crea un gráfico de barras comparando ventas 2023 vs 2024 usando seaborn y matplotlib

Pista: Puedes usar melt() para transformar el DataFrame

## Ejercicio 3:

Dado este DataFrame:

np.random.seed(42)
datos_empleados = {
    'Salario': np.random.normal(50000, 15000, 200),
    'Edad': np.random.randint(22, 65, 200),
    'Departamento': np.random.choice(['Ventas', 'TI', 'Marketing', 'RH'], 200)
}

df_empleados = pd.DataFrame(datos_empleados)

Crea un subplot con 2 filas y 2 columnas que contenga:

1. Histograma de Salarios
2. Boxplot de Salarios por Departamento
3. Scatter plot de Salario vs Edad
4. Gráfico de densidad de Edad

## Ejercicio 4:

np.random.seed(123)
datos_complejos = {
    'Ingresos': np.random.normal(5000, 1500, 100),
    'Publicidad': np.random.normal(1000, 300, 100),
    'Clientes': np.random.normal(200, 50, 100),
    'Satisfaccion': np.random.uniform(1, 10, 100),
    'Ventas': np.random.normal(10000, 2000, 100)
}

df_correlacion = pd.DataFrame(datos_complejos)

Crea un heatmap de correlaciones usando seaborn

Incluye anotaciones con los valores de correlación

## Ejercicio 5:
```python
fechas = pd.date_range('2023-01-01', periods=365, freq='D')

datos_temporales = {
    'Fecha': fechas,
    'Ventas': np.random.normal(1000, 200, 365) + np.sin(np.arange(365) * 2 * np.pi / 30) * 100,
    'Temperatura': np.random.normal(25, 5, 365) + np.sin(np.arange(365) * 2 * np.pi / 365) * 10
}

df_temporal = pd.DataFrame(datos_temporales)

df_temporal['Mes'] = df_temporal['Fecha'].dt.month
```
Crea los siguientes gráficos:

1. Gráfico de línea de Ventas a lo largo del tiempo
2. Gráfico de promedio mensual de Ventas
3. Relación entre Temperatura y Ventas

## Ejercicio 6:

```python
np.random.seed(789)
n_registros = 1000

datos_ecommerce = {
    'edad': np.random.randint(18, 70, n_registros),
    'ingresos_anuales': np.random.normal(50000, 20000, n_registros),
    'compras_mensuales': np.random.poisson(5, n_registros),
    'monto_promedio_compra': np.random.normal(150, 50, n_registros),
    'satisfaccion_cliente': np.random.randint(1, 11, n_registros),
    'categoria_favorita': np.random.choice(['Electrónicos', 'Ropa', 'Hogar', 'Deportes'], n_registros),
    'dias_ultima_compra': np.random.exponential(30, n_registros)
}

df_ecommerce = pd.DataFrame(datos_ecommerce)
df_ecommerce['gasto_total'] = df_ecommerce['compras_mensuales'] * df_ecommerce['monto_promedio_compra']
```

Crea un reporte completo de visualizaciones que incluya:

1. Perfil demográfico de los clientes
2. Análisis de comportamiento de compra
3. Relación entre variables
4. Segmentación por categoría favorita
5. Recomendaciones basadas en los hallazgos