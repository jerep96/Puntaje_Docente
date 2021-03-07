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


	return F_Ac

"""Sub-funcion para calcular Experiencia en dictado de capacitaciones en Experiencias Laborales """
def dictadoCapacitaciones(dt_entrada, i):
	experiencia_capacitador = dt_entrada.iloc[i]['¿Posee experiencia como capacitador/a?']
	antiguedad = dt_entrada.iloc[i]['Indique la cantidad de años en total de toda su experiencia como capacitador/a']
	area_capacitacion = dt_entrada.iloc[i]['Indique el/las área/s en la que realizó la/s capacitacion/es']
	destinatario = dt_entrada.iloc[i]['Indique el/las área/s en la que realizó la/s capacitacion/es']
	if experiencia_capacitador == 'No':
		experiencia_capacitador = 0
		antiguedad = 0
		area_capacitacion = 0
		destinatario = 0
	else:
		if antiguedad == '10 o más años':
			antiguedad = 5
		elif antiguedad == '5 a 10 años':
			antiguedad = 4
		else:
			antiguedad = 3
		if area_capacitacion == 'Ciencias Exactas y Naturales' || area_capacitacion == 'Ciencias Sociales- Humanidades- Artística':
			area_capacitacion = 1
		elif area_capacitacion ==  'Pedagogía' || area_capacitacion == 'Informática-Tecnología':
			area_capacitacion = 2
		elif area_capacitacion == 'En Ninguna':
			area_capacitacion = 0
		else:
			area_capacitacion = 0.5
		if destinatario == 'Docentes' || destinatario == 'Equipos Técnicos del Ministerio de Educación':
			destinatario = 1
		elif destinatario == 'Ninguno':
			destinatario = 0
		else:
			destinatario = 0.5
	
	return

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
		experiencia_docente_sistema_educativo = 0.5
	if experiencia_docente_sistema_educativo == 'De 5 a 10 años'
		experiencia_docente_sistema_educativo = 1
	if experiencia_docente_sistema_educativo == 'Más de 10 años'
		experiencia_docente_sistema_educativo = 2
	if experiencia_docente_sistema_educativo == 'Ninguna experiencia'
		experiencia_docente_sistema_educativo = 0

	"""Experiencia en Capacitaciones"""
	experiencia_capacitador = dt_entrada.iloc[i]['¿Posee experiencia como capacitador/a?']
	if experiencia_capacitador == 'Sí' || experiencia_capacitador == 'Si':
		experiencia_capacitador = dictadoCapacitaciones()
	else:
		experiencia_capacitador = 0

	"""Experiencia en enseñanza mediadas por TIC"""
	experiencia_mediada_tic = dt_entrada.iloc[i]['¿Posee experiencia en propuestas enseñanza y aprendizaje mediadas por TIC (educación a distancia, educación virtual, educación remota, plataformas educativas, etc.)?']
	if experiencia_mediada_tic == 'Sí' || experiencia_mediada_tic == 'Si':
		puntaje_rol = dt_entrada.iloc[i]['¿En qué rol/les?']
		if puntaje_rol == 'Tutor' || puntaje_rol == 'Coordinador de tutores':
			puntaje_rol = 7
		elif puntaje_rol == 'Contenidista' || puntaje_rol == 'Didactizador' || puntaje_rol == 'Autor':
			puntaje_rol = 6
		elif puntaje_rol == 'Estudiante':
			puntaje_rol = 2
		else:
			puntaje_rol = 0
	else:
		puntaje_rol = 0

	"""Experiencia en administracion de aulas virtuales"""
	experiencia_aulas_virtuales = dt_entrada.iloc[i]['¿Posee experiencia en la administración de aulas virtuales?']
	if experiencia_aulas_virtuales == 'Sí' || experiencia_aulas_virtuales == 'Si':
		puntaje_experiencia_aulas_virtuales = 3
	else:
		puntaje_experiencia_aulas_virtuales = 0

	"""Utilizacion y frecuencia del aula virtual"""
	envio_recepcion_correos = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Envió/recepción de correos]']
	if envio_recepcion_correos == 'Todos los días' || envio_recepcion_correos == 'Casi todos los días':
		envio_recepcion_correos = 0.5
	else:
		envio_recepcion_correos = 0
	comunicacion_chat = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Comunicación por chats]']
	if comunicacion_chat == 'Todos los días' || comunicacion_chat == 'Casi todos los días':
		comunicacion_chat = 0.5
	else:
		comunicacion_chat = 0
	acordar_colegas = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Acordar criterios con colegas]']
	if acordar_colegas == 'Todos los días' || acordar_colegas == 'Casi todos los días':
		acordar_colegas = 1
	else:
		acordar_colegas = 0
	acordar_alumnos = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Acordar criterios con estudiantes]']
	if acordar_alumnos == 'Todos los días' || acordar_alumnos == 'Casi todos los días':
		acordar_alumnos = 1
	else:
		acordar_alumnos = 0
	evaluacion_retro = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Evaluación y retroalimentación]']
	if evaluacion_retro == 'Todos los días' || evaluacion_retro == 'Casi todos los días':
		evaluacion_retro = 1
	else:
		evaluacion_retro = 0
	rubricas = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Uso de rúbricas]']
	if rubricas == 'Todos los días' || rubricas == 'Casi todos los días':
		rubricas = 1
	else:
		rubricas = 0
	dar_clases = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Dar clases]']
	if dar_clases == 'Todos los días' || dar_clases == 'Casi todos los días':
		dar_clases = 1
	else:
		dar_clases = 0
	contenidos_digitales = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Elaborar/compartir contenidos digitales]']
	if contenidos_digitales == 'Todos los días' || contenidos_digitales == 'Casi todos los días':
		contenidos_digitales = 1
	else:
		contenidos_digitales = 0
	alojar = dt_entrada.iloc[i]['¿Con qué frecuencia realiza las siguientes acciones en aulas virtuales? [Alojar archivos/documentos educativos]']
	if alojar == 'Todos los días' || alojar == 'Casi todos los días':
		alojar = 1
	else:
		alojar = 0

	puntos_utilizacion_freceuncia = envio_recepcion_correos + comunicacion_chat + acordar_colegas + acordar_alumnos + evaluacion_retro + rubricas + dar_clases + contenidos_digitales + alojar
	if puntos_utilizacion_freceuncia >= 5:
		puntos_utilizacion_freceuncia = 5
	else:
		puntos_utilizacion_freceuncia = puntos_utilizacion_freceuncia



