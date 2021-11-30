# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:28:47 2021

@author: amand
"""
import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# 1. Número de casos de contagios del país

num_casos = data.shape[0]
print(f'El número de casos de contagiados en el país es de: {num_casos}')

# 2. Números de municipios afectados

num_municipios = len(data.groupby('Nombre municipio').size())
print(f'El número de municipios afectados es: {num_municipios}')

# 3. Liste los municipios afectados (sin repetir)

lista_mpio = data.groupby('Nombre municipio').size().sort_values(ascending=False)
print(f'\nMunicipios afectados: {lista_mpio}')

# 4. Número de personas que se encuentran en atención en casa

data['Ubicación del caso'].replace('Casa', 'CASA', inplace=True)
data['Ubicación del caso'].replace('casa', 'CASA', inplace=True) 

atencion_casa = len(data[data['Ubicación del caso'] == 'CASA'])
print(f'Número de personas que se encuentran con atención en casa: {atencion_casa}')

# 5. Número de personas que se encuentran recuperados

num_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'El total de  personas recuperada es de: {num_recuperados}') 

# 6. Número de personas que ha fallecido

num_fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]
print(f'El número de personas que han fallecido es de: {num_fallecidos}')

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)

tipo_caso = data.groupby('Tipo de contagio').size().sort_values(ascending=False)
print(f'{tipo_caso}')

# 8. Número de departamentos afectados

num_dpto = len(data.groupby('Nombre departamento').size())
print(f'{num_dpto} departamentos fueron afectados')

# 9.Liste los departamentos afectados(sin repetirlos)

data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)
data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)

lista_dpto = data.groupby('Nombre departamento').size().sort_values(ascending=False)
print(f'Departamentos afectados: {lista_dpto}')

# 10. Ordene de mayor a menor por tipo de atención

tipo_atencion = data.groupby('Ubicación del caso').size().sort_values(ascending=False)
print(f'{tipo_atencion}')

# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados

dptos = data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con más casos de contagios son: {dptos}')

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

dpto_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'Departamentos con más casos fallecidos: {dpto_fallecidos}')

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados

dpto_recuperados = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'Depaetamentos con más casos recuperados: {dpto_recuperados}')

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados

lista_mcontagiados = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'Los 10 municipios más contagiados: {lista_mcontagiados}')

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos

mpio_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'Municipios con más casos fallecidos: {mpio_fallecidos}')

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados

mpio_recuperado = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'Municipios con más casos recuperados: {mpio_recuperado}')

# 17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados

dpto_ciudades = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)
print(f'Ciudades con más casos de contagio: {dpto_ciudades}')

# 18. Número de Mujeres y hombres contagiados por ciudad por departamento

num_personas = data.groupby(['Nombre departamento', 'Nombre municipio','Sexo']).size().sort_values(ascending=False)
print( f' {num_personas}')

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por
# ciudad por departamento

promedio_edad = data.groupby( ['Nombre departamento', 'Nombre municipio', 'Sexo']).Edad.mean()
print(f'{promedio_edad}')

20. Liste de mayor a menor el número de contagiados por país de
procedencia

lista_procedencia = data['Nombre del país'].value_counts()
print(f' Número de contagiados por país: {lista_procedencia}')   
