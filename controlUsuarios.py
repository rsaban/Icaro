#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
from Crypto.Cipher import ARC4


class users:
	
	def __init__(self):
		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaControlUsuarios = ruta + "ControlUsuarios.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaControlUsuarios)

		self.ventanaControlUsuarios = builder.get_object("controlUsuarios")

		self.cbxUsuariosRegistrados = builder.get_object("cbxUsuariosRegistrados")
		self.lsUsuariosRegistrados = builder.get_object("lsUsuariosRegistrados")
		self.cbxCentro = builder.get_object("cbxCentro")
		self.lsCentro = builder.get_object("lsCentro")
		self.tbNombre = builder.get_object("tbNombre")
		self.cbxCargo = builder.get_object("cbxCargo")
		self.lsCargo = builder.get_object("lsCargo")
		self.tbDNI = builder.get_object("tbDNI")
		self.tbUsuario = builder.get_object("tbUsuario")
		self.tbPass = builder.get_object("tbPass")
		self.tbNivel = builder.get_object("tbNivel")
		self.btAceptar = builder.get_object("btAceptar")

		#Obtenemos el Msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btAceptarMsgBox = builder.get_object("btAceptarMsgBox")
		
			
		dict = {"on_btAceptar_clicked": self.btAceptarClick,
				"on_cbxUsuariosRegistrados_changed": self.cbxUsuariosRegistradosTextChanged,
				"on_cbxCargo_changed": self.cbxCargoTextChanged,
				"on_btEliminar_clicked": self.btEliminarClick,
				"on_btAceptarMsgBox_clicked": self.btAceptarMsgBoxClick
				}
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
			self.lbMsgBox.set_text("No se han encontrado Centros de Trabajo. Por favor, dirijase al menú \"Herramientas/Nuevo Centro de Trabajo\" y registre un Centro antes de crear usuarios para Icaro. Gracias")
			self.btAceptarMsgBox.set_label("Cerrar")
		cursor.close()

	def cbxCargoTextChanged(self, widget):
		if self.cbxCargo.get_active() == 0:
			self.tbNivel.set_text("1")

	def btAceptarClick(self, widget):
		#operacion = self.btAceptar.get_label()

		centro = self.cbxCentro.get_active_text()
		nombre = self.tbNombre.get_text()
		cargo = self.cbxCargo.get_active_text()
		dni = self.tbDNI.get_text()
		usuario = self.tbUsuario.get_text()
		passw = self.tbPass.get_text()
		nivel = self.tbNivel.get_text()

		encriptar = ARC4.new('01234567')
		pass_encriptado = encriptar.encrypt(passw)

		queryConsultaCentro = "SELECT IdCentro FROM CENTRO WHERE NombreCentro = \"" + centro + "\""

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryConsultaCentro)
		except Exception, e:
			self.msgbox.show()
			self.lbMsgBox.set_text(str(e))
			self.btAceptarMsgBox.set_label("Cerrar")

		idcentro = cursor.fetchone()

		queryInsertarTecnico = "INSERT INTO TECNICOS (NombreTecnico, DNITecnico, ProfesionTecnico) VALUES (\"" + nombre + "\", \"" + dni + "\", \"" + cargo + "\")"

		if self.btAceptar.get_label() == "gtk-ok":
			
			try:
				cursor.execute(queryInsertarTecnico)
				c.commit()
			except Exception, e:
				c.rollback()

			queryConsultaTecnico = "SELECT IdTecnico FROM TECNICOS WHERE DNITecnico = \"" + dni + "\""

			try:
				cursor.execute(queryConsultaTecnico)
			except Exception, e:
				raise e
			
			idtecnico = cursor.fetchone()

			queryInsertarUsuGes = "INSERT INTO USUGES (IdTecnico, IdCentro, Usuario, KeyApp, Nivel) VALUES (\"" + str(idtecnico[0]) + "\", \"" + str(idcentro[0]) + "\", \"" + usuario + "\", \"" + pass_encriptado + "\", \"" + nivel + "\")"

			try:
				cursor.execute(queryInsertarUsuGes)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Usuario registrado con éxito.")
				self.btAceptarMsgBox.set_label("Cerrar")
			except Exception, e:
				c.rollback()

			cursor.close()
		
		
		elif self.btAceptar.get_label() == "Actualizar":
			pass

	def cbxUsuariosRegistradosTextChanged(self, widget):
		usuarioSeleccionado = cbxUsuariosRegistrados.get_active_text()
		pass

	def btEliminarClick(self, widget):
		pass

	def btAceptarMsgBoxClick(self, widget):
		if self.btAceptarMsgBox.get_label() == "Cerrar":
			self.msgbox.hide()
			self.ventanaControlUsuarios.hide()
		else:
			pass


		

