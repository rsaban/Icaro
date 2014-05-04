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
import globales

class nuevoExp:
	
	
	def __init__(self):

		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaNuevoExpdte = ruta + "NuevaFichaMenor.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaNuevoExpdte)

		self.FichaMenor = builder.get_object("FichaMenor")

		#Esto para el titulo del centro activo y para la variable idCentro, que tengo que guardarla en la tabla Menor.
		self.lbNombreCentro = builder.get_object("lbNombreCentro")
		self.lbIdCentro = builder.get_object("lbIdCentro")
		
		self.tbExpdte = builder.get_object("tbExpdte")
		self.tbFechaApertura = builder.get_object("tbFechaApertura")
		self.cbxEquipo = builder.get_object("cbxEquipo")
		self.tbNombre = builder.get_object("tbNombre")
		self.cbxTipoDoc = builder.get_object("cbxTipoDoc")
		self.tbDNI = builder.get_object("tbDNI")
		self.tbPasaporte = builder.get_object("tbPasaporte")
		self.tbDireccion = builder.get_object("tbDireccion")
		self.cbxSexo = builder.get_object("cbxSexo")
		self.tbCP = builder.get_object("tbCP")
		self.tbLocalidad = builder.get_object("tbLocalidad")
		self.tbProvincia = builder.get_object("tbProvincia")
		self.tbFechaNac = builder.get_object("tbFechaNac")
		self.tbTlfno = builder.get_object("tbTlfno")
		self.tbMovil = builder.get_object("tbMovil")
		self.tbMail = builder.get_object("tbMail")
		self.tbNacionalidad = builder.get_object("tbNacionalidad")
		self.tbNUSS = builder.get_object("tbNUSS")
		self.tbNUSSA = builder.get_object("tbNUSSA")
		self.tbCIN = builder.get_object("tbCIN")
		self.cbxPadron = builder.get_object("cbxPadron")
		self.cbxDesamparo = builder.get_object("cbxDesamparo")
		self.tbFechaAdmision = builder.get_object("tbFechaAdmision")


		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btMsgboxAceptar = builder.get_object("btMsgboxAceptar")

		#Ponemos el nombre a la ventana, el centro activo y el idCentro en un label Invisible.
		self.FichaMenor.set_title("Nueva Ficha")
		self.lbNombreCentro.set_text(globales.nombreCentro)
		self.lbIdCentro.set_text(str(globales.idcentro))


		dict = {"on_btAceptar_clicked": self.btAceptarClick,
				"on_btCancelar_clicked": self.btCancelarClick,
				"on_btMsgboxAceptar_clicked": self.btMsgboxAceptarClick
				}
		builder.connect_signals(dict)


	def btAceptarClick(self, widget):
		if self.tbExpdte.get_text() == "" or self.tbExpdte.get_text().isspace() == True or self.tbFechaAdmision.get_text() == "" or self.tbFechaAdmision.get_text().isspace() == True:
			self.msgbox.show()
			self.lbMsgBox.set_text("El número de expediente y la fecha de admisión son campos obligatorios.")
			self.btMsgboxAceptar.set_label("Upss!! Que cabeza la mía!!")
		else:	

			expdte = self.tbExpdte.get_text()
			fechaAperturaText = self.tbFechaApertura.get_text()
			equipo = str(self.cbxEquipo.get_active_text())
			nombre = self.tbNombre.get_text()
			tipoDoc = str(self.cbxTipoDoc.get_active_text())
			dni = self.tbDNI.get_text()
			pasaporte = self.tbPasaporte.get_text()
			direccion = self.tbDireccion.get_text()
			sexo = str(self.cbxSexo.get_active_text())
			cp = self.tbCP.get_text()
			localidad = self.tbLocalidad.get_text()
			provincia = self.tbProvincia.get_text()
			fechaNacText = self.tbFechaNac.get_text()
			tlfno = self.tbTlfno.get_text()
			movil = self.tbMovil.get_text()
			mail = self.tbMail.get_text()
			nacionalidad = self.tbNacionalidad.get_text()
			nuss = self.tbNUSS.get_text()
			nussa = self.tbNUSSA.get_text()
			cin = self.tbCIN.get_text()
			padron = str(self.cbxPadron.get_active_text())
			desamparo = str(self.cbxDesamparo.get_active_text())
			centroActivo = self.lbIdCentro.get_text()
			fechaAdmisionText = self.tbFechaAdmision.get_text()

			day = datetime.datetime.strptime(fechaAdmisionText, '%d/%m/%Y')
			fechaAdmision = day.strftime('%Y-%m-%d')

			day2 = datetime.datetime.strptime(fechaAperturaText, '%d/%m/%Y')
			fechaApertura = day2.strftime('%Y-%m-%d')

			day3 = datetime.datetime.strptime(fechaNacText, '%d/%m/%Y')
			fechaNac = day3.strftime('%Y-%m-%d')


			queryInsertarMenor = "INSERT INTO MENOR (Nombre, FechaNac, DNI, Pasaporte, Sexo, Desamparo, Direccion, CP, Localidad, Provincia, Telefono1, Telefono2, Mail, Nacionalidad, Empadronamiento, NUSS, NUSSA, CIN, IdCentro) VALUES (\'" + nombre + "', '" + fechaNac + "', '" + dni + "', '" + pasaporte + "', '" + sexo + "', '" + desamparo + "', '" + direccion + "', '" + cp + "', '" + localidad + "', '" + provincia + "', '" + tlfno + "', '" + movil + "', '" + mail + "', '" + nacionalidad + "', '" + padron + "', '" + nuss + "', '" + nussa + "', '" + cin + "', '" + centroActivo + "')"
			queryConsultarIdMenor = "SELECT IdMenor FROM MENOR WHERE DNI = \"" + dni + "\""
			queryInsertarDNI = "INSERT INTO DNI (DNI, TipoDoc) VALUES (\'" + dni + "', '" + tipoDoc + "')"
			queryInsertarPasaporte = "INSERT INTO PASAPORTE (Pasaporte) VALUES (\'" + pasaporte + "')"
			queryGrabarAdmision = "INSERT INTO ADMISION (IdExpdte, FechaAdmision) VALUES (\'" + expdte + "', '" + fechaAdmision + "')"


			try:
				c = MySQLdb.connect(*conexion.datos)
			except Exception, e:
				# self.msgbox.show()
				# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
				# self.btAceptarMsgBox.set_label("Aceptar")
				return
			cursor = c.cursor()

			try:
				cursor.execute(queryInsertarMenor)
				c.commit()
			except Exception, e:
				c.rollback()

			if dni == "" or dni.isspace == True:
				pass
			else:
				try:
					cursor.execute(queryInsertarDNI)
					c.commit()
				except Exception, e:
					c.rollback()

			if pasaporte == "" or pasaporte.isspace == True:
				pass
			else:
				try:
					cursor.execute(queryInsertarPasaporte)
					c.commit()
				except Exception, e:
					c.rollback()

			try:
				cursor.execute(queryConsultarIdMenor)
			except Exception, e:
				raise e

			idmenor = cursor.fetchone()

			queryInsertarExpdte = "INSERT INTO EXPEDIENTE (IdExpdte, FechaApertura, EQM, IdMenor) VALUES (\'" + expdte + "', '" + fechaApertura + "', '" + equipo + "', '" + str(idmenor[0]) + "')"

			try:
				cursor.execute(queryInsertarExpdte)
				c.commit()
			except Exception, e:
				c.rollback()

			try:
				cursor.execute(queryGrabarAdmision)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Expediente registrado con éxito en Icaro.")
				self.btMsgboxAceptar.set_label("Aceptar")
			except Exception, e:
				c.rollback()

			cursor.close()
			c.close()
		
	def btCancelarClick(self, widget):
		self.FichaMenor.hide()

	def btMsgboxAceptarClick (self, widget):
		if self.btMsgboxAceptar.get_label() == "Aceptar":
			self.msgbox.hide()
			self.FichaMenor.hide()
		else:
			self.msgbox.hide()





