import pandas as pd
import os
from datos_personales import *

""" Cargando excel original """
dt_entrada = pd.read_excel('Pruebas')

"""Recorriendo Excel"""
i = 0
while i <= len(dt_entrada.index):
	guardarDatosPersonales.nombre(i,dt_entrada)



"""Creando nuevo excel"""

data = {}

dt_salida = pd.create_excel('puntaje'. columns = ['Apellido', 'Nombre', 'DNI', 'Ejercicio docencia', 'IES', 'Región',
 'Nivel para el que se postula', 'Tit_Doc', 'Otro_tit', 'Post', 'F_Ac', 'Exp_doc_niv', 'Exp_doc_sist', 'Ant', 
 'Area_cap', 'Dest', 'Tic', 'Rol', 'A_V', 'Frec_A_V', 'Tic_Rol', 'Aulas_Virtuales', 'Exp_laborales', 
 'Comp_dig_correg', 'Cap_prof', 'Puntaje_final'])