"""Funcion para el calculo de puntaje segun comptencias digitales"""
def competencias(dt_entrada, i):

"""Competencias digitales"""
"""Procesasdor de texto"""
procesador_texto = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Elabora propuestas de enseñanza usando procesador de texto (Word, Openoffice, Google Docs)]']
if procesador_texto == 'Experto':
	procesador_texto = 1
elif procesador_texto == 'Avanzado':
	procesador_texto = 1*0.8
elif procesador_texto == 'Básico':
	procesador_texto = 1*0.5
else:
	procesador_texto = 0

"""Planilla de Calculo"""
planilla_calculo = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Utiliza planillas de cálculo (Excel, hojas de cálculo de código abierto) en su práctica docente]']
if planilla_calculo == 'Experto':
	planilla_calculo = 2
elif planilla_calculo == 'Avanzado':
	planilla_calculo = 2*0.8
elif planilla_calculo == 'Básico':
	planilla_calculo = 2*0.5
else:
	planilla_calculo = 0

"""Presentaciones Interactivas"""
presentaciones = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Elabora presentaciones interactivas (Power Point / Prezzi, Genially, otras de código abierto)]']
if presentaciones == 'Experto':
	presentaciones = 2
elif presentaciones == 'Avanzado':
	presentaciones = 2*0.8
