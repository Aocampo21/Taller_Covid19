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