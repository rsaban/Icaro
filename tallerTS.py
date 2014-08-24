#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
import MySQLdb
import datetime


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
		self.tvAnadirPar = builder.get_object("tvAnadirPar")
		self.tvMenores = builder.get_object("tvMenores")
		#datosTaller
		self.tbNombreTaller = builder.get_object("tbNombreTaller")
		self.tbFechaInicio = builder.get_object("tbFechaInicio")
		self.tbFechaFin = builder.get_object("tbFechaFin")
		#tallerTS
		self.cbxTaller = builder.get_object("cbxTaller")
		self.cbxInicio = builder.get_object("cbxInicio")
		self.tbFin = builder.get_object("tbFin")

		#ponemos la seleccion múltiple de tvMenores
		selection = self.tvMenores.get_selection()
		selection.set_mode(gtk.SELECTION_MULTIPLE)

		#obtengo los liststore
		self.lsTaller = builder.get_object("lsTaller")
		self.lsFechaInicio = builder.get_object("lsFechaInicio")
		self.lstvAnadirPar = builder.get_object("lstvAnadirPar")
		self.lstvPartTaller = builder.get_object("lstvPartTaller")

		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btMsgboxAceptar = builder.get_object("btMsgboxAceptar")

		#cargo el cbxTaller con los talleres existentes si los hubiera.
		queryNombresTaller = "SELECT DISTINCT NombreTallerTS FROM TALLERES_TS"

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		try:
			cursor.execute(queryNombresTaller)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lsTaller.append(resultado[i])

		cursor.close()
		c.close()



		dict = {"on_btNuevoTaller_clicked": self.btNuevoTallerClick,
				"on_cbxTaller_changed": self.cbxTallerTextChanged,
				"on_cbxInicio_changed": self.cbxInicioTextChanged,
				"on_btMostrarAnadirPar_clicked": self.btMostrarAnadirParClick,
				"on_btAnadirPar_clicked": self.btAnadirParClick,
				"on_btEliminarPar_clicked": self.btEliminarParClick,
				"on_btAceptarTaller_clicked": self.btAceptarTallerClick,
				"on_participantes_delete_event": self.participantesDelete,
				"on_datosTaller_delete_event": self.datosTallerDelete,
				"on_btMsgboxAceptar_clicked": self.btMsgBoxAceptarClick
				}
		builder.connect_signals(dict)

	def btNuevoTallerClick(self, widget):
		self.datosTaller.show()

	def cbxTallerTextChanged(self, widget):
		queryFechasInicioTaller = "SELECT FechaInicio FROM TALLERES_TS WHERE NombreTallerTS = \'" + self.cbxTaller.get_active_text() + "'"

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		try:
			cursor.execute(queryFechasInicioTaller)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.acambiar = resultado[i]
				dateFormat = str(self.acambiar[0].strftime("%d/%m/%Y"))
				self.lsFechaInicio.append([dateFormat])

		cursor.close()
		c.close()

	def cbxInicioTextChanged(self, widget):
		fechaInicioText = self.cbxInicio.get_active_text()
		day = datetime.datetime.strptime(fechaInicioText, '%d/%m/%Y')
		fechaInicio = day.strftime('%Y-%m-%d')

		queryFechaFinTaller = "SELECT FechaFin FROM TALLERES_TS WHERE NombreTallerTS = \'" + self.cbxTaller.get_active_text() + "' AND FechaInicio = \'" + fechaInicio + "'"

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		try:
			cursor.execute(queryFechaFinTaller)
		except Exception, e:
			raise e

		resultado = cursor.fetchone()

		if resultado != 0:
			dateFormat = resultado[0].strftime("%d/%m/%Y")
			self.tbFin.set_text(dateFormat)

		cursor.close()
		c.close()


	def datosTallerDelete(self, widget, data=None):
		self.datosTaller.hide()
		return True

	def btMostrarAnadirParClick(self, widget):
		self.participantes.show()

		self.lstvAnadirPar.clear()

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		try:
			query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre, MENOR.IdMenor FROM EXPEDIENTE, MENOR WHERE EXPEDIENTE.IdMenor = MENOR.IdMenor"
			cursor.execute(query)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()


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
		c.close()

	def btAnadirParClick(self, widget):
		tv = self.tvAnadirPar	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			nombre = model[treeiter][1]
			idmenor = model[treeiter][2] 

			self.lstvPartTaller.append([nombre, idmenor])

			self.participantes.hide()

		else:
		 	self.msgbox.show()
		 	self.lbMsgBox.set_text("No hay nada seleccionado")
		 	self.btMsgboxAceptar.set_label("Cerrar")

	def btEliminarParClick(self, widget):
		tv = self.tvMenores	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			self.lstvPartTaller.remove(treeiter)
		else:
		 	self.msgbox.show()
		 	self.lbMsgBox.set_text("No hay nada seleccionado")
		 	self.btMsgboxAceptar.set_label("Cerrar")

	def participantesDelete(self, widget, data=None):
		self.participantes.hide()
		return True

	def btAceptarTallerClick(self, widget):
		nombreTaller = self.tbNombreTaller.get_text()
		
		fechaInicioText = self.tbFechaInicio.get_text()
		day = datetime.datetime.strptime(fechaInicioText, '%d/%m/%Y')
		fechaInicio= day.strftime('%Y-%m-%d')
		
		fechaFinText = self.tbFechaFin.get_text()
		day2 = datetime.datetime.strptime(fechaFinText, '%d/%m/%Y')
		fechaFin = day2.strftime('%Y-%m-%d')

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		queryInsertarTaller = "INSERT INTO TALLERES_TS (NombreTallerTS, FechaInicio, FechaFin) VALUES (\'" + nombreTaller + "', '" + fechaInicio + "', '" + fechaFin + "')"

		try:
			cursor.execute(queryInsertarTaller)
			c.commit()
		except Exception, e:
			c.rollback()

		queryConsultarTaller = "SELECT IdTallerTS FROM TALLERES_TS WHERE NombreTallerTS = \'" + nombreTaller + "' AND FechaInicio = \'" + fechaInicio + "' AND FechaFin = \'" + fechaFin + "'"

		try:
			cursor.execute(queryConsultarTaller)
		except Exception, e:
			raise e

		idtaller = cursor.fetchone()	
		idTaller = str(idtaller[0])

		self.tvMenores.get_selection().select_all()
		tree,iter = self.tvMenores.get_selection().get_selected_rows()

		for i in iter:
			idmenor = tree.get_value(tree.get_iter(i), 1)
			try:
		 		cursor.execute("INSERT INTO TALLERES_TS_PARTICIPANTES (IdTallerTS, IdMenor) VALUES (\'" + idTaller + "', '" + idmenor + "')")
		 		c.commit()
		 	except Exception, e:
		 		c.rollback()

		self.datosTaller.hide()

		# path = self.lstvPartTaller.get_path(self.lstvPartTaller.get_iter_first())
		# treeiter = self.lstvPartTaller.get_iter(path)

		# for i in len(self.lstvPartTaller): #'int' object is not iterable
		# 	try:
		#  		cursor.execute("INSERT INTO TALLERES_TS_PARTICIPANTES (IdTallerTS, IdMenor) VALUES (\'" + idTaller + "', '" + treeiter[1] + "')")
		#  	except Exception, e:
		#  		raise e
		
		# for i in len(self.lstvPartTaller):
		# 	tv = self.tvMenores	
		# 	selection = tv.get_selection()
		# 	model, treeiter = selection.get_selected()
		# 	if treeiter != None:

		# 	try:
		# 		cursor.execute("INSERT INTO TALLERES_TS_PARTICIPANTES (IdTallerTS, IdMenor) VALUES (\'" + i[o] + "', '" + i[1] + "')")
		# 	except Exception, e:
		# 		raise e


		c.close()



	def btMsgBoxAceptarClick(self, widget):
		if self.btMsgboxAceptar.get_label() == "Cerrar":
			self.msgbox.hide()