elif presentaciones == 'Básico':
	presentaciones = 2*0.5
else:
	presentaciones = 0

"""Diseña evaluaciones"""
diseña_evaluaciones = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Diseña evaluaciones apoyadas en TIC que permitan evidenciar la construcción del conocimiento]']
if diseña_evaluaciones == 'Experto':
	diseña_evaluaciones = 5
elif diseña_evaluaciones == 'Avanzado':
	diseña_evaluaciones = 5*0.8
elif diseña_evaluaciones == 'Básico':
	diseña_evaluaciones = 5*0.5
else:
	diseña_evaluaciones = 0

"""Graba Clases"""
graba_clases = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Graba clases teóricas en audios o videos]']
if graba_clases == 'Experto':
	graba_clases = 3
elif graba_clases == 'Avanzado':
	graba_clases = 3*0.8
elif graba_clases == 'Básico':
	graba_clases = 3*0.5
else:
	graba_clases = 0

"""Edicion multimedia"""
edit_multi = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Crea, edita y transfiere archivos (fotos, música, videos, imágenes) entre computadoras y otros dispositivos (pendrive, tablet, celular)]']
if edit_multi == 'Experto':
	edit_multi = 2
elif edit_multi == 'Avanzado':
	edit_multi = 2*0.8
elif edit_multi == 'Básico':
	edit_multi = 2*0.5
else:
	edit_multi = 0

"""Busqueda repositorios educativos"""
busqueda_repo = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Realiza la búsqueda, evaluación y selección de repositorios educativos y revistas electrónicas.]']
if busqueda_repo == 'Experto':
	busqueda_repo = 2
elif busqueda_repo == 'Avanzado':
	busqueda_repo = 2*0.8
elif busqueda_repo == 'Básico':
	busqueda_repo = 2*0.5
else:
	busqueda_repo = 0

"""Protocolos de comunicacion"""
protocolo_comunicacion = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Utiliza protocolos sociales para comunicar y transmitir información en un ambiente digital según destinatarios (colegas / estudiantes)]']
if protocolo_comunicacion == 'Experto':
	protocolo_comunicacion = 4
elif protocolo_comunicacion == 'Avanzado':
	protocolo_comunicacion = 4*0.8
elif protocolo_comunicacion == 'Básico':
	protocolo_comunicacion = 4*0.5
else:
	protocolo_comunicacion = 0

"""Participacion en comunidades de aprendizaje"""
participacion = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Participa en comunidades de aprendizaje]']
if participacion == 'Experto':
	participacion = 4
elif participacion == 'Avanzado':
	participacion = 4*0.8
elif participacion == 'Básico':
	participacion = 4*0.5
else:
	participacion = 0

"""Realiza capacitaciones"""
realiza_capacitaciones = dt_entrada.iloc[i]['¿Cuál de las siguientes acciones puede realizar en la computadora, en el celular, en internet-on line? (Seleccionar la opción que corresponda a su respuesta indicando su nivel de apropiación de las TIC) [Realiza capacitaciones/formaciones on line]']
if realiza_capacitaciones == 'Experto':
	realiza_capacitaciones = 4
elif realiza_capacitaciones == 'Avanzado':
	realiza_capacitaciones = 5*0.8
elif realiza_capacitaciones == 'Básico':
	realiza_capacitaciones = 5*0.5
else:
	realiza_capacitaciones = 0

"""Puntaje Total"""
puntaje_total_competencias = procesador_texto + planilla_calculo + presentaciones + diseña_evaluaciones + graba_clases + edit_multi + busqueda_repo + protocolo_comunicacion + participacion + realiza_capacitaciones
if puntaje_total_competencias >= 15:
	puntaje_total_competencias = 15
else:
	puntaje_total_competencias = puntaje_total_competencias


"""Funcion para el calculo de puntaje segun Capacidades Profesionales"""
def capacidadesProfecionales(dt_entrada, i):
	




	


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