#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
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


		#obtengo los liststore
		self.lstvAnadirPar = builder.get_object("lstvAnadirPar")
		self.lstvPartTaller = builder.get_object("lstvPartTaller")

		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btMsgboxAceptar = builder.get_object("btMsgboxAceptar")

		dict = {"on_btMostrarTaller_clicked": self.btMostrarTallerClick,
				"on_btMostrarAnadirPar_clicked": self.btMostrarAnadirParClick,
				"on_btAnadirPar_clicked": self.btAnadirParClick,
				"on_btEliminarPar_clicked": self.btEliminarParClick,
				"on_btAceptarTaller_clicked": self.btAceptarTallerClick,
				"on_participantes_delete_event": self.participantesDelete,
				"on_datosTaller_delete_event": self.datosTallerDelete,
				"on_btMsgboxAceptar_clicked": self.btMsgBoxAceptarClick
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
			query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre, MENOR.IdMenor FROM EXPEDIENTE, MENOR WHERE EXPEDIENTE.IdMenor = MENOR.IdMenor"
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

		c = conexion.db
		cursor = c.cursor()

		queryInsertarTaller = "INSERT INTO TALLERES_TS (NombreTallerTS, FechaInicio, FechaFin) VALUES (\'" + nombreTaller + "', '" + fechaInicio + "', '" + fechaFin + "')"

		try:
			cursor.execute(queryInsertarTaller)
			c.commit()
		except Exception, e:
			c.rollback()
		

		c.close()



	def btMsgBoxAceptarClick(self, widget):
		if self.btMsgboxAceptar.get_label() == "Cerrar":
			self.msgbox.hide()
