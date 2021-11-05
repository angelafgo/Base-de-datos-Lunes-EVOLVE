# Venta de automoviles marca Audi

# descargar la librería pandas
# importar las librerías
import pandas as pd

df_audi = pd.read_csv('audi.csv') # Leer el archivo csv
print(df_audi) # Imprimir la información del archivo csv

print('-------------------------------------------------------------------------------------')
print(df_audi.head(20)) # las primeras 20 filas del archivo csv

print('-------------------------------------------------------------------------------------')
print(df_audi.shape) # Número de columnas y filas del archivo csv

print('-------------------------------------------------------------------------------------')
# ¿Queremos una columna en específico?
print(df_audi['Nombre'])

print('-------------------------------------------------------------------------------------')
# 2 columnas a la vez
print(df_audi[['id','Venta por']]) # Para poder colocar varias listas se tienen que poner doble corchete

print('-------------------------------------------------------------------------------------')
# Promedio
# error no se puede convertir a numerico y de tal manera convertirlo a promedio
print(df_audi['Venta por'].mean())

print('-------------------------------------------------------------------------------------')
# Resumen de las estadísticas que decribe el data frame
print(df_audi.describe())
