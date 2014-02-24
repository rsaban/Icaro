#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
import datetime
import globales
from ts import ficha_ts

class Ficha:
	
	
	def __init__(self):

		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaFichaMenor = ruta + "FichaMenor.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaFichaMenor)

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
		self.lsEquipo = builder.get_object("lsEquipo")
		self.lsPadron = builder.get_object("lsPadron")
		self.lsSexo = builder.get_object("lsSexo")
		self.lsTipoDoc = builder.get_object("lsTipoDoc")
		self.lbCerrado = builder.get_object("lbCerrado")
		self.btReabrir = builder.get_object("btReabrir")
		self.btMostrarDNI = builder.get_object("btMostrarDNI")
		self.btMostrarPasaporte = builder.get_object("btMostrarPasaporte")
		self.btActualizar = builder.get_object("btActualizar")
		self.btAlta = builder.get_object("btAlta")
		self.btRegCont = builder.get_object("btRegCont")
		self.btDireccion = builder.get_object("btDireccion")
		self.btTS = builder.get_object("btTS")
		self.btPS = builder.get_object("btPS")
		self.btEd = builder.get_object("btEd")


		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btMsgboxAceptar = builder.get_object("btMsgboxAceptar")

		#Obtenemos la ventana DNI y Pasaporte
		self.ventanaDNI = builder.get_object("ventanaDNI")
		self.cbxDNITipoDoc = builder.get_object("cbxDNITipoDoc")
		self.tbDNIDNI = builder.get_object("tbDNIDNI")
		self.tbFechaExpdDNI = builder.get_object("tbFechaExpdDNI")
		self.tbFechaRenoDNI = builder.get_object("tbFechaRenoDNI")
		self.ventanaPasaporte = builder.get_object("ventanaPasaporte")
		self.tbPasPasaporte = builder.get_object("tbPasPasaporte")
		self.tbPasFechaExp = builder.get_object("tbPasFechaExp")
		self.tbPasFechaRenov = builder.get_object("tbPasFechaRenov")

		#Obtenemos la ventana Regimen de Contactos
		self.regimenContactos = builder.get_object("regimenContactos")
		self.lstvRegContactos = builder.get_object("lstvRegContactos")

		#Obtenemos la ventana alta
		self.ventanaAlta = builder.get_object("alta")
		self.tbFechaAlta = builder.get_object("tbFechaAlta")
		self.cbxMotivo = builder.get_object("cbxMotivo")
		self.lsAlta = builder.get_object("lsAlta")

		#Ponemos el nombre a la ventana, el centro activo y el idCentro en un label Invisible.
		self.FichaMenor.set_title("Ficha")
		self.lbNombreCentro.set_text(globales.nombreCentro)
		self.lbIdCentro.set_text(str(globales.idcentro))


		dict = {"on_btActualizar_clicked": self.btActualizarClick,
				"on_btAlta_clicked": self.btAltaClick,
				"on_btDireccion_clicked": self.btDireccionClick,
				"on_btTS_clicked": self.btTSClick,
				"on_btPS_clicked": self.btPSClick,
				"on_btEd_clicked": self.btEdClick,
				"on_btRegCont_clicked": self.btRegContClick,
				"on_btMostrarDNI_clicked": self.btMostrarDNIClick,
				"on_btMostrarPasaporte_clicked": self.btMostrarPasaporteClick,
				"on_ventanaDNI_delete_event": self.BorrarVentanaDNI,
				"on_ventanaPasaporte_delete_event": self.BorrarVentanaPasaporte,
				"on_btDNIAceptar_clicked": self.btDNIAceptarClick,
				"on_btPasAceptar_clicked": self.btPasAceptarClick,
				"on_btMsgboxAceptar_clicked": self.btMsgboxAceptarClick,
				"on_regimenContactos_delete_event": self.regimenContactosDelete,
				"on_btCerrarContactos_clicked": self.regimenContactosDelete,
				"on_alta_delete_event": self.altaDelete,
				"on_btAceptarAlta_clicked": self.btAceptarAltaClick,
				"on_btReabrir_clicked": self.btReabrirClick
				}
		builder.connect_signals(dict)

	def cargarDatos(self, *argv):
		dateFormat = argv[0].strftime("%d/%m/%Y") # fecha con formato
		self.tbFechaAdmision.set_text(dateFormat)
		self.tbExpdte.set_text(argv[1])
		dateFormat2 = argv[2].strftime("%d/%m/%Y")
		self.tbFechaApertura.set_text(dateFormat2)
		self.tbNombre.set_text(argv[4])
		self.tbDNI.set_text(argv[5])
		self.tbPasaporte.set_text(argv[6])
		self.tbDireccion.set_text(argv[8])
		self.tbCP.set_text(str(argv[9]))
		self.tbLocalidad.set_text(argv[11])
		self.tbProvincia.set_text(argv[12])
		dateFormat3 = argv[7].strftime("%d/%m/%Y")
		self.tbFechaNac.set_text(dateFormat3)
		self.tbTlfno.set_text(str(argv[13]))
		self.tbMovil.set_text(str(argv[14]))
		self.tbMail.set_text(argv[15])
		self.tbNacionalidad.set_text(argv[16])
		self.tbNUSS.set_text(str(argv[18]))
		self.tbNUSSA.set_text(str(argv[19]))
		self.tbCIN.set_text(str(argv[20]))

		for posicion, elemento in enumerate(self.lsEquipo):
			f = elemento[0]
			if f == str(argv[3]):
				self.cbxEquipo.set_active(posicion)

		for posicion, elemento in enumerate(self.lsSexo):
			f = elemento[0]
			if f == str(argv[10]):
				self.cbxSexo.set_active(posicion)

		for posicion, elemento in enumerate(self.lsPadron):
			f = elemento[0]
			if f == str(argv[17]):
				self.cbxPadron.set_active(posicion)

		for posicion, elemento in enumerate(self.lsPadron):
			f = elemento[0]
			if f == str(argv[21]):
				self.cbxDesamparo.set_active(posicion)

		if str(argv[22]) == "vacio":
			pass
		else:
			for posicion, elemento in enumerate(self.lsTipoDoc):
				f = elemento[0]
				if f == str(argv[22]):
					self.cbxTipoDoc.set_active(posicion)

		#Consultamos si está en activo en el centro
		queryActivo = "SELECT MAX(ADMISION.FechaAdmision), MAX(ALTA.FechaAlta) FROM ADMISION, ALTA WHERE ADMISION.IdExpdte = \'" + self.tbExpdte.get_text() + "\' AND ALTA.IdExpdte = \'" + self.tbExpdte.get_text() + "\'"

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryActivo)
		except Exception, e:
			raise e

		resultadoActivo = cursor.fetchone()

		if len(resultadoActivo) > 0:
			if resultadoActivo[0] < resultadoActivo[1]:
				self.lbCerrado.show()
				self.btReabrir.show()
				self.tbExpdte.set_sensitive(False)
				self.tbFechaAdmision.set_sensitive(False)	
				self.tbFechaApertura.set_sensitive(False)
				self.tbNombre.set_sensitive(False)
				self.tbDNI.set_sensitive(False)
				self.tbPasaporte.set_sensitive(False)
				self.tbDireccion.set_sensitive(False)
				self.tbCP.set_sensitive(False)
				self.tbLocalidad.set_sensitive(False)
				self.tbProvincia.set_sensitive(False)			
				self.tbFechaNac.set_sensitive(False)
				self.tbTlfno.set_sensitive(False)
				self.tbMovil.set_sensitive(False)
				self.tbMail.set_sensitive(False)
				self.tbNacionalidad.set_sensitive(False)
				self.tbNUSS.set_sensitive(False)
				self.tbNUSSA.set_sensitive(False)
				self.tbCIN.set_sensitive(False)
				self.cbxEquipo.set_sensitive(False)
				self.cbxTipoDoc.set_sensitive(False)
				self.cbxSexo.set_sensitive(False)
				self.cbxPadron.set_sensitive(False)
				self.cbxDesamparo.set_sensitive(False)
				self.btMostrarDNI.set_sensitive(False)
				self.btMostrarPasaporte.set_sensitive(False)
				self.btActualizar.set_sensitive(False)
				self.btAlta.set_sensitive(False)
				self.btRegCont.set_sensitive(False)
				self.btDireccion.set_sensitive(False)
				self.btTS.set_sensitive(False)
				self.btPS.set_sensitive(False)
				self.btEd.set_sensitive(False)

		cursor.close()

	def btActualizarClick(self, widget):
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

		day2 = datetime.datetime.strptime(fechaAperturaText, '%d/%m/%Y')
		fechaApertura = day2.strftime('%Y-%m-%d')

		day3 = datetime.datetime.strptime(fechaNacText, '%d/%m/%Y')
		fechaNac = day3.strftime('%Y-%m-%d')

		queryConsultarIdMenor = "SELECT MENOR.IdMenor FROM MENOR, EXPEDIENTE WHERE EXPEDIENTE.IdExpdte = \"" + expdte + "\" AND EXPEDIENTE.IdMenor = MENOR.IdMenor"
		queryActualizarDNI = "UPDATE DNI SET TipoDoc = \'" + tipoDoc + "\' WHERE DNI.DNI = \'" + dni + "\'"
		
		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryConsultarIdMenor)
		except Exception, e:
			raise e

		idmenor = cursor.fetchone()
		
		queryActualizarFicha = "UPDATE MENOR SET Nombre = \'" + nombre + "\', FechaNac = \'" + fechaNac + "\', DNI = \'" + dni + "\', Pasaporte = \'" + pasaporte + "\', Sexo = \'" + sexo + "\', Desamparo = \'" + desamparo + "\', Direccion = \'" + direccion + "\', CP = \'" + cp + "\', Localidad = \'" + localidad + "\', Provincia = \'" + provincia + "\', Telefono1 = \'" + tlfno + "\', Telefono2 = \'" + movil + "\', Mail = \'" + mail + "\', Nacionalidad = \'" + nacionalidad + "\', Empadronamiento = \'" + padron + "\', NUSS = \'" + nuss + "\', NUSSA = \'" + nussa + "\', CIN = \'" + cin + "\' WHERE MENOR.IdMenor = \'" + str(idmenor[0]) + "\'"

		try:
			cursor.execute(queryActualizarFicha)
			c.commit()
		except Exception, e:
			c.rollback()

		if dni == "" or dni.isspace == True:
			pass
		else:
			try:
				cursor.execute(queryActualizarDNI)
				c.commit()
			except Exception, e:
				c.rollback()

		# DNI.DNI Y PASAPORTE.Pasaporte se acutalizan en cascada en la base de datos siempre que exista un registro en esas Tablas. Si no, hay que insertarlo
		queryConsultarDNI = "SELECT DNI.DNI FROM DNI WHERE DNI.DNI = \'" + dni + "\'"
		try:
			cursor.execute(queryConsultarDNI)
		except Exception, e:
			raise e
		busquedaDni = cursor.fetchone()

		if busquedaDni != None:
			pass
		else:
			queryInsertarDNI = "INSERT INTO DNI (DNI, TipoDoc) VALUES (\'" + dni + "', '" + tipoDoc + "')"
			try:
				cursor.execute(queryInsertarDNI)
				c.commit()
			except Exception, e:
				c.rollback()

		queryConsultarPasaporte = "SELECT PASAPORTE.Pasaporte FROM PASAPORTE WHERE PASAPORTE.Pasaporte = \'" + pasaporte + "\'"
		try:
			cursor.execute(queryConsultarPasaporte)
		except Exception, e:
			raise e
		busquedaPas = cursor.fetchone()

		if busquedaPas != None:
			pass
		else:
			queryInsertarPasaporte = "INSERT INTO PASAPORTE (Pasaporte) VALUES (\'" + pasaporte + "')"
			try:
				cursor.execute(queryInsertarPasaporte)
				c.commit()
			except Exception, e:
				c.rollback()		

		queryActualizarExpdte = "UPDATE EXPEDIENTE SET FechaApertura = \'" + fechaApertura + "\', EQM = \'" + equipo + "\' WHERE EXPEDIENTE.IdExpdte = \'" + expdte + "\' AND EXPEDIENTE.IdMenor = \'" + str(idmenor[0]) + "\'"

		try:
			cursor.execute(queryActualizarExpdte)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Expediente actualizado con éxito en Icaro.")
			self.btMsgboxAceptar.set_label("Aceptar")
		except Exception, e:
			c.rollback()

		if self.btActualizar.get_label() == "Reabrir":
			fechaReadmisionText = self.tbFechaAdmision.get_text()
			dayR = datetime.datetime.strptime(fechaReadmisionText, '%d/%m/%Y')
			fechaReadmision = dayR.strftime('%Y-%m-%d')
			
			queryUltimaAlta = "SELECT MAX(ALTA.FechaAlta) FROM ALTA WHERE ALTA.IdExpdte = \'" + expdte + "'"
			try:
				cursor.execute(queryUltimaAlta)
			except Exception, e:
				raise e

			ultimaAlta = cursor.fetchone()

			fechaUA = ultimaAlta[0]
			
			if str(fechaUA) > fechaReadmision:
				self.msgbox.show()
				self.lbMsgBox.set_text("La fecha de readmision no puede ser inferior a la última fecha de alta del centro (" + str(fechaUA) + ")")
				self.btMsgboxAceptar.set_label("Ups!, no me di cuenta")
			else:
				queryReAdmision = "INSERT INTO ADMISION (IdExpdte, FechaAdmision) VALUES (\'" + expdte + "', '" + fechaReadmision + "')"
				try:
					cursor.execute(queryReAdmision)
					c.commit()
				except Exception, e:
					c.rollback()


		cursor.close()

	def btAltaClick(self, widget):
		self.ventanaAlta.show()

	def btAceptarAltaClick(self, widget):
		fechaAltaText = self.tbFechaAlta.get_text()
		day = datetime.datetime.strptime(fechaAltaText, '%d/%m/%Y')
		fechaAlta = day.strftime('%Y-%m-%d')

		fechaAdmisionText = self.tbFechaAdmision.get_text()
		day2 = datetime.datetime.strptime(fechaAdmisionText, '%d/%m/%Y')
		fechaAdmision = day2.strftime('%Y-%m-%d')

		motivo = self.cbxMotivo.get_active_text()

		#primero, comprobar que la fecha de alta es mayor que la última fecha de admisión.
		if fechaAdmision >= fechaAlta:
			self.msgbox.show()
			self.lbMsgBox.set_text("La fecha de alta no puede ser inferior a la fecha de admisión.")
			self.btMsgboxAceptar.set_label("Ups!, no me di cuenta")

		else:

			queryAlta = "INSERT INTO ALTA (IdExpdte, FechaAlta, MotivoAlta) VALUES (\'" + self.tbExpdte.get_text() + "\', '" + fechaAlta + "\', '" + motivo + "\')"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryAlta)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Alta registrada con éxito")
				self.btMsgboxAceptar.set_label("Cerrar")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("No se pudo completar la operación")
				self.btMsgboxAceptar.set_label("Cerrar")			

			cursor.close()

	def altaDelete(self, widget, data=None):
		self.ventanaAlta.hide()
		return True

	def btDireccionClick(self, widget):
		pass

	def btTSClick(self, widget):
		ficha_ts().cargarDatos(self.lbNombreCentro.get_text(), self.tbExpdte.get_text(), self.tbNombre.get_text(), self.tbDNI.get_text())
		self.FichaMenor.hide()

	def btPSClick(self, widget):
		pass

	def btEdClick(self, widget):
		pass

	def btRegContClick(self, widget):
		self.regimenContactos.show()
		self.lstvRegContactos.clear()

		queryRegContactos = "SELECT UC.NombreConviv, UC.Parentesco, UC.Privilegio FROM UC, EXPEDIENTE, AREA_SOCIAL WHERE EXPEDIENTE.IdExpdte = \'" + self.tbExpdte.get_text() + "\' AND EXPEDIENTE.IdExpdte = AREA_SOCIAL.IdExpdte AND AREA_SOCIAL.IdSocial = UC.IdSocial"

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryRegContactos)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lstvRegContactos.append(resultado[i])

		cursor.close()


	def regimenContactosDelete(self, widget, data=None):
		self.regimenContactos.hide()
		return True

	def btMostrarDNIClick(self, widget):
		if self.tbDNI.get_text() == "" or self.tbDNI.get_text().isspace == True:
			self.msgbox.show()
			self.lbMsgBox.set_text("Actualice el DNI y Tipo de Documento para acceder a los detalles")
			self.btMsgboxAceptar.set_label("Volver")
		else:
			self.ventanaDNI.show()
			self.tbDNIDNI.set_text(self.tbDNI.get_text()) 
			self.cbxDNITipoDoc.set_active(self.cbxTipoDoc.get_active())

			
			queryDetallesDNI = "SELECT DNI.FechaExp, DNI.FechaRenov FROM DNI WHERE DNI.DNI = \'" + self.tbDNI.get_text() + "\'"
			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryDetallesDNI)
			except Exception, e:
				raise e

			resultado = cursor.fetchone()

			if len(resultado) != 0:
				if resultado[0] == None:
					pass
				else:
					dateFormat6 = resultado[0].strftime("%d/%m/%Y")
					self.tbFechaExpdDNI.set_text(dateFormat6)
					dateFormat7 = resultado[1].strftime("%d/%m/%Y")
					self.tbFechaRenoDNI.set_text(dateFormat7)
			else:
				pass

			cursor.close()

	def btMostrarPasaporteClick(self, widget):
		if self.tbPasaporte.get_text() == "" or self.tbPasaporte.get_text().isspace == True:
			self.msgbox.show()
			self.lbMsgBox.set_text("Actualice el Pasaporte para acceder a los detalles")
			self.btMsgboxAceptar.set_label("Volver")
		else:
			self.ventanaPasaporte.show()
			self.tbPasPasaporte.set_text(self.tbPasaporte.get_text())

			queryDetallesPasaporte = "SELECT PASAPORTE.FechaExpP, PASAPORTE.FechaRenovP FROM PASAPORTE WHERE PASAPORTE.Pasaporte = \'" + self.tbPasaporte.get_text() + "\'"
			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryDetallesPasaporte)
			except Exception, e:
				raise e

			resultado = cursor.fetchone()

			if len(resultado) != 0:
				if resultado[0] == None:
					pass
				else:
					dateFormat4 = resultado[0].strftime("%d/%m/%Y")
					self.tbPasFechaExp.set_text(dateFormat4)
					dateFormat5 = resultado[1].strftime("%d/%m/%Y")
					self.tbPasFechaRenov.set_text(dateFormat5)
			else:
				self.tbPasFechaExp.set_text("vacio")
				self.tbPasFechaRenov.set_text("vacio")

			cursor.close()

	def BorrarVentanaDNI(self, widget, data=None):
		self.ventanaDNI.hide()
		return True

	def BorrarVentanaPasaporte(self, widget, data=None):
		self.ventanaPasaporte.hide()
		return True

	def btDNIAceptarClick(self, widget):
		if self.tbFechaExpdDNI.get_text() == "" or self.tbFechaExpdDNI.get_text().isspace == True or self.tbFechaRenoDNI.get_text() == "" or self.tbFechaRenoDNI.get_text().isspace == True:
			self.msgbox.show()
			self.lbMsgBox.set_text("Por favor, introduzca las fechas de Expedición y Renovación antes de continuar.")
			self.btMsgboxAceptar.set_label("Volver")
			self.msgbox.set_modal(True)
		else:
			day = datetime.datetime.strptime(self.tbFechaExpdDNI.get_text(), '%d/%m/%Y')
			fechaExpedicion = day.strftime('%Y-%m-%d')
		
			day = datetime.datetime.strptime(self.tbFechaRenoDNI.get_text(), '%d/%m/%Y')
			fechaRenovacion = day.strftime('%Y-%m-%d')
			
			queryActualizarFechasDNI = "UPDATE DNI SET FechaExp = \'" + fechaExpedicion + "\', FechaRenov = \'" + fechaRenovacion + "\' WHERE DNI.DNI = \'" + self.tbDNIDNI.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryActualizarFechasDNI)
				c.commit()
				self.ventanaDNI.hide()
			except Exception, e:
				c.rollback()

			cursor.close()
	
	def btPasAceptarClick(self, widget):
		if self.tbPasFechaExp.get_text() == "" or self.tbPasFechaExp.get_text().isspace == True or self.tbPasFechaRenov.get_text() == "" or self.tbPasFechaRenov.get_text().isspace == True:
			self.msgbox.show()
			self.lbMsgBox.set_text("Por favor, introduzca las fechas de Expedición y Renovación antes de continuar.")
			self.btMsgboxAceptar.set_label("Volver")
			self.msgbox.set_modal(True)
		else:
			day = datetime.datetime.strptime(self.tbPasFechaExp.get_text(), '%d/%m/%Y')
			fechaExpedicion = day.strftime('%Y-%m-%d')
		
			day = datetime.datetime.strptime(self.tbPasFechaRenov.get_text(), '%d/%m/%Y')
			fechaRenovacion = day.strftime('%Y-%m-%d')
			
			queryActualizarFechasPasporte = "UPDATE PASAPORTE SET FechaExpP = \'" + fechaExpedicion + "\', FechaRenovP = \'" + fechaRenovacion + "\' WHERE DNI.DNI = \'" + self.tbDNIDNI.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryActualizarFechasPasporte)
				c.commit()
				self.ventanaPasaporte.hide()
			except Exception, e:
				c.rollback()

			cursor.close()

	def btReabrirClick(self, widget):
		self.lbCerrado.hide()
		self.btReabrir.hide()
		self.tbExpdte.set_sensitive(True)
		self.tbFechaAdmision.set_sensitive(True)
		self.tbFechaAdmision.set_editable(True)
		self.tbFechaApertura.set_sensitive(True)
		self.tbNombre.set_sensitive(True)
		self.tbDNI.set_sensitive(True)
		self.tbPasaporte.set_sensitive(True)
		self.tbDireccion.set_sensitive(True)
		self.tbCP.set_sensitive(True)
		self.tbLocalidad.set_sensitive(True)
		self.tbProvincia.set_sensitive(True)			
		self.tbFechaNac.set_sensitive(True)
		self.tbTlfno.set_sensitive(True)
		self.tbMovil.set_sensitive(True)
		self.tbMail.set_sensitive(True)
		self.tbNacionalidad.set_sensitive(True)
		self.tbNUSS.set_sensitive(True)
		self.tbNUSSA.set_sensitive(True)
		self.tbCIN.set_sensitive(True)
		self.cbxEquipo.set_sensitive(True)
		self.cbxTipoDoc.set_sensitive(True)
		self.cbxSexo.set_sensitive(True)
		self.cbxPadron.set_sensitive(True)
		self.cbxDesamparo.set_sensitive(True)
		self.btMostrarDNI.set_sensitive(True)
		self.btMostrarPasaporte.set_sensitive(True)
		self.btActualizar.set_sensitive(True)
		self.btActualizar.set_label("Reabrir")
	
	def btMsgboxAceptarClick (self, widget):
		if self.btMsgboxAceptar.get_label() == "Aceptar":
			self.msgbox.hide()
			self.FichaMenor.hide()
		elif self.btMsgboxAceptar.get_label() == "Cerrar":
			self.msgbox.hide()
			self.ventanaAlta.hide()
			self.FichaMenor.hide()
		else:
			self.msgbox.hide()





