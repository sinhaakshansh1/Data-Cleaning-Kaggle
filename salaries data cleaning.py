# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:25:48 2024

@author: aksha
"""

import pandas as pd
import numpy as np
import re
salaries = pd.read_csv("C:/Users/aksha/Downloads/salaries.csv")

sujetoobligado_data = salaries['sujetoobligado']

#resolving first issue
def CamelCase(s):
    words = s.split()
    final_string = ' '.join(i.capitalize() for i in words)
    
    return (final_string)
sujetoobligado_data = sujetoobligado_data.apply(CamelCase)
print(sujetoobligado_data)

#resolving second and third issue
nombre_data = salaries['nombre']

def CamelCasenombre(name):
    words = str(name).split()
    final_string = ' '.join(i.capitalize() for i in words)
    
    return (final_string)
nombre_data=nombre_data.apply(CamelCasenombre)
nombre_data = nombre_data.fillna(np.nan)
print(nombre_data)
        
#resolving fourth and fifth issue
denominacion_data = salaries['denominacion']
def CamelCasedenominacion(name):
    words = str(name).split()
    final_string = ' '.join(i.capitalize() for i in words)
    
    return (final_string)
denominacion_data=denominacion_data.apply(CamelCasedenominacion)
denominacion_data = denominacion_data.fillna(np.nan)
print(denominacion_data)

#resolving sixth issue
montoneto_data = salaries['montoneto'].astype(float)
print(montoneto_data)

#resolving seventh issue
montoneto_data = montoneto_data.fillna(np.nan)
print(montoneto_data)

#resolving eigth and ninth issue
cargo_data = salaries['cargo']
def CamelCasecargo(name):
    words = str(name).split()
    final_string = ' '.join(i.capitalize() for i in words)
    
    return (final_string)
cargo_data=cargo_data.apply(CamelCasecargo)
cargo_data = cargo_data.fillna(np.nan)
print(cargo_data)

#resolving tenth and eleventh issue
area_data = salaries['area']
def CamelCasearea(name):
    words = str(name).split()
    final_string = ' '.join(i.capitalize() for i in words)
    
    return (final_string)
area_data=area_data.apply(CamelCasearea)
area_data = area_data.fillna(np.nan)
print(area_data)

#resolving twelfth issue
montobruto_data = salaries['montobruto'].astype(float)
print(montobruto_data)

#resolving thirteenth issue
montobruto_data = montobruto_data.fillna(np.nan)
print(montobruto_data)
        
salaries.columns.values
salaries = salaries.loc[:,['nombre', 'denominacion', 'montoneto', 'cargo', 'area', 'montobruto',
       'idInformacion', 'periodoreportainicio','periodoreportafin']]
salaries.to_csv('salaries_cleaned.csv', index=False)    