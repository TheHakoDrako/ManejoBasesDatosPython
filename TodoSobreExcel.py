import pandas as pd

def cargarDatosExcel(NombreDelArchivo):
  df = pd.read_excel(NombreDelArchivo)
  
  df = df[['Columna1', 'Columna2', 'Columna3']
          
  df = df.sort_values('Columna2')
          
  df = df.drop_duplicates()
          
  return df

df = cargarDatosExcel('NombreArchivoExcel')        
