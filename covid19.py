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