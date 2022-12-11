""" 
Naturalmente se emplean muchas librerias a la hora de escribir code, dado que tienen muchas funcionalidades.
Pandas es una libreria que tiene muchas herramientas para realizar analisis de datos y manipularlos, por lo tanto, puede ser una forma de cargar datos de excel.
"""

# Llamamos/importamos la libreria:

import pandas as pd

# Definimos una funcion para cargar datos utilizando el método "pd.read_excel" que es de la libreria pandas
# La funcion cargara los datos del archivo de excel (NombreDelArchivo) en un objeto de tipo "DataFrame"

def cargarDatosExcel(NombreDelArchivo):
  df = pd.read_excel(NombreDelArchivo)
  
  df = df[['Columna1', 'Columna2', 'Columna3']
          
  df = df.sort_values('Columna2')
          
  df = df.drop_duplicates()
          
  return df

df = cargarDatosExcel('NombreArchivoExcel')        
