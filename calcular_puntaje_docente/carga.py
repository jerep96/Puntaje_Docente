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
	cant_titulo_docente = dt_entrada.iloc[i]['¿Cuántos títulos docente posee?']
	if cant_titulo_docente == 'Posee 1 título docente':
		cant_titulo_docente = 5
	if cant_titulo_docente == 'Posee 2 títulos':
		cant_titulo_docente = 6
	if cant_titulo_docente == 'Posee más de 2 títulos':
		cant_titulo_docente = 7
	if cant_titulo_docente == 'No posee':
		cant_titulo_docente = 0

	"""Otros Titulos"""
	otro_titulo = dt_entrada.iloc[i]['Si respondió "Sí" en la respuesta anterior, por favor indique el área de su/s título/s. De lo contrario continúe completando el formulario']
	if otro_titulo = 'Ciencias Exactas y Naturales ':
		otro_titulo = 1
	if otro_titulo = 'Ciencias de la Salud':
		otro_titulo = 1
	if otro_titulo = 'Ciencias Sociales- Humanidades- Artística':
		otro_titulo = 3
	if otro_titulo = 'Educación Física':
		otro_titulo = 1
	if otro_titulo = 'Informática-Tecnología':
		otro_titulo = 3
	if otro_titulo = 'No posee':
		otro_titulo = 0

	"""Titulo de Postitulo"""
	postitulo = dt_entrada.iloc[i]['¿Posee alguna formación de posgrado /postítulo, indique por favor la/s carrera/s?']
	doctorado = dt_entrada.iloc[i]['Indique por favor la etapa en la que se encuentra en dicha formación de posgrado/postítulo. [Doctorado]']
	maestria = dt_entrada.iloc[i]['Indique por favor la etapa en la que se encuentra en dicha formación de posgrado/postítulo. [Maestría]']
	especializacion = dt_entrada.iloc[i]['Indique por favor la etapa en la que se encuentra en dicha formación de posgrado/postítulo. [Especialización]']
	diplomatura = dt_entrada.iloc[i]['Indique por favor la etapa en la que se encuentra en dicha formación de posgrado/postítulo. [Diplomatura]']
	actualizacion_academica = dt_entrada.iloc[i]['Indique por favor la etapa en la que se encuentra en dicha formación de posgrado/postítulo. [Actualización Académica]']
	if postitulo == 'No posee':
		postitulo = 0
	elif postitulo == 'Doctorado':
		if doctorado == 'Recibido/a':
			postitulo = 4
		elif doctorado == 'Finalizando el cursado de la carrera' || doctorado == 'Tesis pendiente':
			postitulo = 1
		else:
			postitulo = 0
	elif postitulo == 'Maestría':
		if maestria == 'Recibido/a':
			postitulo = 3
		elif maestria == 'Finalizando el cursado de la carrera' || maestria == 'Tesis pendiente':
			postitulo = 1
		else:
			postitulo = 0
	elif postitulo == 'Especialización':
		if especializacion == 'Recibido/a':
			postitulo = 3
		elif especializacion == 'Finalizando el cursado de la carrera' || especializacion == 'Tesis pendiente':
			postitulo = 1
		else:
			postitulo = 0
	elif postítulo == 'Diplomatura':
		if diplomatura == 'Recibido/a':
			postitulo = 3
		elif diplomatura == 'Finalizando el cursado de la carrera' || diplomatura == 'Tesis pendiente':
			postitulo = 1
		else:
			postitulo = 0
	elif postitulo == 'Actualización Académica':
		if actualizacion_academica == 'Recibido/a':
			postitulo = 3
		elif actualizacion_academica == 'Finalizando el cursado de la carrera' || actualizacion_academica == 'Tesis pendiente':
			postitulo = 1
		else:
			postitulo = 0

	"""Calculo Total Formacion academica"""
	F_Ac = cant_titulo_docente + otro_titulo + postitulo


"""Sub-funcion para calcular Experiencia en dictado de capacitaciones en Experiencias Laborales """
def dictadoCapacitaciones(dt_entrada, i):
	experiencia_nivel_postulacion = dt_entrada.iloc[i]['¿Posee experiencia como capacitador/a?']


"""Funcion para calcular la categoria de puntajes Experiencias Laborales"""
def experienciaLaboral(dt_entrada, i):

	
	"""Experiencia en el nivel de Postulacion"""
	experiencia_nivel_postulacion = dt_entrada.iloc[i]['Experiencia en la docencia en el Nivel en el que se postula ']
	if experiencia_nivel_postulacion ==  'Hasta 5 años':
		experiencia_nivel_postulacion = 1
	if experiencia_nivel_postulacion == 'De 5 a 10 años':
		experiencia_nivel_postulacion = 3
	if experiencia_nivel_postulacion == 'Más de 10 años':
		experiencia_nivel_postulacion = 6
	if experiencia_nivel_postulacion == 'Ninguna experiencia':
		experiencia_nivel_postulacion = 0
	"""Experiencia en el sistema educativo"""
	experiencia_docente_sistema_educativo = dt_entrada.iloc[i]['Experiencia docente en el sistema educativo. (Inicial, Primaria, Secundaria, Superior No Universitaria, Superior Universitaria)']
	if experiencia_docente_sistema_educativo == 'Hasta 5 años':
		experiencia_docente_sistema_educativo = 0,5
	if experiencia_docente_sistema_educativo == 'De 5 a 10 años'
		experiencia_docente_sistema_educativo = 1
	if experiencia_docente_sistema_educativo == 'Más de 10 años'
		experiencia_docente_sistema_educativo = 2
	if experiencia_docente_sistema_educativo == 'Ninguna experiencia'
		experiencia_docente_sistema_educativo = 0






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