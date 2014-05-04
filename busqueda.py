#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
import MySQLdb
from fichaMenor import Ficha
import datetime

class ventanaBusqueda:
	
	def __init__(self):

		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaBusqueda = ruta + "Busqueda.glade"

		builder= gtk.Builder()
		builder.add_from_file(pantallaBusqueda)

		self.ventana = builder.get_object("Busqueda")
		self.tbBusqueda = builder.get_object("tbBusqueda")
		self.lsBusqueda = builder.get_object("lsBusqueda")

		self.btBuscar = builder.get_object("btBuscar")
		self.btVer = builder.get_object("btVer")

		self.tvBusqueda = builder.get_object("tvBusqueda")

		#obtenemos los radiobutton
		self.rbExpdte = builder.get_object("rbExpdte")
		self.rbNombre = builder.get_object("rbNombre")
		self.rbDNI = builder.get_object("rbDNI")

		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMensaje = builder.get_object("lbMensaje")
		self.btMsgboxAceptar = builder.get_object("btMsgBoxAceptar")


		dict = {"on_btBuscar_clicked": self.btBuscarClick, 
				"on_btVer_clicked": self.btVerClick,
				"on_btMsgBoxAceptar_clicked": self.btMsgBoxAceptarClick}
		builder.connect_signals(dict)

		

	def btBuscarClick(self, widget):
		self.lsBusqueda.clear()
	
		peticion = self.tbBusqueda.get_text()

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()

		if self.rbExpdte.get_active() == True:
			try:
				query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre, MENOR.DNI FROM EXPEDIENTE, MENOR WHERE EXPEDIENTE.IdExpdte LIKE \"%" + peticion + "%\" AND EXPEDIENTE.IdMenor = MENOR.IdMenor"
				cursor.execute(query)
			except Exception, e:
				raise e

		elif self.rbNombre.get_active() == True:
			try:
				query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre, MENOR.DNI FROM EXPEDIENTE, MENOR WHERE MENOR.Nombre LIKE \"%" + peticion + "%\" AND EXPEDIENTE.IdMenor = MENOR.IdMenor"
				cursor.execute(query)
			except Exception, e:
				raise e
		elif self.rbDNI.get_active() == True:
			try:
				query = "SELECT EXPEDIENTE.IdExpdte, MENOR.Nombre, MENOR.DNI FROM EXPEDIENTE, MENOR WHERE MENOR.DNI LIKE \"%" + peticion + "%\" AND EXPEDIENTE.IdMenor = MENOR.IdMenor"
				cursor.execute(query)
			except Exception, e:
				raise e

		encontrado = cursor.fetchall()
		
		if len(encontrado) != 0:
			for i in range(len(encontrado)):
				self.lsBusqueda.append(encontrado[i])
		else:
			self.msgbox.show()
			self.lbMensaje.set_text("No se encontraron resultados")
			return

		cursor.close()
		c.close()


	def btVerClick(self, widget):
		
		tv = self.tvBusqueda	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			expdte = model[treeiter][0]
			nombre = model[treeiter][1]
			dni = model[treeiter][2]

		try:
			c = MySQLdb.connect(*conexion.datos)
		except Exception, e:
			# self.msgbox.show()
			# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
			# self.btAceptarMsgBox.set_label("Aceptar")
			return
		cursor = c.cursor()
		
		if dni == "" or dni.isspace == True:
			try:
				query = "SELECT EXPEDIENTE.FechaApertura, EXPEDIENTE.EQM, MAX(ADMISION.FechaAdmision), MENOR.FechaNac, MENOR.Pasaporte, MENOR.Sexo, MENOR.Desamparo, MENOR.Direccion, MENOR.CP, MENOR.Localidad, MENOR.Provincia, MENOR.Telefono1, MENOR.Telefono2, MENOR.Mail, MENOR.Nacionalidad, MENOR.Empadronamiento, MENOR.NUSS, MENOR.NUSSA, MENOR.CIN FROM EXPEDIENTE, ADMISION, MENOR WHERE EXPEDIENTE.IdExpdte= \"" + expdte + "\" AND EXPEDIENTE.IdExpdte = ADMISION.IdExpdte AND EXPEDIENTE.IdMenor = MENOR.IdMenor"
				cursor.execute(query)
			except Exception, e:
				raise e
	
			resultadoConsulta = cursor.fetchone()
		
			fechaAper = resultadoConsulta[0]
			eqm = resultadoConsulta[1]
			fechaAdm = resultadoConsulta[2]
			fechaNac = resultadoConsulta[3]
			pasaporte = resultadoConsulta[4]
			sexo = resultadoConsulta[5]
			desamparo = resultadoConsulta[6]
			direccion = resultadoConsulta[7]
			cp = resultadoConsulta[8]
			localidad = resultadoConsulta[9]
			prov = resultadoConsulta[10]
			tlfno = resultadoConsulta[11]
			movil = resultadoConsulta[12]
			mail = resultadoConsulta[13]
			nacion = resultadoConsulta[14]
			padron = resultadoConsulta[15]
			nuss = resultadoConsulta[16]
			nussa = resultadoConsulta[17]
			cin = resultadoConsulta[18]

			#enviamos todo a la ficha
			Ficha().cargarDatos(fechaAdm, expdte, fechaAper, eqm, nombre, dni, pasaporte, fechaNac, direccion, cp, sexo, localidad, prov, tlfno, movil, mail, nacion, padron, nuss, nussa, cin, desamparo, "vacio")
		else:
			try:
				query = "SELECT EXPEDIENTE.FechaApertura, EXPEDIENTE.EQM, MAX(ADMISION.FechaAdmision), MENOR.FechaNac, MENOR.Pasaporte, MENOR.Sexo, MENOR.Desamparo, MENOR.Direccion, MENOR.CP, MENOR.Localidad, MENOR.Provincia, MENOR.Telefono1, MENOR.Telefono2, MENOR.Mail, MENOR.Nacionalidad, MENOR.Empadronamiento, MENOR.NUSS, MENOR.NUSSA, MENOR.CIN, DNI.TipoDoc FROM EXPEDIENTE, ADMISION, MENOR, DNI WHERE EXPEDIENTE.IdExpdte= \"" + expdte + "\" AND EXPEDIENTE.IdExpdte = ADMISION.IdExpdte AND EXPEDIENTE.IdMenor = MENOR.IdMenor AND MENOR.DNI = DNI.DNI"
				cursor.execute(query)
			except Exception, e:
				raise e

			resultadoConsulta = cursor.fetchone()
		
			fechaAper = resultadoConsulta[0]
			eqm = resultadoConsulta[1]
			fechaAdm = resultadoConsulta[2]
			fechaNac = resultadoConsulta[3]
			pasaporte = resultadoConsulta[4]
			sexo = resultadoConsulta[5]
			desamparo = resultadoConsulta[6]
			direccion = resultadoConsulta[7]
			cp = resultadoConsulta[8]
			localidad = resultadoConsulta[9]
			prov = resultadoConsulta[10]
			tlfno = resultadoConsulta[11]
			movil = resultadoConsulta[12]
			mail = resultadoConsulta[13]
			nacion = resultadoConsulta[14]
			padron = resultadoConsulta[15]
			nuss = resultadoConsulta[16]
			nussa = resultadoConsulta[17]
			cin = resultadoConsulta[18]
			tipodoc = resultadoConsulta[19]

			#enviamos todo a la ficha
			Ficha().cargarDatos(fechaAdm, expdte, fechaAper, eqm, nombre, dni, pasaporte, fechaNac, direccion, cp, sexo, localidad, prov, tlfno, movil, mail, nacion, padron, nuss, nussa, cin, desamparo, tipodoc)
		


		cursor.close()
		c.close()
		self.ventana.hide()

	
	def btMsgBoxAceptarClick(self, widget):
		self.msgbox.hide()

	# def cambiarbotones(self, x, y):
	# 	self.btVer.set_label(x)
	# 	self.btBuscar.set_label(y)