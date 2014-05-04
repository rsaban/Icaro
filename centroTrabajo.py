#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
import MySQLdb


class working_center:
	
	def __init__(self):
		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaNuevoCentro = ruta + "CentroDeTrabajo.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaNuevoCentro)

		self.ventanaNuevoCentroTrabajo = builder.get_object("nuevoCentroTrabajo")

		self.tbNombre = builder.get_object("tbNombre")
		self.tbTitularidad = builder.get_object("tbTitularidad")
		self.tbCIF = builder.get_object("tbCIF")
		self.tbDireccion = builder.get_object("tbDireccion")
		self.tbCP = builder.get_object("tbCP")
		self.tbLocalidad = builder.get_object("tbLocalidad")
		self.tbProvincia = builder.get_object("tbProvincia")
		self.tbTlfno = builder.get_object("tbTlfno")
		self.tbMovil = builder.get_object("tbMovil")
		self.tbMail = builder.get_object("tbMail")		

		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btAceptarMsgBox = builder.get_object("btAceptarMsgBox")
			
		dict = {"on_btAceptar_clicked": self.btAceptarClick,
				"on_btAceptarMsgBox_clicked": self.btAceptarMsgBoxClick
				}
		builder.connect_signals(dict)



	def btAceptarClick(self, widget):
		nombre = self.tbNombre.get_text()
		titularidad = self.tbTitularidad.get_text()
		cif = self.tbCIF.get_text()
		direccion = self.tbDireccion.get_text()
		cp = self.tbCP.get_text()
		localidad = self.tbLocalidad.get_text()
		provincia = self.tbProvincia.get_text()
		tlfno = self.tbTlfno.get_text()
		movil = self.tbMovil.get_text()
		mail = self.tbMail.get_text()

		if "\"" in nombre or "\"" in titularidad or "\"" in cif or "\"" in direccion or "\"" in cp or "\"" in localidad or "\"" in provincia or "\"" in tlfno or "\"" in movil or "\"" in mail or  "\'" in nombre or "\'" in titularidad or "\'" in cif or "\'" in direccion or "\'" in cp or "\'" in localidad or "\'" in provincia or "\'" in tlfno or "\'" in movil or "\'" in mail:
			self.msgbox.show()
			self.lbMsgBox.set_text("Prohibido Comillas")
			self.btAceptarMsgBox.set_label("Perdón, lo había olvidado")
		else:

			queryNuevoCentro = "INSERT INTO CENTRO (NombreCentro, Titularidad, CIFCentro, DireccionCentro, CPCentro, LocalidadCentro, ProvinciaCentro, Telefono1Centro, Telefono2Centro, MailCentro) VALUES (\'" + nombre + "', '" + titularidad + "', '" + cif + "', '" + direccion + "', '" + cp + "', '" + localidad + "', '" + provincia + "', '" + tlfno + "', '" + movil + "', '" + mail + "\')"
		
			try:
				c = MySQLdb.connect(*conexion.datos)
			except Exception, e:
				# self.msgbox.show()
				# self.lbMsgBox.set_text("No se pudo solicitar el expediente. El servidor no está disponible. Intentelo más tarde.")
				# self.btAceptarMsgBox.set_label("Aceptar")
				return
			cursor = c.cursor()	

			try:
				cursor.execute(queryNuevoCentro)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Centro registrado con éxito.")
				self.btAceptarMsgBox.set_label("Aceptar")
			except Exception, e:
				raise e

			cursor.close()
			c.close()
		

	def btAceptarMsgBoxClick(self, widget):
		if self.btAceptarMsgBox.get_label() == "Perdón, lo había olvidado":
			self.msgbox.hide()
		else:
			self.msgbox.hide()
			self.ventanaNuevoCentroTrabajo.hide()



