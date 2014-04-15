#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
from eleccion import ventanaEleccion
from herramientas import tools
from controles import controls
import conexion
from Crypto.Cipher import ARC4
import globales

class main:
	
	def __init__(self):
		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaPrincipal = ruta + "Main.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaPrincipal)

		self.ventanaPass = builder.get_object("Pass")
		self.tbUsuario = builder.get_object("tbUsuario")
		self.tbPass = builder.get_object("tbPass")
		self.lsCentro = builder.get_object("lsCentro")
		self.cbxCentro = builder.get_object("cbxCentro")


		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btAceptarMsgBox = builder.get_object("btAceptarMsgBox")


		dict = {"on_btExpedientes_clicked": self.btExpedientesClick,
				"on_btSalir_clicked":self.Salir,
				"on_btHerramientas_clicked": self.HerramientasClick,
				"on_btLegislacion_clicked": self.btLegislacionClick,
				"on_btControles_clicked": self.btControlesClick,
				"on_btAceptar_clicked": self.btAceptarPassClick,
				"on_btAceptarMsgBox_clicked": self.btAceptarMsgBoxClick,
				"on_btCancelar_clicked": self.Salir,
				"gtk_main_quit": self.Salir}
		builder.connect_signals(dict)


		c = conexion.db
		cursor = c.cursor()

		queryCentro = "SELECT NombreCentro FROM CENTRO"

		try:
			cursor.execute(queryCentro)
		except Exception, e:
			raise e

		listado = cursor.fetchall()

		if len(listado) != 0:
			for i in range(len(listado)):
				self.lsCentro.append(listado[i])
			self.cbxCentro.set_active(0)
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se han encontrado Centros de Trabajo. Por favor, inicie con la clave de Administrador proporcionada, dirijase al menú \"Herramientas/Nuevo Centro de Trabajo\" y registre un Centro antes de empezar a utilizar Icaro. Gracias")

		cursor.close()

	def btExpedientesClick(self, widget):
		ventanaEleccion()
		
	def HerramientasClick(self, widget):
		tools()

	def btLegislacionClick(self, widget):
		pass

	def btControlesClick(self, widget):
		controls()

	def btAceptarPassClick(self, widget):
		usuario = self.tbUsuario.get_text()
		passw = self.tbPass.get_text()
		centro = self.cbxCentro.get_active_text()

		encriptar = ARC4.new('01234567')
		pass_encriptado = encriptar.encrypt(passw)
			 
		c = conexion.db
		cursor = c.cursor()
				

		queryConsultaCentro = "SELECT IdCentro FROM CENTRO WHERE NombreCentro = \"" + centro + "\""
				
		try:
			cursor.execute(queryConsultaCentro)
		except Exception, e:
			self.msgbox.show()
			self.lbMsgBox.set_text(str(e))
			self.btAceptarMsgBox.set_label("Cerrar")
		
		idcentro = cursor.fetchone()

	
		try:
			query = "SELECT IdUsuges, IdTecnico, IdCentro, Nivel FROM USUGES WHERE Usuario = " + "'" + usuario + "' AND KeyApp = '" + pass_encriptado + "' AND IdCentro = '" + str(idcentro[0]) + "'"
			cursor.execute(query)
		except Exception, e:
			pass

		usuario_coincide = cursor.fetchone()

		if usuario_coincide != None:
			self.ventanaPass.hide()
			globales.idusuges = usuario_coincide[0]
			globales.idtecnico = usuario_coincide[1]
			globales.idcentro = usuario_coincide[2]
			globales.nivel = usuario_coincide[3]
			globales.nombreCentro = self.cbxCentro.get_active_text()
			#self.msgbox.show()
			#self.lbMsgBox.set_text(str(globales.idusuges) + " " + str(globales.idtecnico) + " " + str(globales.idcentro) + " " + str(globales.nivel))
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Usuario o contraseña incorrectos")

		cursor.close()
	
	def btAceptarMsgBoxClick(self, widget):
		self.msgbox.hide()
		self.tbUsuario.set_text("")
		self.tbPass.set_text("")

	def Salir(self, widget, data=None):
		gtk.main_quit()

	
if __name__=="__main__":
	
	main()
	gtk.main()



		