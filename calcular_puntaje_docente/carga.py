import pandas as pd
import os
from datos_personales import *

""" Cargando excel original """
dt_entrada = pd.read_excel('Pruebas')

"""Funcion para capturar los datos personales"""
def datosPersonales(dt_entrada, i):
	apellido = dt_entrada.iloc[i]['Apellido/s (Tal como figura en su DNI. Ej: PEREZ)']
	nombre = dt_entrada.iloc[i]['Nombre/s (Tal como figura en su DNI. Ej: BLANCA TERESA)']
	dni = dt_entrada.iloc[i]['DNI (Sólo colocar números, sin puntos. Ej: 11222333 )']
	ejercico_docencia = dt_entrada.iloc[i]['¿Se encuentra actualmente en ejercicio de la docencia?']
	ies = dt_entrada.iloc[i]['Indique el o los IES en los que actualmente se encuentra ejerciendo la docencia o integrando algún departamento o coordinación. ']
	region = dt_entrada.iloc[i]['Marque la o las Regiones Educativas en donde se encuentra ejerciendo la docencia']
	nivel_postulacion = dt_entrada.iloc[i]['Especifique el Nivel en el que se postula como Formador Tutor']

"""Funcion para calcular la categoria de puntajes Formacion Academica"""
def formacionAcademica(dt_entrada,i):

	"""Titulos Docente"""
	cant_titulo_docenete = dt_entrada.iloc[i]['¿Cuántos títulos docente posee?']
	if cant_titulo_docenete == 'Posee 1 título docente':
		cant_titulo_docenete = 5
	if cant_titulo_docenete == 'Posee 2 títulos':
		cant_titulo_docenete = 6
	if cant_titulo_docenete == 'Posee más de 2 títulos':
		cant_titulo_docenete = 7
	if cant_titulo_docenete == 'No posee':
		cant_titulo_docenete = 0

	"""Otros Titulos"""
	otro_titulo = dt_entrada.iloc[i]['¿Cuántos títulos docente posee?']







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