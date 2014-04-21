#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion


class taller_ts:
	
	def __init__(self):

		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaTallerTS = ruta + "tallerTS.glade"

		builder= gtk.Builder()
		builder.add_from_file(pantallaTallerTS)

		#obtengo las ventanas
		self.datosTaller = builder.get_object("datosTaller")
		self.participantes = builder.get_object("participantes")

		#obtengo los objetos

		#obtengo los liststore
		self.lstvAnadirPar = builder.get_object("lstvAnadirPar")

		dict = {"on_btMostrarTaller_clicked": self.btMostrarTallerClick,
				"on_btMostrarAnadirPar_clicked": self.btMostrarAnadirParClick,
				"on_participantes_delete_event": self.participantesDelete,
				"on_datosTaller_delete_event": self.datosTallerDelete
				}
		builder.connect_signals(dict)

	def btMostrarTallerClick(self, widget):
		self.datosTaller.show()
		
	def datosTallerDelete(self, widget, data=None):
		self.datosTaller.hide()
		return True

	def btMostrarAnadirParClick(self, widget):
		self.participantes.show()

		self.lstvAnadirPar.clear()

		c = conexion.db
		cursor = c.cursor()

		try:
			#query = "SELECT DISTINCT EXPEDIENTE.IdExpdte, MENOR.Nombre FROM EXPEDIENTE, MENOR, ADMISION A1, ALTA AL1 WHERE EXPEDIENTE.IdMenor = MENOR.IdMenor AND A1.IdExpdte =  EXPEDIENTE.IdExpdte  AND AL1.IdExpdte = EXPEDIENTE.IdExpdte AND (SELECT MAX(FechaAdmision) FROM ADMISION A2 WHERE A1.IdExpdte = A2.IdExpdte) < (SELECT MAX(FechaAlta) FROM ALTA AL2 WHERE AL1.IdExpdte = AL2.IdExpdte)"
			#SELECT DISTINCT EXPEDIENTE.IdExpdte, MENOR.Nombre FROM EXPEDIENTE, MENOR, ADMISION A1, ALTA AL1 WHERE EXPEDIENTE.IdMenor = MENOR.IdMenor AND A1.IdExpdte =  EXPEDIENTE.IdExpdte  AND AL1.IdExpdte = EXPEDIENTE.IdExpdte AND (SELECT MAX(FechaAdmision) FROM ADMISION A2 WHERE A1.IdExpdte = A2.IdExpdte) < (SELECT CASE WHEN FechaAlta IS NULL THEN 0 ELSE MAX(FechaAlta) END FROM ALTA AL2 WHERE AL1.IdExpdte = AL2.IdExpdte)
			query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre FROM EXPEDIENTE, MENOR WHERE EXPEDIENTE.IdMenor = MENOR.IdMenor"
			cursor.execute(query)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		#no funciona todavia!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
		#ahora para cada resultado debo consultar si está activo, si lo está, añadirlo al lstvAnadirPar
		# for i in range(len(resultado)):
		# 	if i[2] < i[3]:
		# 		self.lstvAnadirPar.append(i[0][1])

		if len(resultado) != 0:
			for i in range(len(resultado)):
				#Consultamos si está en activo en el centro
				numero_expediente = str(resultado[i][0])
				queryActivo = "SELECT MAX(ADMISION.FechaAdmision), MAX(ALTA.FechaAlta) FROM ADMISION, ALTA WHERE ADMISION.IdExpdte = \'" + numero_expediente + "\' AND ALTA.IdExpdte = \'" + numero_expediente + "\'"
				try:
					cursor.execute(queryActivo)
				except Exception, e:
					raise e

				resultadoActivo = cursor.fetchone()

				if len(resultadoActivo) > 0:
					if resultadoActivo[0] >= resultadoActivo[1]:
						self.lstvAnadirPar.append(resultado[i])
					
			


		cursor.close()

	def participantesDelete(self, widget, data=None):
		self.participantes.hide()
		return True


