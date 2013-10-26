#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
import datetime


class ficha_ts:
	
	def __init__(self):
		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaTS = ruta + "TS.glade"

		builder= gtk.Builder()
		builder.add_from_file(pantallaTS)
		
		#fondos del notebook
		self.acambiar1 = builder.get_object("layout2")
		self.acambiar2 = builder.get_object("layout3")
		self.acambiar3 = builder.get_object("layout4")
		self.acambiar4 = builder.get_object("layout5")
		self.acambiar5 = builder.get_object("layout6")
		self.acambiar8 = builder.get_object("layout8")
		self.acambiar9 = builder.get_object("layout9")
		self.acambiar24 = builder.get_object("layout24")

		#ficha
		#ENCABEZADO
		self.lbCentroActivo = builder.get_object("lbCentroActivo")
		self.lbMostrarExpdte = builder.get_object("lbMostrarExpdte")
		self.lbMostrarNombre = builder.get_object("lbMostrarNombre")
		self.lbMostrarDNI = builder.get_object("lbMostrarDNI")
		#NOTEBOOK
		self.notebook1 = builder.get_object("notebook1")
		#Antecedentes
		self.tbAntecedentes = builder.get_object("tbAntecedentes")
		self.cbxPHC = builder.get_object("cbxPHC")
		self.cbxMedidaInternamiento = builder.get_object("cbxMedidaInternamiento")
		#Convivencia
		self.tvUC = builder.get_object("tvUC")
		self.cbxTipoVivienda = builder.get_object("cbxTipoVivienda")
		self.tbCaracViv = builder.get_object("tbCaracViv")
		#Situacion Familiar
		self.tbEconomiaFamiliar = builder.get_object("tbEconomiaFamiliar")
		self.tbSanidadFamiliar = builder.get_object("tbSanidadFamiliar")
		#Regimen de contactos
		self.tvContactosFamiliares = builder.get_object("tvContactosFamiliares")
		self.tvContactosProfesionales = builder.get_object("tvContactosProfesionales")
		#Formacion y Empleo
		self.cbxFormReglada = builder.get_object("cbxFormReglada")
		self.tbFormCompl = builder.get_object("tbFormCompl")
		self.cbxSitLaboral = builder.get_object("cbxSitLaboral")
		self.tbExperiencia = builder.get_object("tbExperiencia")
		#Entorno y Comunidad
		self.cbxSitJud = builder.get_object("cbxSitJud")
		self.tbDetalleLegal = builder.get_object("tbDetalleLegal")
		self.tbEntorno = builder.get_object("tbEntorno")
		#Diagnostico Social
		self.tbDiagnostico = builder.get_object("tbDiagnostico")
		#SAE
		self.tbOficina = builder.get_object("tbOficina")
		self.tbDireccionOficina = builder.get_object("tbDireccionOficina")
		self.tbTelefonoOficina = builder.get_object("tbTelefonoOficina")
		self.tbInscripcion = builder.get_object("tbInscripcion")
		self.tbRenovacion = builder.get_object("tbRenovacion")
		self.tbCadAdmva = builder.get_object("tbCadAdmva")
		self.tvRegistroCitas = builder.get_object("tvRegistroCitas")
		#Andalucia Orienta
		self.tbOficinaOrienta = builder.get_object("tbOficinaOrienta")
		self.tbDireccionOrienta = builder.get_object("tbDireccionOrienta")
		self.tbTelefonoOrienta = builder.get_object("tbTelefonoOrienta")
		self.tbOrientador = builder.get_object("tbOrientador")
		self.tbFechaInicioOrienta = builder.get_object("tbFechaInicioOrienta")
		self.tvCitasOrienta = builder.get_object("tvCitasOrienta")
		#Andalucia Acoge
		self.tvConsultasAAcoge = builder.get_object("tvConsultasAAcoge")
		#Labora
		self.tbOrientadorLabora = builder.get_object("tbOrientadorLabora")
		self.tbTelefonoLabora = builder.get_object("tbTelefonoLabora")
		self.tvCursosLabora = builder.get_object("tvCursosLabora")
		self.tvPracticasLabora = builder.get_object("tvPracticasLabora")
		self.cbxPracticasLabora = builder.get_object("cbxPracticasLabora")
		#Cruz Roja
		self.tvConsultasCRoja = builder.get_object("tvConsultasCRoja")
		#Extranjeria
		self.cbxPermisoExtranj = builder.get_object("cbxPermisoExtranj")
		self.tbFechaExpedicionPermiso = builder.get_object("tbFechaExpedicionPermiso")
		self.tbFechaRenovacionPermiso = builder.get_object("tbFechaRenovacionPermiso")
		self.cbxPermisoTrabajo = builder.get_object("cbxPermisoTrabajo")
		self.cbxPermisoExcepTrabajo = builder.get_object("cbxPermisoExcepTrabajo")
		self.tvEmpleos = builder.get_object("tvEmpleos")
		#SGIT
		self.tvConsultasSGIT = builder.get_object("tvConsultasSGIT")
		#Extutelados
		self.tvPropuestas = builder.get_object("tvPropuestas")
		self.tvReuniones = builder.get_object("tvReuniones")

		#unidadConvivencia
		self.ventanaUC = builder.get_object("unidadConvivencia")
		self.tbFamiliarReg = builder.get_object("tbFamiliarReg")
		self.tbNacFamiliar = builder.get_object("tbNacFamiliar")
		self.cbxParentesco = builder.get_object("cbxParentesco")
		self.cbxConv = builder.get_object("cbxConv")
		self.tbDireccionFamiliar = builder.get_object("tbDireccionFamiliar")
		self.tbTelefonoFamiliar = builder.get_object("tbTelefonoFamiliar")
		self.tbMailFamiliar = builder.get_object("tbMailFamiliar")
		self.cbxSitLabFamiliar = builder.get_object("cbxSitLabFamiliar")
		self.cbxPrivilegio = builder.get_object("cbxPrivilegio")
		self.btAceptarFamiliar = builder.get_object("btAceptarFamiliar")
		self.fixed1 = builder.get_object("fixed1")
		self.btEliminarFam = builder.get_object("btEliminarFam")
	
		#contactosFamiliares
		self.ventanaContacFam = builder.get_object("contactosFamiliares")
		self.cbxTipo = builder.get_object("cbxTipo")
		self.tbContacto = builder.get_object("tbContacto")
		self.tbLugar = builder.get_object("tbLugar")
		self.tbFechaConFam = builder.get_object("tbFechaConFam")
		self.tbHoraContacFam = builder.get_object("tbHoraContacFam")
		self.tbObservFam = builder.get_object("tbObservFam")
		self.fixed2 = builder.get_object("fixed2")
		self.btAceptarContacFam = builder.get_object("btAceptarContacFam")
		self.btBorrarContactoFam = builder.get_object("btBorrarContactoFam")

		#selecFam	
		self.ventanaSelecFam = builder.get_object("selecFam")
		self.cbxFamReg = builder.get_object("cbxFamReg")
		self.btAceptarSelecFam = builder.get_object("btAceptarSelecFam")

		#selecTecnico	
		self.ventanaSelecTecnico = builder.get_object("selecTecnico")
		self.cbxTecReg = builder.get_object("cbxTecReg")
		self.btAceptarSelecTecnico = builder.get_object("btAceptarSelecTecnico")
	
		#contactosTS
		self.ventanaContactosTS = builder.get_object("contactosTS")
		self.tbFamiliar = builder.get_object("tbFamiliar")
		self.tbFechaContTS = builder.get_object("tbFechaContTS")
		self.tbHora = builder.get_object("tbHora")
		self.tbDetalles = builder.get_object("tbDetalles")
		self.btAceptarCTS = builder.get_object("btAceptarCTS")
		self.btEliminarConTS = builder.get_object("btEliminarConTS")
		self.fixed3 = builder.get_object("fixed3")

		#proxCitaSAE
		self.ventanaProxCitaSAE = builder.get_object("proxCitaSAE")
		self.tbFechaCitaSAE = builder.get_object("tbFechaCitaSAE")
		self.tbDetallesCitaSAE = builder.get_object("tbDetallesCitaSAE")
		self.btAceptarCitaSAE = builder.get_object("btAceptarCitaSAE")
		self.btEliminarCita = builder.get_object("btEliminarCita")
		self.fixed4 = builder.get_object("fixed4")	

		#proxCitaOrienta
		self.ventanaProxCitaOrienta = builder.get_object("proxCitaOrienta")
		self.tbFechaCitaOrienta = builder.get_object("tbFechaCitaOrienta")
		self.tbDetallesCitaOrienta = builder.get_object("tbDetallesCitaOrienta")
		self.btAceptarCitaOrienta = builder.get_object("btAceptarCitaOrienta")
		self.btEliminarCitaOrienta = builder.get_object("btEliminarCitaOrienta")
		self.fixed5 = builder.get_object("fixed5")			
	
		#consultaAAcoge	
		self.ventanaNuevoAAcoge = builder.get_object("consultaAAcoge")
		self.tbServicio = builder.get_object("tbServicio")
		self.tbTecnico = builder.get_object("tbTecnico")
		self.tbFechaConsulta = builder.get_object("tbFechaConsulta")
		self.tbObserv = builder.get_object("tbObserv")
		self.btAceptarConsultaAcoge = builder.get_object("btAceptarConsultaAcoge")
		self.btEliminarConsultaAcoge = builder.get_object("btEliminarConsultaAcoge")
		self.fixed6 = builder.get_object("fixed6")	
	
		#cursoLabora	
		self.ventanaCursoLabora = builder.get_object("cursoLabora")
		self.tbTitulo = builder.get_object("tbTitulo")
		self.tbFechaInicio = builder.get_object("tbFechaInicio")
		self.tbObjetivos = builder.get_object("tbObjetivos")
		self.cbxEstado = builder.get_object("cbxEstado")
	
		#practicaLabora	
		self.ventanaPracticaLabora = builder.get_object("practicaLabora")
		self.tbInicioPractica = builder.get_object("tbInicioPractica")
		self.tbFinPractica = builder.get_object("tbFinPractica")
		self.tbEmpresaPractica = builder.get_object("tbEmpresaPractica")
		self.tbDireccionEmpresaPractica = builder.get_object("tbDireccionEmpresaPractica")
		self.tbTelefonoEmpresaPractica = builder.get_object("tbTelefonoEmpresaPractica")
		self.tbMailEmpresaPractica = builder.get_object("tbMailEmpresaPractica")
		self.tbContactoEmpresaPractica = builder.get_object("tbContactoEmpresaPractica")
		self.cbxContrato = builder.get_object("cbxContrato")

		#empresaExtranj
		self.ventanaNuevoEmpleoExtranj = builder.get_object("empresaExtranj")
		self.tbEmpresa = builder.get_object("tbEmpresa")
		self.tbFechaInicioEmpresa = builder.get_object("tbFechaInicioEmpresa")
		self.tbDuracion = builder.get_object("tbDuracion")
	
		#propuestaExTut
		self.ventanaPropExtut = builder.get_object("propuestaExTut")
		self.cbxEntidadExtut = builder.get_object("cbxEntidadExtut")
		self.tbFechaEntidad = builder.get_object("tbFechaEntidad")

		#reunionesExtut
		self.ventanaReunionesExtut = builder.get_object("reunionesExTut")
		self.cbxEntidadReunion = builder.get_object("cbxEntidadReunion")
		self.cbxTipoReunion = builder.get_object("cbxTipoReunion")
		self.tbFechaReunion = builder.get_object("tbFechaReunion")
		self.tbAcuerdosReunion = builder.get_object("tbAcuerdosReunion")

		#empresaExtut
		self.ventanaEmpresaExTut = builder.get_object("empresaExTut")
		self.tbEntidad = builder.get_object("tbEntidad")
		self.tbDireccionEntidad = builder.get_object("tbDireccionEntidad")
		self.tbTelefonoEntidad = builder.get_object("tbTelefonoEntidad")
		self.tbMailEntidad = builder.get_object("tbMailEntidad")

		#obtenemos los liststore
		self.lsCursoLabora = builder.get_object("lsCursoLabora")
		self.lsEstadoCivil = builder.get_object("lsEstadoCivil")
		self.lsEstadoPermisoTrabajo = builder.get_object("lsEstadoPermisoTrabajo")
		self.lsFamReg = builder.get_object("lsFamReg")
		self.lsFormacion = builder.get_object("lsFormacion")
		self.lsPHC = builder.get_object("lsPHC")
		self.lsParentesco = builder.get_object("lsParentesco")
		self.lsPracticas = builder.get_object("lsPracticas")
		self.lsSitLabMenor = builder.get_object("lsSitLabMenor")
		self.lsSitLaboral = builder.get_object("lsSitLaboral")
		self.lsSitLegal = builder.get_object("lsSitLegal")
		self.lsTipoPermisoTrabajo = builder.get_object("lsTipoPermisoTrabajo")
		self.lsTipoVivienda = builder.get_object("lsTipoVivienda")
		self.lsMedidaInternamiento = builder.get_object("lsMedidaInternamiento")
		self.lsPrivilegio = builder.get_object("lsPrivilegio")
		self.lstvFamiliares = builder.get_object("lstvFamiliares")
		self.lsTipoContacto = builder.get_object("lsTipoContacto")
		self.lstvContacFam = builder.get_object("lstvContacFam")
		self.lstvContacTs = builder.get_object("lstvContacTs")
		self.lstvCitaSAE = builder.get_object("lstvCitaSAE")
		self.lstvCitaOrienta = builder.get_object("lstvCitaOrienta")
		self.lsTecReg = builder.get_object("lsTecReg")
		self.lstvAAcoge = builder.get_object("lstvAAcoge")

		#aplicar cambio de color a los fondos del notebook
		self.acambiar8.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar9.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar2.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar3.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar4.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar5.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))
		self.acambiar24.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#DCDCDC"))

		#Obtenemos el msgbox
		self.msgbox = builder.get_object("msgbox")
		self.lbMsgBox = builder.get_object("lbMsgBox")
		self.btMsgBoxAceptar = builder.get_object("btMsgBoxAceptar")

		dict = {"on_btAceptar_clicked":self.btAceptarClick,
				"on_btConvivencia_clicked": self.btConvivenciaClick,
				"on_unidadConvivencia_delete_event": self.uCDelete,
				"on_btMsgBoxAceptar_clicked": self.btMsgBoxAceptarClick,
				"on_btAceptarFamiliar_clicked": self.btAceptarFamiliarClick,
				"on_btNuevoCF_clicked": self.btNuevoCFClick,
				"on_contactosFamiliares_delete_event": self.contactosFamiliaresDelete,
				"on_selecFam_delete_event": self.selecFamDelete,
				"on_btSeleccFam_clicked": self.btSelecFamClick,
				"on_btNuevoContTS_clicked": self.btNuevoContTSClick,
				"on_contactosTS_delete_event": self.contactosTSDelete,
				"on_btSelecFam2_clicked": self.btSelecFamClick2,
				"on_btProxCitaSAE_clicked": self.btProxCitaSAEClick,
				"on_proxCitaSAE_delete_event": self.proxCitaSAEDelete,
				"on_btNuevoAAcoge_clicked": self.btNuevoAAcogeClick,
				"on_consultaAAcoge_delete_event": self.consultaAAcogeDelete,
				"on_btNuevoLabora_clicked": self.btNuevoLaboraClick,
				"on_cursoLabora_delete_event": self.cursoLaboraDelete,
				"on_btPracticaLabora_clicked": self.btPracticaLaboraClick,
				"on_practicaLabora_delete_event": self.practicaLaboraDelete,
				"on_btNuevoExtranj_clicked": self.btNuevoExtranjClick,
				"on_empresaExtranj_delete_event": self.empresaExtranjDelete,
				"on_btPropExtut_clicked": self.btPropExtutClick,
				"on_propuestaExTut_delete_event": self.propuestaExTutDelete,
				"on_btReunionExtut_clicked": self.btReunionExtutClick,
				"on_reunionesExTut_delete_event": self.reunionesExTutDelete,
				"on_btEmpesaExtut_clicked": self.empresaExTutClick,
				"on_btEmpresExTut2_clicked": self.empresaExTutClick,
				"on_empresaExTut_delete_event": self.empresaExTutDelete,
				"on_btDetalleConv_clicked": self.btDetalleConvClick,
				"on_btEliminarFam_clicked": self.btEliminarFamClick,
				"on_btAceptarSelecFam_clicked": self.btAceptarSelecFamClick,
				"on_btAceptarContacFam_clicked": self.btAceptarContacFamClick,
				"on_btBorrarContactoFam_clicked": self.btBorrarContactoFamClick,
				"on_btDetalleConFam_clicked": self.btDetalleConFamClick,
				"on_btEliminarConTS_clicked": self.btEliminarConTSClick,
				"on_btAceptarCTS_clicked": self.btAceptarCTSClick,
				"on_btDetalleConProf_clicked": self.btDetalleConProfClick,
				"on_btAceptarCitaSAE_clicked": self.btAceptarCitaSAEClick,
				"on_btDetalleCitaSAE_clicked": self.btDetalleCitaSAEClick,
				"on_btEliminarCita_clicked": self.btEliminarCitaClick,
				"on_btProxCitaOrienta_clicked": self.btProxCitaOrientaClick,
				"on_btAceptarCitaOrienta_clicked": self.btAceptarCitaOrientaClick,
				"on_btDetalleCitaOrienta_clicked": self.btDetalleCitaOrientaClick,
				"on_proxCitaOrienta_delete_event": self.proxCitaOrientaDelete,
				"on_btEliminarCitaOrienta_clicked": self.btEliminarCitaOrientaClick,
				"on_btSeleccionarOrientador_clicked": self.btSeleccionarOrientadorClick,
				"on_selecTecnico_delete_event": self.selecTecnicoDelete,
				"on_btAceptarConsultaAcoge_clicked": self.btAceptarConsultaAcogeClick,
				"on_btSelecTecnico_clicked": self.btSelecTecnicoClick,
				"on_btAceptarSelecTecnico_clicked": self.btAceptarSelecTecnicoClick,
				"on_btDetalleConsultaAAcoge_clicked": self.btDetalleConsultaAAcogeClick,
				"on_btEliminarConsultaAcoge_clicked": self.btEliminarConsultaAAcogeClick
				} 
		builder.connect_signals(dict)


	def cargarDatos(self, *argv):
		self.lbCentroActivo.set_text(argv[0])
		self.lbMostrarExpdte.set_text(argv[1])
		self.lbMostrarNombre.set_text(argv[2])
		self.lbMostrarDNI.set_text(argv[3])

		#consultamos el idmenor
		queryConsultarIdMenor = "SELECT MENOR.IdMenor FROM MENOR, EXPEDIENTE WHERE EXPEDIENTE.IdExpdte = \"" + self.lbMostrarExpdte.get_text() + "\" AND EXPEDIENTE.IdMenor = MENOR.IdMenor"
			
		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryConsultarIdMenor)
		except Exception, e:
			raise e

		idm = cursor.fetchone()
		global idmenor 
		idmenor = str(idm[0])


		queryCargarDatos1 = "SELECT AREA_SOCIAL.SitOtrosCentros, AREA_SOCIAL.PHC, AREA_SOCIAL.MedidaInternamiento, AREA_SOCIAL.TipoVivienda, AREA_SOCIAL.CaracVivienda, AREA_SOCIAL.SitEconLabFam, AREA_SOCIAL.SitSanitFam, AREA_SOCIAL.FormacionReglada, AREA_SOCIAL.FormacionComplementaria, AREA_SOCIAL.SitLabActual, AREA_SOCIAL.SitLabDetalle, AREA_SOCIAL.SitLegal, AREA_SOCIAL.SitLegalDetalle, AREA_SOCIAL.EntornoSocial, AREA_SOCIAL.DiagSocial, AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

		try:
			cursor.execute(queryCargarDatos1)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		consultado1 = cursor.fetchone()

		if consultado1 != None:
			textbuffer = self.tbAntecedentes.get_buffer() 
 			textbuffer.set_text(consultado1[0]) 

			for posicion, elemento in enumerate(self.lsPHC):
				f = elemento[0]
				if f == consultado1[1]:
					self.cbxPHC.set_active(posicion)

			for posicion, elemento in enumerate(self.lsMedidaInternamiento):
				f = elemento[0]
				if f == consultado1[2]:
					self.cbxMedidaInternamiento.set_active(posicion)

			for posicion, elemento in enumerate(self.lsTipoVivienda):
				f = elemento[0]
				if f == consultado1[3]:
					self.cbxTipoVivienda.set_active(posicion)

			textbuffer2 = self.tbCaracViv.get_buffer() 
 			textbuffer2.set_text(consultado1[4]) 

 			textbuffer3 = self.tbEconomiaFamiliar.get_buffer() 
 			textbuffer3.set_text(consultado1[5]) 

 			textbuffer4 = self.tbSanidadFamiliar.get_buffer() 
 			textbuffer4.set_text(consultado1[6]) 

 			for posicion, elemento in enumerate(self.lsFormacion):
				f = elemento[0]
				if f == consultado1[7]:
					self.cbxFormReglada.set_active(posicion)

			textbuffer5 = self.tbFormCompl.get_buffer() 
 			textbuffer5.set_text(consultado1[8]) 

 			for posicion, elemento in enumerate(self.lsSitLaboral):
				f = elemento[0]
				if f == consultado1[9]:
					self.cbxSitLaboral.set_active(posicion)

			textbuffer6 = self.tbExperiencia.get_buffer() 
 			textbuffer6.set_text(consultado1[10]) 

 			for posicion, elemento in enumerate(self.lsSitLegal):
				f = elemento[0]
				if f == consultado1[11]:
					self.cbxSitJud.set_active(posicion)

			textbuffer7 = self.tbDetalleLegal.get_buffer() 
 			textbuffer7.set_text(consultado1[12]) 

 			textbuffer8 = self.tbEntorno.get_buffer() 
 			textbuffer8.set_text(consultado1[13]) 

 			textbuffer9 = self.tbDiagnostico.get_buffer() 
 			textbuffer9.set_text(consultado1[14]) 

		else:
			pass
	
		queryCargarDatos2 = "SELECT SAE.OficinaSAE, SAE.DireccionOficinaSAE, SAE.Telefono, SAE.IdSAE FROM SAE WHERE SAE.IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryCargarDatos2)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		consultado2 = cursor.fetchone()

		if consultado2 != None:
			self.tbOficina.set_text(consultado2[0])
			self.tbDireccionOficina.set_text(consultado2[1])
			self.tbTelefonoOficina.set_text(str(consultado2[2]))

			sae = str(consultado2[3])

			queryConsultarDemandaSAE = "SELECT SAE_DEMANDA.FechaInscripcion, SAE_DEMANDA.FechaRenovacion, SAE_DEMANDA.FechaCaducidadAdmva FROM SAE_DEMANDA WHERE SAE_DEMANDA.IdSAE = \'" + sae + "\'"

			try:
				cursor.execute(queryConsultarDemandaSAE)
			except Exception, e:
				raise e

			consultaDemanda = cursor.fetchone()

			if consultaDemanda != None:
				dateFormat = consultaDemanda[0].strftime("%d/%m/%Y")
				self.tbInscripcion.set_text(dateFormat)

				dateFormat2 = consultaDemanda[1].strftime("%d/%m/%Y")
				self.tbRenovacion.set_text(dateFormat2)

				dateFormat3 = consultaDemanda[2].strftime("%d/%m/%Y")
				self.tbCadAdmva.set_text(dateFormat3)
			else:
				pass

		else:
			pass

		queryCargarDatos3 = "SELECT ORIENTA.Oficina, ORIENTA.Direccion, ORIENTA.Telefono, ORIENTA.Orientador, ORIENTA.FechaInicio FROM ORIENTA WHERE ORIENTA.IdMenor = \'" + idmenor + "\'"
		
		try:
			cursor.execute(queryCargarDatos3)
		except Exception, e:
			raise e

		consultado3 = cursor.fetchone()

		if consultado3 != None:
			self.tbOficinaOrienta.set_text(consultado3[0])
			self.tbDireccionOrienta.set_text(consultado3[1])
			self.tbTelefonoOrienta.set_text(str(consultado3[2]))
			self.tbOrientador.set_text(consultado3[3])
			
			dateFormat4 = consultado3[4].strftime("%d/%m/%Y")
			self.tbFechaInicioOrienta.set_text(dateFormat4)

		else:
			pass

		queryCargarDatos4 = "SELECT LABORA.OrientadorLabora, LABORA.Telefono, LABORA.ActuacionesPracticas FROM LABORA WHERE LABORA.IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryCargarDatos4)
		except Exception, e:
			raise e

		consultado4 = cursor.fetchone()

		if consultado4 != None:
			self.tbOrientadorLabora.set_text(consultado4[0])
			self.tbTelefonoLabora.set_text(str(consultado4[1]))
			
			for posicion, elemento in enumerate(self.lsPracticas):
				f = elemento[0]
				if f == consultado4[2]:
					self.cbxPracticasLabora.set_active(posicion)

		else:
			pass			

		queryCargarDatos5 = "SELECT EXTRANJERIA.TipoPermiso, EXTRANJERIA.FechaExpedicion, EXTRANJERIA.FechaRenovacion, EXTRANJERIA.PermisoTrabajo, EXTRANJERIA.PermisoExcepTrabajo FROM EXTRANJERIA WHERE EXTRANJERIA.IdMenor = \'" + idmenor + "\'"	

		try:
			cursor.execute(queryCargarDatos5)
		except Exception, e:
			raise e

		consultado5 = cursor.fetchone()

		if consultado5 != None:
			for posicion, elemento in enumerate(self.lsTipoPermisoTrabajo):
				f = elemento[0]
				if f == consultado5[0]:
					self.cbxPermisoExtranj.set_active(posicion)

			dateFormat5 = consultado5[1].strftime("%d/%m/%Y")
			self.tbFechaExpedicionPermiso.set_text(dateFormat5)

			dateFormat6 = consultado5[2].strftime("%d/%m/%Y")
			self.tbFechaRenovacionPermiso.set_text(dateFormat6)

			for posicion, elemento in enumerate(self.lsEstadoPermisoTrabajo):
				f = elemento[0]
				if f == consultado5[3]:
					self.cbxPermisoTrabajo.set_active(posicion)
			
			for posicion, elemento in enumerate(self.lsEstadoPermisoTrabajo):
				f = elemento[0]
				if f == consultado5[4]:
					self.cbxPermisoExcepTrabajo.set_active(posicion)

		else:
			pass			
		


		#ahora voy a cargar los treeviews
		self.cargartvFamiliares()
		self.cargartvContacFam()
		self.cargartvContacTs()
		self.cargartvCitasSAE()
		self.cargartvCitasOrienta()
		self.cargartvConsultasAACoge()
		

		cursor.close()	

	def cargartvFamiliares(self):
		self.lstvFamiliares.clear()

		c = conexion.db
		cursor = c.cursor()

		queryCargarDatos1 = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

		try:
			cursor.execute(queryCargarDatos1)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		consultado1 = cursor.fetchone()

		if consultado1 != None:
			querytvFamiliares = "SELECT UC.NombreConviv, UC.Parentesco, UC.IdUC FROM UC  WHERE UC.IdSocial = \'" + str(consultado1[0]) + "\'"

			try:
				cursor.execute(querytvFamiliares)
			except Exception, e:
				raise e

			resultadoFam = cursor.fetchall()

			if len(resultadoFam) != 0:
				for i in range(len(resultadoFam)):
					self.lstvFamiliares.append(resultadoFam[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()	

	def cargartvContacFam(self):
		self.lstvContacFam.clear()

		c = conexion.db
		cursor = c.cursor()

		queryCargarDatos1 = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

		try:
			cursor.execute(queryCargarDatos1)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		consultado1 = cursor.fetchone()

		if consultado1 != None:
			querytvContactosFamiliares = "SELECT TipoContacto, PersonaContacto, FechaContacto, IdRCF FROM REGIMEN_CONTACTOS_FAMILIA WHERE IdSocial = \'" + str(consultado1[0]) + "\' ORDER BY FechaContacto DESC"

			try:
				cursor.execute(querytvContactosFamiliares)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvContacFam.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()	

	def cargartvContacTs(self):
		self.lstvContacTs.clear()

		c = conexion.db
		cursor = c.cursor()

		queryCargarDatos = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

		try:
			cursor.execute(queryCargarDatos)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		consultado1 = cursor.fetchone()

		if consultado1 != None:
			querytvContactosTs = "SELECT FamiliarContacto, FechaContacto, IdRCTs FROM REGIMEN_CONTACTOS_TS WHERE IdSocial = \'" + str(consultado1[0]) + "\' ORDER BY FechaContacto DESC"

			try:
				cursor.execute(querytvContactosTs)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvContacTs.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()	

	def cargartvCitasSAE(self):
		self.lstvCitaSAE.clear()

		c = conexion.db
		cursor = c.cursor()
		
		queryObtenerIdSAE = "SELECT SAE.IdSAE FROM SAE WHERE SAE.IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryObtenerIdSAE)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		comprobacion = cursor.fetchone()
			
		
		if comprobacion != None:
			querytvCitasSAE = "SELECT SAE_CITAS.FechaCita, SAE_CITAS.InformeCita, SAE_CITAS.IdCita FROM SAE, SAE_CITAS WHERE SAE.IdMenor = \'" + idmenor + "\' AND SAE.IdSAE = \'" + str(comprobacion[0]) + "\' AND SAE.IdSAE = SAE_CITAS.IdSAE ORDER BY SAE_CITAS.FechaCita DESC"

			try:
				cursor.execute(querytvCitasSAE)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvCitaSAE.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()	

	def cargartvCitasOrienta(self):
		self.lstvCitaOrienta.clear()

		c = conexion.db
		cursor = c.cursor()
		
		queryObtenerIdOrienta = "SELECT ORIENTA.IdOrienta FROM ORIENTA WHERE ORIENTA.IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryObtenerIdOrienta)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		comprobacion = cursor.fetchone()
			
		
		if comprobacion != None:
			querytvCitasOrienta = "SELECT ORIENTA_CITAS.FechaCita, ORIENTA_CITAS.Observaciones, ORIENTA_CITAS.IdCitaOrienta FROM ORIENTA, ORIENTA_CITAS WHERE ORIENTA.IdMenor = \'" + idmenor + "\' AND ORIENTA.IdOrienta = \'" + str(comprobacion[0]) + "\' AND ORIENTA.IdOrienta = ORIENTA_CITAS.IdOrienta ORDER BY ORIENTA_CITAS.FechaCita DESC"

			try:
				cursor.execute(querytvCitasOrienta)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvCitaOrienta.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()	

	def cargartvConsultasAACoge(self):
		self.lstvAAcoge.clear()

		c = conexion.db
		cursor = c.cursor()
		
		querytvConsultasAAcoge = "SELECT ServicioConsultado, Tecnico, FechaConsulta, IdAAcoge FROM AACOGE WHERE IdMenor = \'" + idmenor + "\' ORDER BY FechaConsulta DESC"

		try:
			cursor.execute(querytvConsultasAAcoge)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lstvAAcoge.append(resultado[i])
		

		cursor.close()	

	def btAceptarClick(self, widget):#Este es el boton Acutalizar Pestaña
		paginaActual = self.notebook1.get_current_page()
	
		if paginaActual == 0:
			a = self.tbAntecedentes.get_buffer()
			anteced = a.get_text(*a.get_bounds())
			prestacion = self.cbxPHC.get_active_text()
			medida = self.cbxMedidaInternamiento.get_active_text()

			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarAntecedentes = "UPDATE AREA_SOCIAL SET SitOtrosCentros = \'" + anteced + "\', PHC = \'" + prestacion + "\', MedidaInternamiento = \'" + medida + "\' WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryActualizarAntecedentes)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			else:
				expdte = self.lbMostrarExpdte.get_text()
				queryInsertarAntecedentes = "INSERT INTO AREA_SOCIAL (SitOtrosCentros, PHC, MedidaInternamiento, IdExpdte) VALUES (\'" + anteced + "\', '" + prestacion + "\', '" + medida + "\', '" + expdte + "\')"

				try:
					cursor.execute(queryInsertarAntecedentes)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 1:
			tipoViv = self.cbxTipoVivienda.get_active_text()
			c = self.tbCaracViv.get_buffer()
			caracViv = c.get_text(*c.get_bounds())

			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarConvivencia = "UPDATE AREA_SOCIAL SET TipoVivienda = \'" + tipoViv + "\', CaracVivienda = \'" + caracViv + "\' WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryActualizarConvivencia)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarConvivencia = "INSERT INTO AREA_SOCIAL (TipoVivienda, CaracVivienda, IdExpdte) VALUES (\'" + tipoViv + "\', '" + caracViv + "\', '" + self.lbMostrarExpdte.get_text() + "\')"

				try:
					cursor.execute(queryInsertarConvivencia)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 2:
			ef = self.tbEconomiaFamiliar.get_buffer()
			economFam = ef.get_text(*ef.get_bounds())
			sf = self.tbSanidadFamiliar.get_buffer()
			sanidadFam = sf.get_text(*sf.get_bounds())

			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarEcSan = "UPDATE AREA_SOCIAL SET SitEconLabFam = \'" + economFam + "\', SitSanitFam = \'" + sanidadFam + "\' WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryActualizarEcSan)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarEcSan = "INSERT INTO AREA_SOCIAL (SitEconLabFam, SitSanitFam, IdExpdte) VALUES (\'" + economFam + "\', '" + sanidadFam + "\', '" + self.lbMostrarExpdte.get_text() + "\')"

				try:
					cursor.execute(queryInsertarEcSan)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 3:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 4:
			formRegl = self.cbxFormReglada.get_active_text()
			fc = self.tbFormCompl.get_buffer()
			formCompl = fc.get_text(*fc.get_bounds())
			sitLab = self.cbxSitLaboral.get_active_text()
			exp = self.tbExperiencia.get_buffer()
			experi = exp.get_text(*exp.get_bounds())

			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarForm = "UPDATE AREA_SOCIAL SET FormacionReglada = \'" + formRegl + "\', FormacionComplementaria = \'" + formCompl + "\', SitLabActual = \'" + sitLab + "\', SitLabDetalle = \'" + experi + "\' WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryActualizarForm)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarForm = "INSERT INTO AREA_SOCIAL (FormacionReglada, FormacionComplementaria, SitLabActual, SitLabDetalle, IdExpdte) VALUES (\'" + formRegl + "\', '" + formCompl + "\', '" + sitLab + "\', '" + experi + "\', '" + self.lbMostrarExpdte.get_text() + "\')"

				try:
					cursor.execute(queryInsertarForm)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 5:
			jud = self.cbxSitJud.get_active_text()
			l = self.tbDetalleLegal.get_buffer()
			legal = l.get_text(*l.get_bounds())
			ent = self.tbEntorno.get_buffer()
			entorno = ent.get_text(*ent.get_bounds())

			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarLegal = "UPDATE AREA_SOCIAL SET SitLegal = \'" + jud + "\', SitLegalDetalle = \'" + legal + "\', EntornoSocial = \'" + entorno + "\' WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryActualizarLegal)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarLegal = "INSERT INTO AREA_SOCIAL (SitLegal, SitLegalDetalle, EntornoSocial, IdExpdte) VALUES (\'" + jud + "\', '" + legal + "\', '" + entorno + "\', '" + self.lbMostrarExpdte.get_text() + "\')"

				try:
					cursor.execute(queryInsertarLegal)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 6:
			d = self.tbDiagnostico.get_buffer()
			diag = d.get_text(*d.get_bounds())

			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarDiag = "UPDATE AREA_SOCIAL SET DiagSocial = \'" + diag + "\' WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryActualizarDiag)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarDiag = "INSERT INTO AREA_SOCIAL (DiagSocial, IdExpdte) VALUES (\'" + diag + "\', '" + self.lbMostrarExpdte.get_text() + "\')"

				try:
					cursor.execute(queryInsertarDiag)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 7:
			ofi = self.tbOficina.get_text()
			direc = self.tbDireccionOficina.get_text()
			tlfn = self.tbTelefonoOficina.get_text()
			inscripText = self.tbInscripcion.get_text()
			renovText = self.tbRenovacion.get_text()
			cadAdText = self.tbCadAdmva.get_text()

			day = datetime.datetime.strptime(inscripText, '%d/%m/%Y')
			inscrip = day.strftime('%Y-%m-%d')
			day2 = datetime.datetime.strptime(renovText, '%d/%m/%Y')
			renov = day2.strftime('%Y-%m-%d')
			day3 = datetime.datetime.strptime(cadAdText, '%d/%m/%Y')
			cadAd = day3.strftime('%Y-%m-%d')
			
			queryComprobarRegistro = "SELECT SAE.IdMenor FROM SAE WHERE IdMenor = \'" + idmenor + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarSAE = "UPDATE SAE SET OficinaSAE = \'" + ofi + "\', DireccionOficinaSAE = \'" + direc + "\', Telefono = \'" + tlfn + "\' WHERE IdMenor = \'" + idmenor + "\'"
				try:
					cursor.execute(queryActualizarSAE)
					c.commit()
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarSAE = "INSERT INTO SAE (OficinaSAE, DireccionOficinaSAE, Telefono, IdMenor) VALUES (\'" + ofi + "\', '" + direc + "\', '" + tlfn + "\', '" + idmenor + "\')"

				try:
					cursor.execute(queryInsertarSAE)
					c.commit()
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			
			queryConsultarIdSAE = "SELECT SAE.IdSAE FROM SAE WHERE IdMenor = \'" + idmenor + "\'"

			try:
				cursor.execute(queryConsultarIdSAE)
			except Exception, e:
				raise e

			resultadoConsultaSAE = cursor.fetchone()
			idsae = str(resultadoConsultaSAE[0])

			queryComprobarRegistro2 = "SELECT SAE_DEMANDA.IdSAE FROM SAE_DEMANDA WHERE IdSAE = \'" + idsae + "\'"

			try:
				cursor.execute(queryComprobarRegistro2)
			except Exception, e:
				raise e

			comprobacion2 = cursor.fetchone()

			if comprobacion2 != None:
				queryActualizarDemanda = "UPDATE SAE_DEMANDA SET FechaInscripcion = \'" + inscrip + "\', FechaRenovacion = \'" + renov + "\', FechaCaducidadAdmva = \'" + cadAd + "\' WHERE IdSAE = \'" + idsae + "\'"
				try:
					cursor.execute(queryActualizarDemanda)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar1")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarDemanda = "INSERT INTO SAE_DEMANDA (FechaInscripcion, FechaRenovacion, FechaCaducidadAdmva, IdSAE) VALUES (\'" + inscrip + "\', '" + renov + "\', '" + cadAd + "\', '" + idsae + "\')"
				try:
					cursor.execute(queryInsertarDemanda)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar2" + str(queryInsertarDemanda))
					self.btMsgBoxAceptar.set_label("Cerrar")


			cursor.close()
		
		elif paginaActual == 8:
			ofic = self.tbOficinaOrienta.get_text()
			dire = self.tbDireccionOrienta.get_text()
			tlfno = self.tbTelefonoOrienta.get_text()
			orientador = self.tbOrientador.get_text()
			fi = self.tbFechaInicioOrienta.get_text()
			day = datetime.datetime.strptime(fi, '%d/%m/%Y')
			fechaInic = day.strftime('%Y-%m-%d')

			queryComprobarRegistro = "SELECT ORIENTA.IdMenor FROM ORIENTA WHERE IdMenor = \'" + idmenor + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarOrienta = "UPDATE ORIENTA SET Oficina = \'" + ofic + "\', Direccion = \'" + dire + "\', Telefono = \'" + tlfno + "\', Orientador = \'" + orientador + "\', FechaInicio = \'" + fechaInic + "\' WHERE IdMenor = \'" + idmenor + "\'"

				try:
					cursor.execute(queryActualizarOrienta)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarOrienta = "INSERT INTO ORIENTA (Oficina, Direccion, Telefono, Orientador, FechaInicio, IdMenor) VALUES (\'" + ofic + "\', '" + dire + "\', '" + tlfno + "\', '" + orientador + "\', '" + fechaInic + "\', '" + idmenor + "\')"

				try:
					cursor.execute(queryInsertarOrienta)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 9:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 10:
			orient = self.tbOrientadorLabora.get_text()
			tfno = self.tbTelefonoLabora.get_text()
			actPrac = self.cbxPracticasLabora.get_active_text()

			queryComprobarRegistro = "SELECT LABORA.IdMenor FROM LABORA WHERE IdMenor = \'" + idmenor + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarLabora = "UPDATE LABORA SET OrientadorLabora = \'" + orient + "\', Telefono = \'" + tfno + "\', ActuacionesPracticas = \'" + actPrac + "\' WHERE IdMenor = \'" + idmenor + "\'"

				try:
					cursor.execute(queryActualizarLabora)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarLabora = "INSERT INTO LABORA (OrientadorLabora, Telefono, ActuacionesPracticas, IdMenor) VALUES (\'" + orient + "\', '" + tfno + "\', '" + actPrac + "\', '" + idmenor + "\')"

				try:
					cursor.execute(queryInsertarLabora)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 11:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 12:
			permExt = self.cbxPermisoExtranj.get_active_text()
			fE = self.tbFechaExpedicionPermiso.get_text()
			day = datetime.datetime.strptime(fE, '%d/%m/%Y')
			fechaExpdc = day.strftime('%Y-%m-%d')
			fR = self.tbFechaRenovacionPermiso.get_text()
			day2 = datetime.datetime.strptime(fR, '%d/%m/%Y')
			fechaRenov = day2.strftime('%Y-%m-%d')
			permTr = self.cbxPermisoTrabajo.get_active_text()
			permExcTr = self.cbxPermisoExcepTrabajo.get_active_text()

			queryComprobarRegistro = "SELECT EXTRANJERIA.IdMenor FROM EXTRANJERIA WHERE IdMenor = \'" + idmenor + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarExtranjeria = "UPDATE EXTRANJERIA SET TipoPermiso = \'" + permExt + "\', FechaExpedicion = \'" + fechaExpdc + "\', FechaRenovacion = \'" + fechaRenov + "\', PermisoTrabajo = \'" + permTr + "\', PermisoExcepTrabajo = \'" + permExcTr + "\' WHERE IdMenor = \'" + idmenor + "\'"

				try:
					cursor.execute(queryActualizarExtranjeria)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarExtranjeria = "INSERT INTO EXTRANJERIA (TipoPermiso, FechaExpedicion, FechaRenovacion, PermisoTrabajo, PermisoExcepTrabajo, IdMenor) VALUES (\'" + permExt + "\', '" + fechaExpdc + "\', '" + fechaRenov + "\', '" + permTr + "\', '" + permExcTr + "\', '" + idmenor + "\')"

				try:
					cursor.execute(queryInsertarExtranjeria)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Actualizado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("No se pudo actualizar")
					self.btMsgBoxAceptar.set_label("Cerrar")

			cursor.close()

		elif paginaActual == 13:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 14:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

	def btConvivenciaClick(self, widget):
		self.ventanaUC.show()
		self.btAceptarFamiliar.set_label("Aceptar")
		self.fixed1.move(self.btAceptarFamiliar, 135, 0)
		self.btEliminarFam.set_visible(False)

		self.tbFamiliarReg.set_text("")
		self.tbNacFamiliar.set_text("")
		self.cbxParentesco.set_active(0)
		self.cbxConv.set_active(0)
		self.tbDireccionFamiliar.set_text("")
		self.tbTelefonoFamiliar.set_text("")
		self.tbMailFamiliar.set_text("")
		self.cbxSitLabFamiliar.set_active(0)
		self.cbxPrivilegio.set_active(0)
		
	def btAceptarFamiliarClick(self, widget):
		fam = self.tbFamiliarReg.get_text()
		
		fN = self.tbNacFamiliar.get_text()
		day = datetime.datetime.strptime(fN, '%d/%m/%Y')
		fNac = day.strftime('%Y-%m-%d')
		
		paren = self.cbxParentesco.get_active_text()
		conv = self.cbxConv.get_active_text()
		dire = self.tbDireccionFamiliar.get_text()
		tlf = self.tbTelefonoFamiliar.get_text()
		mail = self.tbMailFamiliar.get_text()
		sitL = self.cbxSitLabFamiliar.get_active_text()
		privi = self.cbxPrivilegio.get_active_text()

		
		if str(self.btAceptarFamiliar.get_label()) == "Aceptar":
			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryInsertarFamiliar = "INSERT INTO UC (NombreConviv, FechaNacConviv, Parentesco, SitLabConviv, DireccionConviv, TelefonoConviv, MailConviv, Conviviente, Privilegio, IdSocial) VALUES (\'" + fam + "\', '" + fNac + "\', '" + paren + "\', '" + sitL + "\', '" + dire + "\', '" + tlf + "\', '" + mail + "\', '" + conv + "\', '" + privi + "\', '" + str(comprobacion[0]) + "\')"

				try:
					cursor.execute(queryInsertarFamiliar)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Registrado con éxito")
					self.btMsgBoxAceptar.set_label(" Cerrar ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("El registro ha fallado")
					self.btMsgBoxAceptar.set_label("Cerrar")
			else:
				queryInsertarAreaSocial = "INSERT INTO AREA_SOCIAL (IdExpdte) VALUES (\'" + self.lbMostrarExpdte.get_text() + "\')"

				try:
					cursor.execute(queryInsertarAreaSocial)
					c.commit()
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el programa")
					self.btMsgBoxAceptar.set_label("Cerrar")

				try:
					cursor.execute(queryComprobarRegistro)
				except Exception, e:
					raise e

				nuevaComprobacion = cursor.fetchone()

				queryInsertarFamiliar = "INSERT INTO UC (NombreConviv, FechaNacConviv, Parentesco, SitLabConviv, DireccionConviv, TelefonoConviv, MailConviv, Conviviente, Privilegio, IdSocial) VALUES (\'" + fam + "\', '" + fNac + "\', '" + paren + "\', '" + sitL + "\', '" + dire + "\', '" + tlf + "\', '" + mail + "\', '" + conv + "\', '" + privi + "\', '" + str(nuevaComprobacion[0]) + "\'"

				try:
					cursor.execute(queryInsertarFamiliar)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Registrado con éxito")
					self.btMsgBoxAceptar.set_label("Cerrar")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("El registro ha fallado")
					self.btMsgBoxAceptar.set_label("Cerrar")

				self.cargartvFamiliares()

		elif self.btAceptarFamiliar.get_label() == "Actualizar":
			tv = self.tvUC	
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				iduc = model[treeiter][2]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarFamiliar = "UPDATE UC SET NombreConviv = \'" + fam + "\', FechaNacConviv = \'" + fNac + "\', Parentesco = \'" + paren + "\', SitLabConviv = \'" + sitL + "\', DireccionConviv = \'" + dire + "\', TelefonoConviv = \'" + tlf + "\', MailConviv = \'" + mail + "\', Conviviente = \'" + conv + "\', Privilegio = \'" + privi + "\' WHERE IdUC = \'" + iduc + "\'"

			try:
				cursor.execute(queryActualizarFamiliar)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Actualizado con éxito")
				self.btMsgBoxAceptar.set_label(" Cerrar ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("Cerrar")

			self.cargartvFamiliares()
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("El proceso de actualización ha fallado")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()

	def btDetalleConvClick(self, widget):
		self.ventanaUC.show()
		self.btAceptarFamiliar.set_label("Actualizar")
		self.fixed1.move(self.btAceptarFamiliar, 70, 0)
		self.btEliminarFam.set_visible(True)
		self.fixed1.move(self.btEliminarFam, 180, 0)

		tv = self.tvUC	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			iduc = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleFam = "SELECT * FROM UC WHERE IdUC = \'" + iduc + "\'"

		try:
			cursor.execute(queryDetalleFam)
		except Exception, e:
			raise e

		resultadoDetalleFam = cursor.fetchone()

		if resultadoDetalleFam != None:
			self.tbFamiliarReg.set_text(str(resultadoDetalleFam[1]))
			dateFormat = resultadoDetalleFam[2].strftime("%d/%m/%Y") # fecha con formato
			self.tbNacFamiliar.set_text(dateFormat)
			
			for posicion, elemento in enumerate(self.lsParentesco):
				f = elemento[0]
				if f == str(resultadoDetalleFam[3]):
					self.cbxParentesco.set_active(posicion)

			for posicion, elemento in enumerate(self.lsSitLaboral):
				f = elemento[0]
				if f == str(resultadoDetalleFam[4]):
					self.cbxSitLabFamiliar.set_active(posicion)
		
			self.tbDireccionFamiliar.set_text(resultadoDetalleFam[5])
			self.tbTelefonoFamiliar.set_text(str(resultadoDetalleFam[6]))
			self.tbMailFamiliar.set_text(resultadoDetalleFam[7])

			for posicion, elemento in enumerate(self.lsPHC):
				f = elemento[0]
				if f == str(resultadoDetalleFam[8]):
					self.cbxConv.set_active(posicion)
					
			for posicion, elemento in enumerate(self.lsPrivilegio):
				f = elemento[0]
				if f == str(resultadoDetalleFam[9]):
					self.cbxPrivilegio.set_active(posicion)
	
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
	def btEliminarFamClick(self, widget):
		tv = self.tvUC	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			iduc = model[treeiter][2]
		
		c = conexion.db
		cursor = c.cursor()

		queryActualizarFamiliar = "DELETE FROM UC WHERE IdUC = \'" + iduc + "\'"
		
		try:
			cursor.execute(queryActualizarFamiliar)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminado con éxito")
			self.btMsgBoxAceptar.set_label(" Cerrar ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label(" Cerrar ")

		self.cargartvFamiliares()

		cursor.close()

	def uCDelete(self, widget, data=None):
		self.ventanaUC.hide()
		return True

	def btNuevoCFClick(self, widget):
		self.ventanaContacFam.show()
		self.btAceptarContacFam.set_label("Aceptar")
		self.fixed2.move(self.btAceptarContacFam, 145, 0)
		self.btBorrarContactoFam.set_visible(False)
		self.cbxTipo.set_active(0)
		self.tbContacto.set_text("")
		self.tbLugar.set_text("")
		self.tbFechaConFam.set_text("")
		self.tbHoraContacFam.set_text("")
		textbuffer = self.tbObservFam.get_buffer() 
 		textbuffer.set_text("")

	def btAceptarContacFamClick(self, widget):
		tipo = self.cbxTipo.get_active_text()
		pers = self.tbContacto.get_text()
		sitio = self.tbLugar.get_text()

		fC = self.tbFechaConFam.get_text()
		day = datetime.datetime.strptime(fC, '%d/%m/%Y')
		fechaCont = day.strftime('%Y-%m-%d')

		hora = self.tbHoraContacFam.get_text()
		ob = self.tbObservFam.get_buffer()
		observ = ob.get_text(*ob.get_bounds())

		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarContacFam.get_label() == "Aceptar":
			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e
			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryInsertarContacFam = "INSERT INTO REGIMEN_CONTACTOS_FAMILIA (TipoContacto, PersonaContacto, LugarContacto, FechaContacto, HoraContacto, ObservacionesContacto, IdSocial) VALUES (\'" + tipo + "\', '" + pers + "\', '" + sitio + "\', '" + fechaCont + "\', '" + hora + "\', '" + observ + "\', '" + str(comprobacion[0]) + "\')" 

				try:
					cursor.execute(queryInsertarContacFam)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Contacto registrado con éxito")
					self.btMsgBoxAceptar.set_label("  Cerrar  ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("  Cerrar  ")

				self.cargartvContacFam()

			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Fallo en el registro")
				self.btMsgBoxAceptar.set_label("Cerrar")

		elif self.btAceptarContacFam.get_label() == "Actualizar":
			tv = self.tvContactosFamiliares	
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idrcf = model[treeiter][3]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarContactFam = "UPDATE REGIMEN_CONTACTOS_FAMILIA SET TipoContacto = \'" + tipo + "\', PersonaContacto = \'" + pers + "\', LugarContacto = \'" + sitio + "\', FechaContacto = \'" + fechaCont + "\', HoraContacto = \'" + hora + "\', ObservacionesContacto = \'" + observ + "\' WHERE IdRCF = \'" + idrcf + "\'"

			try:
				cursor.execute(queryActualizarContactFam)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Actualizado con éxito")
				self.btMsgBoxAceptar.set_label("  Cerrar  ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("  Cerrar  ")

			self.cargartvContacFam()
		
		cursor.close()

	def btDetalleConFamClick(self, widget):
		self.ventanaContacFam.show()
		self.btAceptarContacFam.set_label("Actualizar")
		self.fixed2.move(self.btAceptarContacFam, 145, 0)
		self.btBorrarContactoFam.set_visible(True)
		self.fixed2.move(self.btBorrarContactoFam, 255, 0)

		tv = self.tvContactosFamiliares	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idrcf = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleContacFam = "SELECT * FROM REGIMEN_CONTACTOS_FAMILIA WHERE IdRCF = \'" + idrcf + "\'"

		try:
			cursor.execute(queryDetalleContacFam)
		except Exception, e:
			raise e

		resultadoDetalleContacFam = cursor.fetchone()

		if resultadoDetalleContacFam != None:
			for posicion, elemento in enumerate(self.lsTipoContacto):
				f = elemento[0]
				if f == str(resultadoDetalleContacFam[1]):
					self.cbxTipo.set_active(posicion)
		
			self.tbContacto.set_text(str(resultadoDetalleContacFam[2]))
			self.tbLugar.set_text(str(resultadoDetalleContacFam[3]))

 			dateFormat = resultadoDetalleContacFam[4].strftime("%d/%m/%Y") 
			self.tbFechaConFam.set_text(dateFormat)

			self.tbHoraContacFam.set_text(str(resultadoDetalleContacFam[5]))
			
			textbuffer = self.tbObservFam.get_buffer() 
 			textbuffer.set_text(str(resultadoDetalleContacFam[6]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btBorrarContactoFamClick(self, widget):
		tv = self.tvContactosFamiliares	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idrcf = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarContacFam = "DELETE FROM REGIMEN_CONTACTOS_FAMILIA WHERE IdRCF = \'" + idrcf + "\'"
		
		try:
			cursor.execute(queryBorrarContacFam)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminado con éxito")
			self.btMsgBoxAceptar.set_label("  Cerrar  ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("  Cerrar  ")

		self.cargartvContacFam()

		cursor.close()

	def contactosFamiliaresDelete(self, widget, data=None):
		self.ventanaContacFam.hide()
		return True

	def btSelecFamClick(self, widget):
		self.ventanaSelecFam.show()
		self.btAceptarSelecFam.set_label("Seleccionar")
		self.lsFamReg.clear()
		
		queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"
		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryComprobarRegistro)
		except Exception, e:
			raise e

		comprobacion = cursor.fetchone()
	
		if comprobacion != None:
			queryListaFamiliares = "SELECT UC.NombreConviv FROM UC WHERE IdSocial = \'" + str(comprobacion[0]) + "\'"

			try:
				cursor.execute(queryListaFamiliares)
			except Exception, e:
				raise e

			listadoFam = cursor.fetchall()

			for i in range(len(listadoFam)):
				self.lsFamReg.append(listadoFam[i])

		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los registros")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()

	def btAceptarSelecFamClick(self, widget):
		famSelec = self.cbxFamReg.get_active_text()
		self.ventanaSelecFam.hide()

		if self.btAceptarSelecFam.get_label() == "Seleccionar":
			self.tbContacto.set_text(famSelec)
		elif self.btAceptarSelecFam.get_label() == " Seleccionar ":
			self.tbFamiliar.set_text(famSelec)

	def selecFamDelete(self, widget, data=None):
		self.ventanaSelecFam.hide()
		return True

	def btSelecFamClick2(self, widget):
		self.ventanaSelecFam.show()
		self.btAceptarSelecFam.set_label(" Seleccionar ")
		self.lsFamReg.clear()
		
		queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"
		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryComprobarRegistro)
		except Exception, e:
			raise e

		comprobacion = cursor.fetchone()
	
		if comprobacion != None:
			queryListaFamiliares = "SELECT UC.NombreConviv FROM UC WHERE IdSocial = \'" + str(comprobacion[0]) + "\'"

			try:
				cursor.execute(queryListaFamiliares)
			except Exception, e:
				raise e

			listadoFam = cursor.fetchall()

			for i in range(len(listadoFam)):
				self.lsFamReg.append(listadoFam[i])

		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los registros")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()

	
	def btNuevoContTSClick(self, widget):
		self.ventanaContactosTS.show()
		self.btAceptarCTS.set_label("Aceptar")
		self.fixed3.move(self.btAceptarCTS, 145, 0)
		self.btEliminarConTS.set_visible(False)
		self.tbFamiliar.set_text("")
		self.tbFechaContTS.set_text("")
		self.tbHora.set_text("")
		textbuffer = self.tbDetalles.get_buffer()
		textbuffer.set_text("")

	def btAceptarCTSClick(self, widget):
		fam = self.tbFamiliar.get_text()
		
		fCTs = self.tbFechaContTS.get_text()
		day = datetime.datetime.strptime(fCTs, '%d/%m/%Y')
		fechaContTs = day.strftime('%Y-%m-%d')
				
		hora = self.tbHora.get_text()
		
		dt = self.tbDetalles.get_buffer()
		det = dt.get_text(*dt.get_bounds())
		
		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarCTS.get_label() == "Aceptar":
			queryComprobarRegistro = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e
			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryInsertarContacTs = "INSERT INTO REGIMEN_CONTACTOS_TS (FamiliarContacto, FechaContacto, HoraContacto, ObservacionesContacto, IdSocial) VALUES (\'" + fam + "\', '" + fechaContTs + "\', '" + hora + "\', '" + det + "\', '" + str(comprobacion[0]) + "\')" 

				try:
					cursor.execute(queryInsertarContacTs)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Contacto registrado con éxito")
					self.btMsgBoxAceptar.set_label("   Cerrar   ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("   Cerrar   ")

				self.cargartvContacTs()

			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Fallo en el registro")
				self.btMsgBoxAceptar.set_label("Cerrar")

		elif self.btAceptarCTS.get_label() == "Actualizar":
			tv = self.tvContactosProfesionales	
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idrcts = model[treeiter][2]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarContactTs = "UPDATE REGIMEN_CONTACTOS_TS SET FamiliarContacto = \'" + fam + "\', FechaContacto = \'" + fechaContTs + "\', HoraContacto = \'" + hora + "\', ObservacionesContacto = \'" + det + "\' WHERE IdRCTs = \'" + idrcts + "\'"

			try:
				cursor.execute(queryActualizarContactTs)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Actualizado con éxito")
				self.btMsgBoxAceptar.set_label("   Cerrar   ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("   Cerrar   ")

			self.cargartvContacTs()
		
		cursor.close()

	def btDetalleConProfClick(self, widget):
		self.ventanaContactosTS.show()
		self.btAceptarCTS.set_label("Actualizar")
		self.fixed3.move(self.btAceptarCTS, 145, 0)
		self.btEliminarConTS.set_visible(True)
		self.fixed3.move(self.btEliminarConTS, 255, 0)

		tv = self.tvContactosProfesionales
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idrcts = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleContacTs = "SELECT * FROM REGIMEN_CONTACTOS_TS WHERE IdRCTs = \'" + idrcts + "\'"

		try:
			cursor.execute(queryDetalleContacTs)
		except Exception, e:
			raise e

		resultadoDetalleContacTs = cursor.fetchone()

		if resultadoDetalleContacTs != None:
			self.tbFamiliar.set_text(resultadoDetalleContacTs[1])

			dateFormat = resultadoDetalleContacTs[2].strftime("%d/%m/%Y") 
			self.tbFechaContTS.set_text(dateFormat)

			self.tbHora.set_text(resultadoDetalleContacTs[3])

			textbuffer = self.tbDetalles.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleContacTs[4]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarConTSClick(self, widget):
		tv = self.tvContactosProfesionales	
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idrcts = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarContacTs = "DELETE FROM REGIMEN_CONTACTOS_TS WHERE IdRCTs = \'" + idrcts + "\'"
		
		try:
			cursor.execute(queryBorrarContacTs)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminado con éxito")
			self.btMsgBoxAceptar.set_label("   Cerrar   ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("   Cerrar   ")

		self.cargartvContacTs()

		cursor.close()

	def contactosTSDelete(self, widget, data=None):
		self.ventanaContactosTS.hide()
		return True

	def btProxCitaSAEClick(self, widget):
		self.ventanaProxCitaSAE.show()
		self.btAceptarCitaSAE.set_label("Aceptar")
		self.fixed4.move(self.btAceptarCitaSAE, 130, 0)
		self.btEliminarCita.set_visible(False)
		self.tbFechaCitaSAE.set_text("")
		textbuffer = self.tbDetallesCitaSAE.get_buffer()
		textbuffer.set_text("")

	def btAceptarCitaSAEClick(self, widget):
		fCita = self.tbFechaCitaSAE.get_text()
		day = datetime.datetime.strptime(fCita, '%d/%m/%Y')
		fechaCita = day.strftime('%Y-%m-%d')
				
		dt = self.tbDetallesCitaSAE.get_buffer()
		det = dt.get_text(*dt.get_bounds())

		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarCitaSAE.get_label() == "Aceptar":
			
			queryObtenerIdSAE = "SELECT SAE.IdSAE FROM SAE WHERE SAE.IdMenor = \'" + idmenor + "\'"

			try:
				cursor.execute(queryObtenerIdSAE)
			except Exception, e:
				raise e
				
			comprobacion2 = cursor.fetchone()

			if comprobacion2 != None:
		
				queryInsertarCitaSAE = "INSERT INTO SAE_CITAS (FechaCita, InformeCita, IdSAE) VALUES (\'" + fechaCita + "\', '" + det + "\', '" + str(comprobacion2[0]) + "\')" 

				try:
					cursor.execute(queryInsertarCitaSAE)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Cita registrada con éxito")
					self.btMsgBoxAceptar.set_label("    Cerrar    ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("    Cerrar    ")

				self.cargartvCitasSAE()
			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Registre primero una oficina del SAE")
				self.btMsgBoxAceptar.set_label("Cerrar")
			
		elif self.btAceptarCitaSAE.get_label() == "Actualizar":
			tv = self.tvRegistroCitas
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idcitasae = model[treeiter][2]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarCitaSAE = "UPDATE SAE_CITAS SET FechaCita = \'" + fechaCita + "\', InformeCita = \'" + det + "\' WHERE IdCita = \'" + idcitasae + "\'"

			try:
				cursor.execute(queryActualizarCitaSAE)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Cita actualizada con éxito")
				self.btMsgBoxAceptar.set_label("    Cerrar    ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("    Cerrar    ")

			self.cargartvCitasSAE()
			
		cursor.close()

	def btDetalleCitaSAEClick(self, widget):
		self.ventanaProxCitaSAE.show()
		self.btAceptarCitaSAE.set_label("Actualizar")
		self.fixed4.move(self.btAceptarCitaSAE, 130, 0)
		self.btEliminarCita.set_visible(True)
		self.fixed4.move(self.btEliminarCita, 235, 0)

		tv = self.tvRegistroCitas
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcitasae = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleCitaSAE = "SELECT * FROM SAE_CITAS WHERE IdCita = \'" + idcitasae + "\'"

		try:
			cursor.execute(queryDetalleCitaSAE)
		except Exception, e:
			raise e

		resultadoDetalleCitaSAE = cursor.fetchone()

		if resultadoDetalleCitaSAE != None:
			
			dateFormat = resultadoDetalleCitaSAE[1].strftime("%d/%m/%Y") 
			self.tbFechaCitaSAE.set_text(dateFormat)

			textbuffer = self.tbDetallesCitaSAE.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleCitaSAE[2]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarCitaClick(self, widget):
		tv = self.tvRegistroCitas
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcitasae = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarCitaSAE = "DELETE FROM SAE_CITAS WHERE IdCita = \'" + idcitasae + "\'"
		
		try:
			cursor.execute(queryBorrarCitaSAE)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("    Cerrar    ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("    Cerrar    ")

		self.cargartvCitasSAE()

		cursor.close()

	def proxCitaSAEDelete(self, widget, data=None):
		self.ventanaProxCitaSAE.hide()
		return True
	
	def btSeleccionarOrientadorClick(self, widget):
		self.ventanaSelecTecnico.show()
		self.btAceptarSelecTecnico.set_label("Seleccionar")
		self.lsTecReg.clear()

		c = conexion.db
		cursor = c.cursor()

		queryOrientador = "SELECT DISTINCT Orientador FROM ORIENTA"

		try:
			cursor.execute(queryOrientador)
		except Exception, e:
			raise e

		orientadores = cursor.fetchall()

		if len(orientadores) > 0:
			for i in range(len(orientadores)):
				self.lsTecReg.append(orientadores[i])
		else:
			self.lsTecReg.append(row=None)

		cursor.close()

	def selecTecnicoDelete(self, widget, data=None):
		self.ventanaSelecTecnico.hide()
		return True

	def btProxCitaOrientaClick(self, widget):
		self.ventanaProxCitaOrienta.show()
		self.btAceptarCitaOrienta.set_label("Aceptar")
		self.fixed5.move(self.btAceptarCitaOrienta, 130, 0)
		self.btEliminarCitaOrienta.set_visible(False)
		self.tbFechaCitaOrienta.set_text("")
		textbuffer = self.tbDetallesCitaOrienta.get_buffer()
		textbuffer.set_text("")

	def btAceptarCitaOrientaClick(self, widget):
		fCita = self.tbFechaCitaOrienta.get_text()
		day = datetime.datetime.strptime(fCita, '%d/%m/%Y')
		fechaCita = day.strftime('%Y-%m-%d')
				
		dt = self.tbDetallesCitaOrienta.get_buffer()
		det = dt.get_text(*dt.get_bounds())

		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarCitaOrienta.get_label() == "Aceptar":
			
			queryObtenerIdOrienta = "SELECT ORIENTA.IdOrienta FROM ORIENTA WHERE ORIENTA.IdMenor = \'" + idmenor + "\'"

			try:
				cursor.execute(queryObtenerIdOrienta)
			except Exception, e:
				raise e
				
			comprobacion2 = cursor.fetchone()

			if comprobacion2 != None:
		
				queryInsertarCitaOrienta = "INSERT INTO ORIENTA_CITAS (FechaCita, Observaciones, IdOrienta) VALUES (\'" + fechaCita + "\', '" + det + "\', '" + str(comprobacion2[0]) + "\')" 

				try:
					cursor.execute(queryInsertarCitaOrienta)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Cita registrada con éxito")
					self.btMsgBoxAceptar.set_label("     Cerrar     ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("     Cerrar     ")

				self.cargartvCitasOrienta()
			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Registre primero una oficina de Andalucía Orienta")
				self.btMsgBoxAceptar.set_label("Cerrar")
			
		elif self.btAceptarCitaOrienta.get_label() == "Actualizar":
			tv = self.tvCitasOrienta	
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idcitaorienta = model[treeiter][2]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarCitaOrienta = "UPDATE ORIENTA_CITAS SET FechaCita = \'" + fechaCita + "\', Observaciones = \'" + det + "\' WHERE IdCitaOrienta = \'" + idcitaorienta + "\'"

			try:
				cursor.execute(queryActualizarCitaOrienta)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Cita actualizada con éxito")
				self.btMsgBoxAceptar.set_label("     Cerrar     ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("     Cerrar     ")

			self.cargartvCitasOrienta()
			
		cursor.close()

	def btDetalleCitaOrientaClick(self, widget):
		self.ventanaProxCitaOrienta.show()
		self.btAceptarCitaOrienta.set_label("Actualizar")
		self.fixed5.move(self.btAceptarCitaOrienta, 130, 0)
		self.btEliminarCitaOrienta.set_visible(True)
		self.fixed5.move(self.btEliminarCitaOrienta, 235, 0)

		tv = self.tvCitasOrienta
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcitaorienta = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleCitaOrienta = "SELECT * FROM ORIENTA_CITAS WHERE IdCitaOrienta = \'" + idcitaorienta + "\'"

		try:
			cursor.execute(queryDetalleCitaOrienta)
		except Exception, e:
			raise e

		resultadoDetalleCitaOrienta = cursor.fetchone()

		if resultadoDetalleCitaOrienta != None:
			
			dateFormat = resultadoDetalleCitaOrienta[1].strftime("%d/%m/%Y") 
			self.tbFechaCitaOrienta.set_text(dateFormat)

			textbuffer = self.tbDetallesCitaOrienta.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleCitaOrienta[2]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def proxCitaOrientaDelete(self, widget, data=None):
		self.ventanaProxCitaOrienta.hide()
		return True

	def btEliminarCitaOrientaClick(self, widget):
		tv = self.tvCitasOrienta
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcitaorienta = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarCitaOrienta = "DELETE FROM ORIENTA_CITAS WHERE IdCitaOrienta = \'" + idcitaorienta + "\'"
		
		try:
			cursor.execute(queryBorrarCitaOrienta)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("     Cerrar     ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("     Cerrar     ")

		self.cargartvCitasOrienta()

		cursor.close()

	def btNuevoAAcogeClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.btAceptarConsultaAcoge.set_label("Aceptar")
		self.fixed6.move(self.btAceptarConsultaAcoge, 140, 0)
		self.btEliminarConsultaAcoge.set_visible(False)
		self.tbServicio.set_text("")
		self.tbTecnico.set_text("")
		self.tbFechaConsulta.set_text("")
		textbuffer = self.tbObserv.get_buffer()
		textbuffer.set_text("")

	def consultaAAcogeDelete(self, widget, data=None):
		self.ventanaNuevoAAcoge.hide()
		return True

	def btSelecTecnicoClick(self, widget):
		self.ventanaSelecTecnico.show()
		self.btAceptarSelecTecnico.set_label(" Seleccionar ")
		self.lsTecReg.clear()

		c = conexion.db
		cursor = c.cursor()

		queryTecnico = "SELECT DISTINCT Tecnico FROM AACOGE"

		try:
			cursor.execute(queryTecnico)
		except Exception, e:
			raise e

		tecnicos = cursor.fetchall()

		if len(tecnicos) > 0:
			for i in range(len(tecnicos)):
				self.lsTecReg.append(tecnicos[i])
		else:
			self.lsTecReg.append(row=None)
			#self.lsTecReg.append(["No hay resultados", ])
			
		cursor.close()


	def btAceptarSelecTecnicoClick(self, widget):
		tecSelec = self.cbxTecReg.get_active_text()
		self.ventanaSelecTecnico.hide()

		if self.btAceptarSelecTecnico.get_label() == "Seleccionar":
			self.tbOrientador.set_text(tecSelec)
		elif self.btAceptarSelecTecnico.get_label() == " Seleccionar ":
			self.tbTecnico.set_text(tecSelec)

	def btAceptarConsultaAcogeClick(self, widget):
		servicio = self.tbServicio.get_text()
		tco = self.tbTecnico.get_text()
		fCons = self.tbFechaConsulta.get_text()
		day = datetime.datetime.strptime(fCons, '%d/%m/%Y')
		fechaConsulta = day.strftime('%Y-%m-%d')
				
		dt = self.tbObserv.get_buffer()
		obs = dt.get_text(*dt.get_bounds())

		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarConsultaAcoge.get_label() == "Aceptar":
			
			queryInsertarConsultaAAcoge = "INSERT INTO AACOGE (ServicioConsultado, Tecnico, FechaConsulta, Observaciones, IdMenor) VALUES (\'" + servicio + "\', '" + tco + "\', '" + fechaConsulta + "\', '" + obs + "\', '" + idmenor + "\')" 

			try:
				cursor.execute(queryInsertarConsultaAAcoge)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Consulta registrada con éxito")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("Fallo en el registro")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")

			self.cargartvConsultasAACoge()
			
		elif self.btAceptarConsultaAcoge.get_label() == "Actualizar":
			tv = self.tvConsultasAAcoge
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idaacoge = model[treeiter][3]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarConsultaAcoge = "UPDATE AACOGE SET ServicioConsultado = \'" + servicio + "\', Tecnico = \'" + tco + "\', FechaConsulta = \'" + fechaConsulta + "\', Observaciones = \'" + obs + "\' WHERE IdAAcoge = \'" + idaacoge + "\'"

			try:
				cursor.execute(queryActualizarConsultaAcoge)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Consulta actualizada con éxito")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")

			self.cargartvConsultasAACoge()
			
		cursor.close()

	def btDetalleConsultaAAcogeClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.btAceptarConsultaAcoge.set_label("Actualizar")
		self.fixed6.move(self.btAceptarConsultaAcoge, 140, 0)
		self.btEliminarConsultaAcoge.set_visible(True)
		self.fixed6.move(self.btEliminarConsultaAcoge, 250, 0)

		tv = self.tvConsultasAAcoge
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idaacoge = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleConsultaAAcoge = "SELECT * FROM AACOGE WHERE IdAAcoge = \'" + idaacoge + "\'"

		try:
			cursor.execute(queryDetalleConsultaAAcoge)
		except Exception, e:
			raise e

		resultadoDetalleConsultaAAcoge = cursor.fetchone()

		if resultadoDetalleConsultaAAcoge != None:
			self.tbServicio.set_text(resultadoDetalleConsultaAAcoge[1])
			self.tbTecnico.set_text(resultadoDetalleConsultaAAcoge[2])
			
			dateFormat = resultadoDetalleConsultaAAcoge[3].strftime("%d/%m/%Y") 
			self.tbFechaConsulta.set_text(dateFormat)

			textbuffer = self.tbObserv.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleConsultaAAcoge[4]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarConsultaAAcogeClick(self, widget):
		tv = self.tvConsultasAAcoge
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idaacoge = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarConsultaAAcoge = "DELETE FROM AACOGE WHERE IdAAcoge = \'" + idaacoge + "\'"
		
		try:
			cursor.execute(queryBorrarConsultaAAcoge)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("      Cerrar      ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("      Cerrar      ")

		self.cargartvConsultasAACoge()

		cursor.close()
		



















	def btNuevoLaboraClick(self, widget):
		self.ventanaCursoLabora.show()

	def cursoLaboraDelete(self, widget, data=None):
		self.ventanaCursoLabora.hide()
		return True

	def btPracticaLaboraClick(self, widget):
		self.ventanaPracticaLabora.show()

	def practicaLaboraDelete(self, widget, data=None):
		self.ventanaPracticaLabora.hide()
		return True

	def btNuevoExtranjClick(self, widget):
		self.ventanaNuevoEmpleoExtranj.show()

	def empresaExtranjDelete(self, widget, data=None):
		self.ventanaNuevoEmpleoExtranj.hide()
		return True

	def btPropExtutClick(self, widget):
		self.ventanaPropExtut.show()

	def propuestaExTutDelete(self, widget, data=None):
		self.ventanaPropExtut.hide()
		return True

	def btReunionExtutClick(self, widget):
		self.ventanaReunionesExtut.show()

	def reunionesExTutDelete(self, widget, data=None):
		self.ventanaReunionesExtut.hide()
		return True

	def empresaExTutClick(self, widget):
		self.ventanaEmpresaExTut.show()

	def empresaExTutDelete(self, widget, data=None):
		self.ventanaEmpresaExTut.hide()
		return True

	def btMsgBoxAceptarClick (self, widget):
		if self.btMsgBoxAceptar.get_label() == "Cerrar":
			self.msgbox.hide()
		elif self.btMsgBoxAceptar.get_label() == " Cerrar ":
			self.msgbox.hide()
			self.ventanaUC.hide()
		elif self.btMsgBoxAceptar.get_label() == "  Cerrar  ":
			self.msgbox.hide()
			self.ventanaContacFam.hide()
		elif self.btMsgBoxAceptar.get_label() == "   Cerrar   ":
			self.msgbox.hide()
			self.ventanaContactosTS.hide()
		elif self.btMsgBoxAceptar.get_label() == "    Cerrar    ":
			self.msgbox.hide()
			self.ventanaProxCitaSAE.hide()
		elif self.btMsgBoxAceptar.get_label() == "     Cerrar     ":
			self.msgbox.hide()
			self.ventanaProxCitaOrienta.hide()
		elif self.btMsgBoxAceptar.get_label() == "      Cerrar      ":
			self.msgbox.hide()
			self.ventanaNuevoAAcoge.hide()


		