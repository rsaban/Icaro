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
		self.nombreSesion = builder.get_object("nombreSesion")

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
		self.tbTallerActivo = builder.get_object("tbTallerActivo")
		#nombreSesion
		self.tbNombreSesion = builder.get_object("tbNombreSesion")
		#objetos del notebook
		self.tbObjetivos = builder.get_object("tbObjetivos")
		self.tbMaterial = builder.get_object("tbMaterial")
		self.tbActividades = builder.get_object("tbActividades")
		self.tbDuracion = builder.get_object("tbDuracion")
		self.tvParticipante = builder.get_object("tvParticipante")
		self.tbEvaluacion = builder.get_object("tbEvaluacion")
		self.tvSesiones = builder.get_object("tvSesiones")

		#ponemos la seleccion múltiple de tvMenores
		selection = self.tvMenores.get_selection()
		selection.set_mode(gtk.SELECTION_MULTIPLE)

		#obtengo los liststore
		self.lsTaller = builder.get_object("lsTaller")
		self.lsFechaInicio = builder.get_object("lsFechaInicio")
		self.lstvAnadirPar = builder.get_object("lstvAnadirPar")
		self.lstvPartTaller = builder.get_object("lstvPartTaller")
		self.lsParticipantes = builder.get_object("lsParticipantes")
		self.lsSesiones = builder.get_object("lsSesiones")
		self.lstvAsistentes = builder.get_object("lstvAsistentes")

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
				"on_btVerTaller_clicked": self.btVerTallerClick,
				"on_btNuevaSesion_clicked": self.btNuevaSesionClick,
				"on_btAceptarNombreSesion_clicked": self.btAceptarNombreSesionClick,
				"on_tvSesiones_row_activated": self.tvSesionesDobleClick,
				"on_nombreSesion_delete_event": self.nombreSesionDelete,
				"on_cellToogleAsistencia_toggled": self.controlAsistentes,
				"on_btGuardarSesion_clicked": self.btGuardarSesionClick,
				"on_participantes_delete_event": self.participantesDelete,
				"on_datosTaller_delete_event": self.datosTallerDelete,
				"on_btMsgboxAceptar_clicked": self.btMsgBoxAceptarClick
				}
		builder.connect_signals(dict)

	def btNuevoTallerClick(self, widget):
		self.datosTaller.show()

	def cbxTallerTextChanged(self, widget):
		self.lsFechaInicio.clear()
		self.tbFin.set_text("")
		self.lsParticipantes.clear()
		self.lsSesiones.clear()
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

	def btVerTallerClick(self, widget):
		self.lsParticipantes.clear()
		self.lsSesiones.clear()
		fechaInicioText = self.cbxInicio.get_active_text()
		day = datetime.datetime.strptime(fechaInicioText, '%d/%m/%Y')
		fechaInicio = day.strftime('%Y-%m-%d')
		fechaFinText = self.tbFin.get_text()
		day2 = datetime.datetime.strptime(fechaFinText, '%d/%m/%Y')
		fechaFin = day2.strftime('%Y-%m-%d')

		queryIdTaller = "SELECT IdTallerTS FROM TALLERES_TS WHERE NombreTallerTS = \'" + self.cbxTaller.get_active_text() + "' AND FechaInicio = \'" + fechaInicio + "' AND FechaFin = \'" + fechaFin + "'"

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		try:
			cursor.execute(queryIdTaller)
		except Exception, e:
			raise e

		resultadoIdTaller = cursor.fetchone()

		if resultadoIdTaller != 0:
			localizadoIdTaller = str(resultadoIdTaller[0])

		self.tbTallerActivo.set_text(localizadoIdTaller)

		#cargamos los participantes
		queryParticipantes = "SELECT MENOR.Nombre, MENOR.IdMenor FROM MENOR, TALLERES_TS_PARTICIPANTES, TALLERES_TS WHERE MENOR.IdMenor = TALLERES_TS_PARTICIPANTES.IdMenor AND TALLERES_TS_PARTICIPANTES.IdTallerTS = TALLERES_TS.IdTallerTS AND TALLERES_TS.IdTallerTS = \'" + localizadoIdTaller + "'"

		try:
			cursor.execute(queryParticipantes)
		except Exception, e:
			raise e

		resultadoParticipantes = cursor.fetchall()
		
		#limpio el liststore Asistentes
		self.lstvAsistentes.clear()
		
		if len(resultadoParticipantes) != 0:
			for i in range(len(resultadoParticipantes)):
				self.lsParticipantes.append([resultadoParticipantes[i][0]])
				#los cargo también en la pestaña "Asistentes"
				self.lstvAsistentes.append([resultadoParticipantes[i][0], False, resultadoParticipantes[i][1]])


		#cargamos las sesiones
		querySesiones = "SELECT NombreSesion, IdSesion FROM TALLERES_TS_SESION WHERE IdTallerTS = \'" + str(resultadoIdTaller[0]) + "'"

		try:
			cursor.execute(querySesiones)
		except Exception, e:
			raise e

		resultadoSesiones = cursor.fetchall()

		if len(resultadoSesiones) != 0:
			for i in range(len(resultadoSesiones)):
				self.lsSesiones.append(resultadoSesiones[i])


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

	def btNuevaSesionClick(self, widget):
		self.nombreSesion.show()

	def btAceptarNombreSesionClick(self, widget):
		nombre = self.tbNombreSesion.get_text()
		fechaInicioText = self.cbxInicio.get_active_text()
		day = datetime.datetime.strptime(fechaInicioText, '%d/%m/%Y')
		fechaInicio = day.strftime('%Y-%m-%d')
		fechaFinText = self.tbFin.get_text()
		day2 = datetime.datetime.strptime(fechaFinText, '%d/%m/%Y')
		fechaFin = day2.strftime('%Y-%m-%d')

		queryIdTaller = "SELECT IdTallerTS FROM TALLERES_TS WHERE NombreTallerTS = \'" + self.cbxTaller.get_active_text() + "' AND FechaInicio = \'" + fechaInicio + "' AND FechaFin = \'" + fechaFin + "'"

		try:
		 	c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		try:
			cursor.execute(queryIdTaller)
		except Exception, e:
			raise e

		resultadoIdTaller = cursor.fetchone()
		resultadoIdTaller = str(resultadoIdTaller[0])

		queryNuevaSesion = "INSERT INTO TALLERES_TS_SESION (NombreSesion, IdTallerTS) VALUES (\'" + nombre + "', '" + resultadoIdTaller + "')"

		try:
			cursor.execute(queryNuevaSesion)
			c.commit()
		except Exception, e:
			c.rollback()

		cursor.close()
		c.close()

		self.nombreSesionDelete(self)
		
	def tvSesionesDobleClick(self, treeview, path, column):
		# Aquí hacemos dobleclick a las sesiones. Funciona guay.
		# self.msgbox.show()
		# self.lbMsgBox.set_text("Doble click listo")
		# self.btMsgboxAceptar.set_label("Cerrar")
		
		pass

	def controlAsistentes(self, widget, path):
		self.lstvAsistentes[path][1] = not self.lstvAsistentes[path][1]

	def btGuardarSesionClick(self, widget):
		#obtenemos la sesion
		tv = self.tvSesiones	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			sesion = model[treeiter][1]
		else: 
			self.msgbox.show()
			self.lbMsgBox.set_text("Seleccione la sesión a guardar")
			self.btMsgboxAceptar.set_label("Cerrar")
			return
		#obtenemos el taller
		taller = self.tbTallerActivo.get_text()
		#obtenemos los demás objetos del notebook.
		obj = self.tbObjetivos.get_buffer()
		objetivos = obj.get_text(*obj.get_bounds())
		mat = self.tbMaterial.get_buffer()
		material = mat.get_text(*mat.get_bounds())
		act = self.tbActividades.get_buffer()
		actividades = act.get_text(*act.get_bounds())
		duracion = self.tbDuracion.get_text()
		eva = self.tbEvaluacion.get_buffer()
		evaluacion = eva.get_text(*eva.get_bounds())

		queryGuardarSesion = "UPDATE TALLERES_TS_SESION SET Objetivos = \'" + objetivos + "\', Material = \'" + material + "\', Actividades = \'" + actividades + "\', Duracion = \'" + duracion + "\', Evaluacion = \'" + evaluacion + "\' WHERE IdSesion = \'" + sesion + "\' AND IdTallerTS = \'" + taller + "\'"

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			self.btMsgboxAceptar.set_label("Cerrar")
			return
		cursor = c.cursor()

		try:
			cursor.execute(queryGuardarSesion)
			c.commit()
			# self.msgbox.show()
			# self.lbMsgBox.set_text("Guardado con éxito")
			# self.btMsgboxAceptar.set_label("Cerrar")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("¿Que pasó? No se guardó!!")
			self.btMsgboxAceptar.set_label("Cerrar")

		cursor.close()
		c.close()


		#Ahora reocojo y grabo los asistentes
		selection = self.tvParticipante.get_selection()
		selection.set_mode(gtk.SELECTION_MULTIPLE)

		listaAsisten = []
		listaNoAsisten = []
		self.tvParticipante.get_selection().select_all()
		tree,iter = self.tvParticipante.get_selection().get_selected_rows()
		for i in iter:
			checado = tree.get_value(tree.get_iter(i), 1)
			if checado == True:
				listaAsisten.append(tree.get_value(tree.get_iter(i), 2))
			else:
				listaNoAsisten.append(tree.get_value(tree.get_iter(i), 2))

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			self.btMsgboxAceptar.set_label("Cerrar")
			return
		cursor = c.cursor()

		for i in range(len(listaAsisten)):
			asiste = listaAsisten[i]

			queryAsistencia = "INSERT INTO TALLERES_TS_ASISTENTES VALUES (\'" + taller + "\', '" + sesion + "\', '" + asiste + "\')"

			try:
				cursor.execute(queryAsistencia)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Guardado con éxito")
				self.btMsgboxAceptar.set_label("Cerrar")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("¿Que pasó? No se guardó!!")
				self.btMsgboxAceptar.set_label("Cerrar")




		cursor.close()
		c.close()

	def nombreSesionDelete(self, widget, data=None):
		self.nombreSesion.hide()
		return True

	def btMsgBoxAceptarClick(self, widget):
		if self.btMsgboxAceptar.get_label() == "Cerrar":
			self.msgbox.hide()
