# SP - Venta de automoviles marca Audi
# EVOLVE - 8 Octubre 2021
# SAITD 2021-2022

# Importar todas las librerías necesarias para el análisis
import pandas as pd                
import matplotlib.pyplot as plt    # librería que genera gráficas a partir de datos contenidos en listas.
import seaborn as sns              # librería de visualización de datos para Python, crea atractivas gráficas.
import numpy as np                 # librería especializada en cálculo numérico
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings

# revisar si es necesario 
#% matplotlib inline                
 # ^ Nos permite ver las graficas al momento de pedirlas

# Importar el csv
df_audi = pd.read_csv('audi.csv') # Leer el archivo csv
print(df_audi) # Imprimir la información del archivo csv

# Conocer el Precio de Venta de los automoviles
print('-------------------------------------------------------------------------------------')
print('             Resumen de la columna de "Venta por" de cada automóvil comprado         ')
print(df_audi['Venta por'].describe())
