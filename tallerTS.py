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
			query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre FROM EXPEDIENTE, MENOR WHERE EXPEDIENTE.IdMenor = MENOR.IdMenor"
			cursor.execute(query)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		#ahora para cada resultado debo consultar si está activo, si lo está, añadirlo al lstvAnadirPar




		cursor.close()

	def participantesDelete(self, widget, data=None):
		self.participantes.hide()
		return True


