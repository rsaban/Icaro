#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
import datetime
import fichaMenor

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
		self.ficha = builder.get_object("ficha")
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
		#CentroEducativo
		self.cbxNEE = builder.get_object("cbxNEE")
		self.cbxTipoNEE = builder.get_object("cbxTipoNEE")
		self.tbObservColegio = builder.get_object("tbObservColegio")
		self.tbCentroEducativo = builder.get_object("tbCentroEducativo")
		self.tbCurso = builder.get_object("tbCurso")
		self.tbCodCentEducativo = builder.get_object("tbCodCentEducativo")
		self.tvIncidencias = builder.get_object("tvIncidencias")
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

		#centroEducativo
		self.centroEducativo = builder.get_object("centroEducativo")
		self.tbNombreCE = builder.get_object("tbNombreCE")
		self.tbDireccionCE = builder.get_object("tbDireccionCE")
		self.tbTlfnoCE = builder.get_object("tbTlfnoCE")
		self.tbMailCE = builder.get_object("tbMailCE")
		self.btAceptarCE = builder.get_object("btAceptarCE")
		self.btEliminarCE = builder.get_object("btEliminarCE")
		self.fixed13 = builder.get_object("fixed13")

		#selecCentroEducativo	
		self.ventanaSelecCentroEducativo = builder.get_object("selecCentroEducativo")
		self.cbxCentroEducativo = builder.get_object("cbxCentroEducativo")
		self.btNuevoCE = builder.get_object("btNuevoCE")
		self.btAceptarSelecCentro = builder.get_object("btAceptarSelecCentro")

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
		self.btAceptarCurso = builder.get_object("btAceptarCurso")
		self.btEliminarCurso = builder.get_object("btEliminarCurso")
		self.fixed7 = builder.get_object("fixed7")	
	
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
		self.btAceptarPractica = builder.get_object("btAceptarPractica")
		self.btEliminarPractica = builder.get_object("btEliminarPractica")
		self.fixed8 = builder.get_object("fixed8")

		#empresaExtranj
		self.ventanaNuevoEmpleoExtranj = builder.get_object("empresaExtranj")
		self.tbEmpresa = builder.get_object("tbEmpresa")
		self.tbFechaInicioEmpresa = builder.get_object("tbFechaInicioEmpresa")
		self.tbDuracion = builder.get_object("tbDuracion")
		self.btAceptarEmpresaExtranj = builder.get_object("btAceptarEmpresaExtranj")
		self.btEliminarEmpresaExtranj = builder.get_object("btEliminarEmpresaExtranj")
		self.fixed9 = builder.get_object("fixed9")
	
		#propuestaExTut
		self.ventanaPropExtut = builder.get_object("propuestaExTut")
		self.cbxEntidadExtut = builder.get_object("cbxEntidadExtut")
		self.tbFechaEntidad = builder.get_object("tbFechaEntidad")
		self.btAceptarPropuesta = builder.get_object("btAceptarPropuesta")
		self.btEliminarPropuesta = builder.get_object("btEliminarPropuesta")
		self.fixed11 = builder.get_object("fixed11")

		#reunionesExtut
		self.ventanaReunionesExtut = builder.get_object("reunionesExTut")
		self.cbxEntidadReunion = builder.get_object("cbxEntidadReunion")
		self.cbxTipoReunion = builder.get_object("cbxTipoReunion")
		self.tbFechaReunion = builder.get_object("tbFechaReunion")
		self.tbAcuerdosReunion = builder.get_object("tbAcuerdosReunion")
		self.btAceptarReunion = builder.get_object("btAceptarReunion")
		self.btEliminarReunion = builder.get_object("btEliminarReunion")
		self.fixed12 = builder.get_object("fixed12")

		#empresaExtut
		self.ventanaEmpresaExTut = builder.get_object("empresaExTut")
		self.tbEntidad = builder.get_object("tbEntidad")
		self.tbDireccionEntidad = builder.get_object("tbDireccionEntidad")
		self.tbTelefonoEntidad = builder.get_object("tbTelefonoEntidad")
		self.tbMailEntidad = builder.get_object("tbMailEntidad")
		self.btAceptarEntidadExtut = builder.get_object("btAceptarEntidadExtut")
		self.btEliminarEntidadExtut = builder.get_object("btEliminarEntidadExtut")
		self.fixed10 = builder.get_object("fixed10")
		self.tbIdEntidadExtut = builder.get_object("tbIdEntidadExtut")

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
		self.lstvCursosLabora = builder.get_object("lstvCursosLabora")
		self.lstvPracticasLabora = builder.get_object("lstvPracticasLabora")
		self.lstvCRoja = builder.get_object("lstvCRoja")
		self.lstvSGIT = builder.get_object("lstvSGIT")
		self.lstvExtranjeria = builder.get_object("lstvExtranjeria")
		self.lsEntidadExtut = builder.get_object("lsEntidadExtut")
		self.lstvPropExtut = builder.get_object("lstvPropExtut")
		self.lsTipoReunionExtut = builder.get_object("lsTipoReunionExtut")
		self.lstvReunionesExtut = builder.get_object("lstvReunionesExtut")
		self.lsTipoNEE = builder.get_object("lsTipoNEE")
		self.lsCentrosEducativos = builder.get_object("lsCentrosEducativos")

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

		dict = {"on_btFicha_clicked": self.btFichaClick,
				"on_ficha_delete_event": self.fichaDelete,
				"on_btAceptar_clicked":self.btAceptarClick,
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
				"on_btEliminarConsultaAcoge_clicked": self.btEliminarConsultaAAcogeClick,
				"on_btSelecOrientaLabora_clicked": self.btSelecOrientaLaboraClick,
				"on_btAceptarCurso_clicked": self.btAceptarCursoClick,
				"on_btDetalleCursoLabora_clicked": self.btDetalleCursoLaboraClick,
				"on_btEliminarCurso_clicked": self.btEliminarCursoClick,
				"on_btAceptarPractica_clicked": self.btAceptarPracticaClick,
				"on_btDetallePracticaLabora_clicked": self.btDetallePracticaClick,
				"on_btEliminarPractica_clicked": self.btEliminarPracticaClick,
				"on_btConsultaCRoja_clicked": self.btConsultaCRojaClick,
				"on_btDetalleCRoja_clicked": self.btDetalleCRojaClick,
				"on_btConsultaSGIT_clicked": self.btConsultasSGITClick,
				"on_btDetalleConsultaSGIT_clicked": self.btDetalleSGITClick,
				"on_btAceptarEmpresaExtranj_clicked": self.btAceptarEmpresaExtranjClick,
				"on_btDetalleEmpleo_clicked": self.btDetalleEmpleoClick,
				"on_btEliminarEmpresaExtranj_clicked": self.btEliminarEmpresaExtranjClick,
				"on_btAceptarEntidadExtut_clicked": self.btAceptarEntidadExtutClick,
				"on_btAceptarPropuesta_clicked": self.btAceptarPropuestaClick,
				"on_btDetallePropuesta_clicked": self.btDetallePropuestaClick,
				"on_btEliminarPropuesta_clicked": self.btEliminarPropuestaClick,
				"on_btAceptarReunion_clicked": self.btAceptarReunionExtutClick,
				"on_btDetalleReunion_clicked": self.btDetalleReunionClick,
				"on_btEliminarReunion_clicked": self.btEliminarReunionClick,
				"on_btDetalleEmpresa_clicked": self.btDetalleEmpresaClick,
				"on_btDetalleEmpresa2_clicked": self.btDetalleEmpresa2Click,
				"on_btEliminarEntidadExtut_clicked": self.btEliminarEntidadExtutClick,
				"on_btSelecCentro_clicked": self.btSelecCentroClick,
				"on_btNuevoCE_clicked": self.btNuevoCEClick,
				"on_btAceptarSelecCentro_clicked": self.btAceptarSelecCentroClick,
				"on_centroEducativo_delete_event": self.centroEducativoDelete,
				"on_selecCentroEducativo_delete_event": self.selecCentroEducativoDelete,
				"on_btAceptarCE_clicked": self.btAceptarCEClick,
				"on_btEliminarCE_clicked": self.btEliminarCEClick,
				"on_btDetalleCentro_clicked": self.btDetalleCentroClick
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
		
		queryCargarDatos6 = "SELECT SUBAREA_EDUCATIVA_TS.Curso, SUBAREA_EDUCATIVA_TS.NEE, SUBAREA_EDUCATIVA_TS.TipoNEE, SUBAREA_EDUCATIVA_TS.Observaciones, SUBAREA_EDUCATIVA_TS.IdCE FROM SUBAREA_EDUCATIVA_TS, AREA_SOCIAL WHERE AREA_SOCIAL.IdSocial = SUBAREA_EDUCATIVA_TS.IdSocial AND AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

		try:
			cursor.execute(queryCargarDatos6)
		except Exception, e:
			raise e

		consultado6 = cursor.fetchone()

		if consultado6 != None:
			self.tbCurso.set_text(consultado6[0])
			for posicion, elemento in enumerate(self.lsPHC):
				f = elemento[0]
				if f == consultado6[1]:
					self.cbxNEE.set_active(posicion)

			for posicion, elemento in enumerate(self.lsTipoNEE):
				f = elemento[0]
				if f == consultado6[2]:
					self.cbxTipoNEE.set_active(posicion)

			textbuffer = self.tbObservColegio.get_buffer()
			textbuffer.set_text(consultado6[3])

			self.tbCodCentEducativo.set_text(str(consultado6[4]))

			queryConsultarCE = "SELECT NombreCE FROM CENTRO_EDUCATIVO WHERE IdCE = \'" + str(consultado6[4]) + "\'"

			try:
				cursor.execute(queryConsultarCE)
			except Exception, e:
				raise e
			centroObtenido = cursor.fetchone()

			if len(centroObtenido) > 0:
				self.tbCentroEducativo.set_text(centroObtenido[0])

		else:
			pass			

		#ahora voy a cargar los treeviews
		self.cargartvFamiliares()
		self.cargartvContacFam()
		self.cargartvContacTs()
		self.cargartvCitasSAE()
		self.cargartvCitasOrienta()
		self.cargartvConsultasAACoge()
		self.cargartvCursosLabora()
		self.cargartvPracticasLabora()
		self.cargartvConsultasCRoja()
		self.cargartvConsultasSGIT()
		self.cargartvExtranjeria()
		self.cargartvPropuestasExtut()
		self.cargartvReunionesExtut()

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

	def cargartvCursosLabora(self):
		self.lstvCursosLabora.clear()

		c = conexion.db
		cursor = c.cursor()

		queryObtenerIdLabora = "SELECT IdLabora FROM LABORA WHERE IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryObtenerIdLabora)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		comprobacion = cursor.fetchone()
			
		
		if comprobacion != None:
			querytvConsultasCursosLabora = "SELECT LABORA_CURSOS.CursoRealizado, LABORA_CURSOS.FechaInicioCurso, LABORA_CURSOS.Estado, LABORA_CURSOS.IdCurso FROM LABORA, LABORA_CURSOS WHERE LABORA.IdMenor = \'" + idmenor + "\' AND LABORA.IdLabora = \'" + str(comprobacion[0]) + "\' AND LABORA.IdLabora = LABORA_CURSOS.IdLabora ORDER BY LABORA_CURSOS.FechaInicioCurso DESC"

			try:
				cursor.execute(querytvConsultasCursosLabora)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvCursosLabora.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def cargartvPracticasLabora(self):
		self.lstvPracticasLabora.clear()

		c = conexion.db
		cursor = c.cursor()

		queryObtenerIdLabora = "SELECT IdLabora FROM LABORA WHERE IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryObtenerIdLabora)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		comprobacion = cursor.fetchone()
			
		
		if comprobacion != None:
			querytvConsultarPracticaLabora = "SELECT LABORA_PRACTICAS.FechaInicio, LABORA_PRACTICAS.Empresa, LABORA_PRACTICAS.IdPractica FROM LABORA, LABORA_PRACTICAS WHERE LABORA.IdMenor = \'" + idmenor + "\' AND LABORA.IdLabora = \'" + str(comprobacion[0]) + "\' AND LABORA.IdLabora = LABORA_PRACTICAS.IdLabora ORDER BY LABORA_PRACTICAS.FechaInicio DESC"

			try:
				cursor.execute(querytvConsultarPracticaLabora)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvPracticasLabora.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def cargartvConsultasCRoja(self):
		self.lstvCRoja.clear()

		c = conexion.db
		cursor = c.cursor()
		
		querytvConsultasCRoja = "SELECT ServicioConsultado, Tecnico, FechaConsulta, IdCruzRoja FROM CRUZ_ROJA WHERE IdMenor = \'" + idmenor + "\' ORDER BY FechaConsulta DESC"

		try:
			cursor.execute(querytvConsultasCRoja)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lstvCRoja.append(resultado[i])
		

		cursor.close()	

	def cargartvConsultasSGIT(self):
		self.lstvSGIT.clear()

		c = conexion.db
		cursor = c.cursor()
		
		querytvConsultasSGIT = "SELECT ServicioConsultado, Tecnico, FechaConsulta, IdSGit FROM SGIT WHERE IdMenor = \'" + idmenor + "\' ORDER BY FechaConsulta DESC"

		try:
			cursor.execute(querytvConsultasSGIT)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lstvSGIT.append(resultado[i])
		

		cursor.close()	

	def cargartvExtranjeria(self):
		self.lstvExtranjeria.clear()

		c = conexion.db
		cursor = c.cursor()
		
		queryObtenerIdExtranjeria = "SELECT IdExtranjeria FROM EXTRANJERIA WHERE IdMenor = \'" + idmenor + "\'"

		try:
			cursor.execute(queryObtenerIdExtranjeria)
		except Exception, e:
			raise e
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		comprobacion = cursor.fetchone()
			
		
		if comprobacion != None:
			querytvEmpleoExtranjeria= "SELECT EXTRANJERIA_EMPRESA.NombreEEmpresa, EXTRANJERIA_EMPRESA.FechaInicio, EXTRANJERIA_EMPRESA.IdEEmpresa FROM EXTRANJERIA, EXTRANJERIA_EMPRESA WHERE EXTRANJERIA.IdMenor = \'" + idmenor + "\' AND EXTRANJERIA.IdExtranjeria = \'" + str(comprobacion[0]) + "\' AND EXTRANJERIA.IdExtranjeria = EXTRANJERIA_EMPRESA.IdExtranjeria ORDER BY EXTRANJERIA_EMPRESA.FechaInicio DESC"

			try:
				cursor.execute(querytvEmpleoExtranjeria)
			except Exception, e:
				raise e

			resultado = cursor.fetchall()

			if len(resultado) != 0:
				for i in range(len(resultado)):
					self.lstvExtranjeria.append(resultado[i])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("Fallo al recuperar los datos")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()	

	def cargartvPropuestasExtut(self):
		self.lstvPropExtut.clear()

		c = conexion.db
		cursor = c.cursor()
		
		querytvPropuestas = "SELECT EXTUT_ENTIDADES.Nombre, EXTUT_PROPUESTAS.FechaPropuesta, EXTUT_PROPUESTAS.IdProp FROM EXTUT, EXTUT_ENTIDADES, EXTUT_PROPUESTAS  WHERE EXTUT.IdMenor = \'" + idmenor + "\' AND EXTUT.IdExtut = EXTUT_PROPUESTAS.IdExtut AND EXTUT.IdExTEntidad = EXTUT_ENTIDADES.IdExTEntidad ORDER BY EXTUT_PROPUESTAS.FechaPropuesta DESC"

		try:
			cursor.execute(querytvPropuestas)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lstvPropExtut.append(resultado[i])
		

		cursor.close()	

	def cargartvReunionesExtut(self):
		self.lstvReunionesExtut.clear()

		c = conexion.db
		cursor = c.cursor()
		
		querytvReuniones = "SELECT EXTUT_ENTIDADES.Nombre, EXTUT_REUNIONES.FechaReunion, EXTUT_REUNIONES.TipoReunion, EXTUT_REUNIONES.IdReunion FROM EXTUT, EXTUT_ENTIDADES, EXTUT_REUNIONES  WHERE EXTUT.IdMenor = \'" + idmenor + "\' AND EXTUT.IdExtut = EXTUT_REUNIONES.IdExtut AND EXTUT.IdExTEntidad = EXTUT_ENTIDADES.IdExTEntidad ORDER BY EXTUT_REUNIONES.FechaReunion DESC"

		try:
			cursor.execute(querytvReuniones)
		except Exception, e:
			raise e

		resultado = cursor.fetchall()

		if len(resultado) != 0:
			for i in range(len(resultado)):
				self.lstvReunionesExtut.append(resultado[i])
		

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
			curso_colegio = self.tbCurso.get_text()
			ne = self.cbxNEE.get_active_text()
			tipo_ne = self.cbxTipoNEE.get_active_text()
			obs_ne = self.tbObservColegio.get_buffer()
			obsne = obs_ne.get_text(*obs_ne.get_bounds())
			centroEd = self.tbCodCentEducativo.get_text()

			queryComprobarRegistro = "SELECT SUBAREA_EDUCATIVA_TS.IdSubEduc FROM SUBAREA_EDUCATIVA_TS, AREA_SOCIAL WHERE AREA_SOCIAL.IdSocial = SUBAREA_EDUCATIVA_TS.IdSocial AND AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

			c = conexion.db
			cursor = c.cursor()

			try:
				cursor.execute(queryComprobarRegistro)
			except Exception, e:
				raise e

			comprobacion = cursor.fetchone()

			if comprobacion != None:
				queryActualizarNEE = "UPDATE SUBAREA_EDUCATIVA_TS SET Curso = \'" + curso_colegio + "', NEE = \'" + ne + "\', TipoNEE = \'" + tipo_ne  + "\', Observaciones = \'" + obsne + "\', IdCE = \'" + centroEd + "\' WHERE IdSubEduc = \'" + str(comprobacion[0]) + "\'"

				try:
					cursor.execute(queryActualizarNEE)
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
				queryObtenerIdSocial = "SELECT AREA_SOCIAL.IdSocial FROM AREA_SOCIAL WHERE AREA_SOCIAL.IdExpdte = \'" + self.lbMostrarExpdte.get_text() + "\'"

				try:
					cursor.execute(queryObtenerIdSocial)
				except Exception, e:
					raise e

				idsoc = cursor.fetchone()

				queryInsertarNEE = "INSERT INTO SUBAREA_EDUCATIVA_TS (Curso, NEE, TipoNEE, Observaciones, IdCE, IdSocial) VALUES (\'" + curso_colegio + "\', '" + ne + "\', '" + tipo_ne + "\', '" + obsne + "\', '" + centroEd + "\', '" + str(idsoc[0]) + "\')"

				try:
					cursor.execute(queryInsertarNEE)
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

		elif paginaActual == 8:	
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
		
		elif paginaActual == 9:
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

		elif paginaActual == 10:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 11:
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

		elif paginaActual == 12:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 13:
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

		elif paginaActual == 14:
			self.msgbox.show()
			self.lbMsgBox.set_text("Esta pestaña no es actualizable mediante este botón.")
			self.btMsgBoxAceptar.set_label("Cerrar")

		elif paginaActual == 15:
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
		self.ventanaNuevoAAcoge.set_title("Andalucía Acoge")
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
		
		if self.ventanaNuevoAAcoge.get_title() == "Andalucía Acoge":
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

		elif self.ventanaNuevoAAcoge.get_title() == "Cruz Roja":
			self.ventanaSelecTecnico.show()
			self.btAceptarSelecTecnico.set_label("   Seleccionar   ")
			self.lsTecReg.clear()

			c = conexion.db
			cursor = c.cursor()

			queryTecnico = "SELECT DISTINCT Tecnico FROM CRUZ_ROJA"

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
								
			cursor.close()

	def btAceptarSelecTecnicoClick(self, widget):
		tecSelec = self.cbxTecReg.get_active_text()
		self.ventanaSelecTecnico.hide()

		if self.btAceptarSelecTecnico.get_label() == "Seleccionar":
			self.tbOrientador.set_text(tecSelec)
		elif self.btAceptarSelecTecnico.get_label() == " Seleccionar ":
			self.tbTecnico.set_text(tecSelec)
		elif self.btAceptarSelecTecnico.get_label() == "  Seleccionar  ":
			self.tbOrientadorLabora.set_text(tecSelec)
		elif self.btAceptarSelecTecnico.get_label() == "   Seleccionar   ":
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

		if self.ventanaNuevoAAcoge.get_title() == "Andalucía Acoge":
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
		
		elif self.ventanaNuevoAAcoge.get_title() == "Cruz Roja":
			if self.btAceptarConsultaAcoge.get_label() == "Aceptar":
				
				queryInsertarConsultaCRoja = "INSERT INTO CRUZ_ROJA (ServicioConsultado, Tecnico, FechaConsulta, Observaciones, IdMenor) VALUES (\'" + servicio + "\', '" + tco + "\', '" + fechaConsulta + "\', '" + obs + "\', '" + idmenor + "\')" 

				try:
					cursor.execute(queryInsertarConsultaCRoja)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Consulta registrada con éxito")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")

				self.cargartvConsultasCRoja()
				
			elif self.btAceptarConsultaAcoge.get_label() == "Actualizar":
				tv = self.tvConsultasCRoja
				selection = tv.get_selection()
				model, treeiter = selection.get_selected()
				if treeiter != None:
					idcroja = model[treeiter][3]
				
				c = conexion.db
				cursor = c.cursor()
			
				queryActualizarConsultaCRoja = "UPDATE CRUZ_ROJA SET ServicioConsultado = \'" + servicio + "\', Tecnico = \'" + tco + "\', FechaConsulta = \'" + fechaConsulta + "\', Observaciones = \'" + obs + "\' WHERE IdCruzRoja = \'" + idcroja + "\'"

				try:
					cursor.execute(queryActualizarConsultaCRoja)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Consulta actualizada con éxito")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("La actualización ha fallado")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")

				self.cargartvConsultasCRoja()

		elif self.ventanaNuevoAAcoge.get_title() == "Secretariado Gitano":
			if self.btAceptarConsultaAcoge.get_label() == "Aceptar":
				
				queryInsertarConsultaSGIT = "INSERT INTO SGIT (ServicioConsultado, Tecnico, FechaConsulta, Observaciones, IdMenor) VALUES (\'" + servicio + "\', '" + tco + "\', '" + fechaConsulta + "\', '" + obs + "\', '" + idmenor + "\')" 

				try:
					cursor.execute(queryInsertarConsultaSGIT)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Consulta registrada con éxito")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")

				self.cargartvConsultasSGIT()
				
			elif self.btAceptarConsultaAcoge.get_label() == "Actualizar":
				tv = self.tvConsultasSGIT
				selection = tv.get_selection()
				model, treeiter = selection.get_selected()
				if treeiter != None:
					idsgit = model[treeiter][3]
				
				c = conexion.db
				cursor = c.cursor()
			
				queryActualizarConsultaSGIT = "UPDATE SGIT SET ServicioConsultado = \'" + servicio + "\', Tecnico = \'" + tco + "\', FechaConsulta = \'" + fechaConsulta + "\', Observaciones = \'" + obs + "\' WHERE IdSGit = \'" + idsgit + "\'"

				try:
					cursor.execute(queryActualizarConsultaSGIT)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Consulta actualizada con éxito")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("La actualización ha fallado")
					self.btMsgBoxAceptar.set_label("      Cerrar      ")

				self.cargartvConsultasSGIT()




		cursor.close()

	def btDetalleConsultaAAcogeClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.ventanaNuevoAAcoge.set_title("Andalucía Acoge")
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
		c = conexion.db
		cursor = c.cursor()

		if self.ventanaNuevoAAcoge.get_title() == "Andalucía Acoge":
			tv = self.tvConsultasAAcoge
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idaacoge = model[treeiter][3]
							
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

		elif self.ventanaNuevoAAcoge.get_title() == "Cruz Roja":
			tv = self.tvConsultasCRoja
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idcroja = model[treeiter][3]
							
			queryBorrarConsultaCRoja = "DELETE FROM CRUZ_ROJA WHERE IdCruzRoja = \'" + idcroja + "\'"
			
			try:
				cursor.execute(queryBorrarConsultaCRoja)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Eliminada con éxito")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La eliminación ha fallado")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")

			self.cargartvConsultasCRoja()

		elif self.ventanaNuevoAAcoge.get_title() == "Secretariado Gitano":
			tv = self.tvConsultasSGIT
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idsgit = model[treeiter][3]
							
			queryBorrarConsultaSGIT = "DELETE FROM SGIT WHERE IdSGit = \'" + idsgit + "\'"
			
			try:
				cursor.execute(queryBorrarConsultaSGIT)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Eliminada con éxito")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La eliminación ha fallado")
				self.btMsgBoxAceptar.set_label("      Cerrar      ")

			self.cargartvConsultasSGIT()

		cursor.close()
		
	def btSelecOrientaLaboraClick(self, widget):
		self.ventanaSelecTecnico.show()
		self.btAceptarSelecTecnico.set_label("  Seleccionar  ")
		self.lsTecReg.clear()

		c = conexion.db
		cursor = c.cursor()

		queryOrientadorLabora = "SELECT DISTINCT OrientadorLabora FROM LABORA"

		try:
			cursor.execute(queryOrientadorLabora)
		except Exception, e:
			raise e

		orientadoresLabora = cursor.fetchall()

		if len(orientadoresLabora) > 0:
			for i in range(len(orientadoresLabora)):
				self.lsTecReg.append(orientadoresLabora[i])
		else:
			self.lsTecReg.append(row=None)
			
			
		cursor.close()

	def btNuevoLaboraClick(self, widget):
		self.ventanaCursoLabora.show()
		self.btAceptarCurso.set_label("Aceptar")
		self.fixed7.move(self.btAceptarCurso, 170, 0)
		self.btEliminarCurso.set_visible(False)
		self.tbTitulo.set_text("")
		self.tbFechaInicio.set_text("")
		textbuffer = self.tbObjetivos.get_buffer()
		textbuffer.set_text("")
		self.cbxEstado.set_active(0)

	def btAceptarCursoClick(self, widget):
		titulo = self.tbTitulo.get_text()

		fICurso = self.tbFechaInicio.get_text()
		day = datetime.datetime.strptime(fICurso, '%d/%m/%Y')
		fechaICurso = day.strftime('%Y-%m-%d')
				
		obj = self.tbObjetivos.get_buffer()
		objetivos = obj.get_text(*obj.get_bounds())
		
		estado = self.cbxEstado.get_active_text()


		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarCurso.get_label() == "Aceptar":
			
			queryObtenerIdLabora = "SELECT IdLabora FROM LABORA WHERE IdMenor = \'" + idmenor + "\'"

			try:
				cursor.execute(queryObtenerIdLabora)
			except Exception, e:
				raise e
				
			comprobacion = cursor.fetchone()

			if comprobacion != None:
		
				queryInsertarCursoLabora = "INSERT INTO LABORA_CURSOS (CursoRealizado, FechaInicioCurso, ObjetivosCurso, Estado, IdLabora) VALUES (\'" + titulo + "\', '" + fechaICurso + "\', '" + objetivos + "\', '" + estado + "\', '" + str(comprobacion[0]) + "\')" 

				try:
					cursor.execute(queryInsertarCursoLabora)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Curso registrado con éxito")
					self.btMsgBoxAceptar.set_label("       Cerrar       ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("       Cerrar       ")

				self.cargartvCursosLabora()
			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Registre primero un orientador de referencia")
				self.btMsgBoxAceptar.set_label("Cerrar")
			
		elif self.btAceptarCurso.get_label() == "Actualizar":
			tv = self.tvCursosLabora
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idcursolabora = model[treeiter][3]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarCursoLabora = "UPDATE LABORA_CURSOS SET CursoRealizado = \'" + titulo + "\', FechaInicioCurso = \'" + fechaICurso + "\', ObjetivosCurso = \'" + objetivos + "\', Estado = \'" + estado + "\' WHERE IdCurso = \'" + idcursolabora + "\'"

			try:
				cursor.execute(queryActualizarCursoLabora)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Curso actualizado con éxito")
				self.btMsgBoxAceptar.set_label("       Cerrar       ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("       Cerrar       ")

			self.cargartvCursosLabora()
			
		cursor.close()

	def btDetalleCursoLaboraClick(self, widget):
		self.ventanaCursoLabora.show()
		self.btAceptarCurso.set_label("Actualizar")
		self.fixed7.move(self.btAceptarCurso, 130, 0)
		self.btEliminarCurso.set_visible(True)
		self.fixed7.move(self.btEliminarCurso, 235, 0)

		tv = self.tvCursosLabora
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcursolabora = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleCursoLabora = "SELECT * FROM LABORA_CURSOS WHERE IdCurso = \'" + idcursolabora + "\'"

		try:
			cursor.execute(queryDetalleCursoLabora)
		except Exception, e:
			raise e

		resultadoDetalleCursoLabora = cursor.fetchone()

		if resultadoDetalleCursoLabora != None:
			self.tbTitulo.set_text(resultadoDetalleCursoLabora[1])

			dateFormat = resultadoDetalleCursoLabora[2].strftime("%d/%m/%Y") 
			self.tbFechaInicio.set_text(dateFormat)

			textbuffer = self.tbObjetivos.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleCursoLabora[3]))

 		 	for posicion, elemento in enumerate(self.lsCursoLabora):
 		 		f = elemento[0]
 		 		if f == str(resultadoDetalleCursoLabora[4]):
 		 			self.cbxEstado.set_active(posicion)
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarCursoClick(self, widget):
		tv = self.tvCursosLabora
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcursolabora = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarCursoLabora = "DELETE FROM LABORA_CURSOS WHERE IdCurso = \'" + idcursolabora + "\'"
		
		try:
			cursor.execute(queryBorrarCursoLabora)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("       Cerrar       ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("       Cerrar       ")

		self.cargartvCursosLabora()

		cursor.close()

	def cursoLaboraDelete(self, widget, data=None):
		self.ventanaCursoLabora.hide()
		return True

	def btPracticaLaboraClick(self, widget):
		self.ventanaPracticaLabora.show()
		self.btAceptarPractica.set_label("Aceptar")
		self.fixed8.move(self.btAceptarPractica, 160, 0)
		self.btEliminarPractica.set_visible(False)
		self.tbInicioPractica.set_text("")
		self.tbFinPractica.set_text("")
		self.tbEmpresaPractica.set_text("")
		self.tbDireccionEmpresaPractica.set_text("")
		self.tbTelefonoEmpresaPractica.set_text("")
		self.tbMailEmpresaPractica.set_text("")
		self.tbContactoEmpresaPractica.set_text("")
		self.cbxContrato.set_active(0)

	def btAceptarPracticaClick(self, widget):
		fIP = self.tbInicioPractica.get_text()
		day = datetime.datetime.strptime(fIP, '%d/%m/%Y')
		fechaIPractica = day.strftime('%Y-%m-%d')

		fFP = self.tbFinPractica.get_text()
		day2 = datetime.datetime.strptime(fFP, '%d/%m/%Y')
		fechaFPractica = day2.strftime('%Y-%m-%d')

		empresa = self.tbEmpresaPractica.get_text()
		dirEmpresa = self.tbDireccionEmpresaPractica.get_text()
		tlfEmpresa = str(self.tbTelefonoEmpresaPractica.get_text())
		mailEmpresa = self.tbMailEmpresaPractica.get_text()
		contacEmpresa = self.tbContactoEmpresaPractica.get_text()
		contrato = self.cbxContrato.get_active_text()


		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarPractica.get_label() == "Aceptar":
			
			queryObtenerIdLabora = "SELECT IdLabora FROM LABORA WHERE IdMenor = \'" + idmenor + "\'"

			try:
				cursor.execute(queryObtenerIdLabora)
			except Exception, e:
				raise e
				
			comprobacion = cursor.fetchone()

			if comprobacion != None:
		
				queryInsertarPracticaLabora = "INSERT INTO LABORA_PRACTICAS (FechaInicio, FechaFin, Empresa, DireccionEmpresa, TelefonoEmpresa, ContactoEmpresa, ContratoTrabajo, MailEmpresa, IdLabora) VALUES (\'" + fechaIPractica + "\', '" + fechaFPractica + "\', '" + empresa + "\', '" + dirEmpresa + "\', '" + tlfEmpresa + "\', '" + contacEmpresa + "\', '" + contrato + "\', '" + mailEmpresa + "\', '" + str(comprobacion[0]) + "\')" 

				try:
					cursor.execute(queryInsertarPracticaLabora)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Práctica registrado con éxito")
					self.btMsgBoxAceptar.set_label("        Cerrar        ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("        Cerrar        ")

				self.cargartvPracticasLabora()
			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Registre primero un orientador de referencia")
				self.btMsgBoxAceptar.set_label("Cerrar")
			
		elif self.btAceptarPractica.get_label() == "Actualizar":
			tv = self.tvPracticasLabora
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idpracticalabora = model[treeiter][2]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarPracticaLabora = "UPDATE LABORA_PRACTICAS SET FechaInicio = \'" + fechaIPractica + "\', FechaFin = \'" + fechaFPractica + "\', Empresa = \'" + empresa + "\', DireccionEmpresa = \'" + dirEmpresa + "\', TelefonoEmpresa = \'" + tlfEmpresa + "\', ContactoEmpresa = \'" + contacEmpresa + "\', ContratoTrabajo = \'" + contrato + "\', MailEmpresa = \'" + mailEmpresa + "\' WHERE IdPractica = \'" + idpracticalabora + "\'"

			try:
				cursor.execute(queryActualizarPracticaLabora)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Práctica actualizada con éxito")
				self.btMsgBoxAceptar.set_label("        Cerrar        ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("        Cerrar        ")

			self.cargartvPracticasLabora()
			
		cursor.close()

	def btDetallePracticaClick(self, widget):
		self.ventanaPracticaLabora.show()
		self.btAceptarPractica.set_label("Actualizar")
		self.fixed8.move(self.btAceptarPractica, 130, 0)
		self.btEliminarPractica.set_visible(True)
		self.fixed8.move(self.btEliminarPractica, 235, 0)

		tv = self.tvPracticasLabora
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idpracticalabora = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetallePracticaLabora = "SELECT * FROM LABORA_PRACTICAS WHERE IdPractica = \'" + idpracticalabora + "\'"

		try:
			cursor.execute(queryDetallePracticaLabora)
		except Exception, e:
			raise e

		resultadoDetallePracticaLabora = cursor.fetchone()

		if resultadoDetallePracticaLabora != None:
			dateFormat = resultadoDetallePracticaLabora[1].strftime("%d/%m/%Y") 
			self.tbInicioPractica.set_text(dateFormat)

			dateFormat2 = resultadoDetallePracticaLabora[2].strftime("%d/%m/%Y") 
			self.tbFinPractica.set_text(dateFormat2)

			self.tbEmpresaPractica.set_text(resultadoDetallePracticaLabora[3])
			self.tbDireccionEmpresaPractica.set_text(resultadoDetallePracticaLabora[4])
			self.tbTelefonoEmpresaPractica.set_text(str(resultadoDetallePracticaLabora[5]))
			self.tbMailEmpresaPractica.set_text(resultadoDetallePracticaLabora[8])
			self.tbContactoEmpresaPractica.set_text(resultadoDetallePracticaLabora[6])
			self.cbxContrato.set_active(0)

 		 	for posicion, elemento in enumerate(self.lsPHC):
 		 		f = elemento[0]
 		 		if f == str(resultadoDetallePracticaLabora[7]):
 		 			self.cbxContrato.set_active(posicion)
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarPracticaClick(self, widget):
		tv = self.tvPracticasLabora
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idpracticalabora = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarPracticaLabora = "DELETE FROM LABORA_PRACTICAS WHERE IdPractica = \'" + idpracticalabora + "\'"
		
		try:
			cursor.execute(queryBorrarPracticaLabora)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("        Cerrar        ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("        Cerrar        ")

		self.cargartvPracticasLabora()

		cursor.close()

	def practicaLaboraDelete(self, widget, data=None):
		self.ventanaPracticaLabora.hide()
		return True

	def btConsultaCRojaClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.ventanaNuevoAAcoge.set_title("Cruz Roja")
		self.btAceptarConsultaAcoge.set_label("Aceptar")
		self.fixed6.move(self.btAceptarConsultaAcoge, 140, 0)
		self.btEliminarConsultaAcoge.set_visible(False)
		self.tbServicio.set_text("")
		self.tbTecnico.set_text("")
		self.tbFechaConsulta.set_text("")
		textbuffer = self.tbObserv.get_buffer()
		textbuffer.set_text("")

	def btDetalleCRojaClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.ventanaNuevoAAcoge.set_title("Cruz Roja")
		self.btAceptarConsultaAcoge.set_label("Actualizar")
		self.fixed6.move(self.btAceptarConsultaAcoge, 140, 0)
		self.btEliminarConsultaAcoge.set_visible(True)
		self.fixed6.move(self.btEliminarConsultaAcoge, 250, 0)

		tv = self.tvConsultasCRoja
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idcroja = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleConsultaCRoja = "SELECT * FROM CRUZ_ROJA WHERE IdCruzRoja = \'" + idcroja + "\'"

		try:
			cursor.execute(queryDetalleConsultaCRoja)
		except Exception, e:
			raise e

		resultadoDetalleConsultaCroja = cursor.fetchone()

		if resultadoDetalleConsultaCroja != None:
			self.tbServicio.set_text(resultadoDetalleConsultaCroja[1])
			self.tbTecnico.set_text(resultadoDetalleConsultaCroja[2])
			
			dateFormat = resultadoDetalleConsultaCroja[3].strftime("%d/%m/%Y") 
			self.tbFechaConsulta.set_text(dateFormat)

			textbuffer = self.tbObserv.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleConsultaCroja[4]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btConsultasSGITClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.ventanaNuevoAAcoge.set_title("Secretariado Gitano")
		self.btAceptarConsultaAcoge.set_label("Aceptar")
		self.fixed6.move(self.btAceptarConsultaAcoge, 140, 0)
		self.btEliminarConsultaAcoge.set_visible(False)
		self.tbServicio.set_text("")
		self.tbTecnico.set_text("")
		self.tbFechaConsulta.set_text("")
		textbuffer = self.tbObserv.get_buffer()
		textbuffer.set_text("")

	def btDetalleSGITClick(self, widget):
		self.ventanaNuevoAAcoge.show()
		self.ventanaNuevoAAcoge.set_title("Secretariado Gitano")
		self.btAceptarConsultaAcoge.set_label("Actualizar")
		self.fixed6.move(self.btAceptarConsultaAcoge, 140, 0)
		self.btEliminarConsultaAcoge.set_visible(True)
		self.fixed6.move(self.btEliminarConsultaAcoge, 250, 0)

		tv = self.tvConsultasSGIT
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idsgit = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleConsultaSGIT = "SELECT * FROM SGIT WHERE IdSGit = \'" + idsgit + "\'"

		try:
			cursor.execute(queryDetalleConsultaSGIT)
		except Exception, e:
			raise e

		resultadoDetalleConsultaSGIT = cursor.fetchone()

		if resultadoDetalleConsultaSGIT != None:
			self.tbServicio.set_text(resultadoDetalleConsultaSGIT[1])
			self.tbTecnico.set_text(resultadoDetalleConsultaSGIT[2])
			
			dateFormat = resultadoDetalleConsultaSGIT[3].strftime("%d/%m/%Y") 
			self.tbFechaConsulta.set_text(dateFormat)

			textbuffer = self.tbObserv.get_buffer() 
 		 	textbuffer.set_text(str(resultadoDetalleConsultaSGIT[4]))
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btNuevoExtranjClick(self, widget):
		self.ventanaNuevoEmpleoExtranj.show()
		self.btAceptarEmpresaExtranj.set_label("Aceptar")
		self.fixed9.move(self.btAceptarEmpresaExtranj, 140, 0)
		self.btEliminarEmpresaExtranj.set_visible(False)
		self.tbEmpresa.set_text("")
		self.tbFechaInicioEmpresa.set_text("")
		self.tbDuracion.set_text("")

	def btAceptarEmpresaExtranjClick(self, widget):
		empr = self.tbEmpresa.get_text()
		
		fIn = self.tbFechaInicioEmpresa.get_text()
		day = datetime.datetime.strptime(fIn, '%d/%m/%Y')
		fInicioEmpresa = day.strftime('%Y-%m-%d')
		
		dur = self.tbDuracion.get_text()

		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarEmpresaExtranj.get_label() == "Aceptar":
			
			queryObtenerIdExtranj = "SELECT IdExtranjeria FROM EXTRANJERIA WHERE IdMenor = \'" + idmenor + "\'"

			try:
				cursor.execute(queryObtenerIdExtranj)
			except Exception, e:
				raise e
				
			comprobacion = cursor.fetchone()

			if comprobacion != None:
		
				queryInsertarEmpresaExtranjeria = "INSERT INTO EXTRANJERIA_EMPRESA (NombreEEmpresa, FechaInicio, DuracionContrato, IdExtranjeria) VALUES (\'" + empr + "\', '" + fInicioEmpresa + "\', '" + dur + "\', '" + str(comprobacion[0]) + "\')" 

				try:
					cursor.execute(queryInsertarEmpresaExtranjeria)
					c.commit()
					self.msgbox.show()
					self.lbMsgBox.set_text("Empleo registrado con éxito")
					self.btMsgBoxAceptar.set_label("         Cerrar         ")
				except Exception, e:
					c.rollback()
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro")
					self.btMsgBoxAceptar.set_label("         Cerrar         ")

				self.cargartvExtranjeria()
			else:
				self.msgbox.show()
				self.lbMsgBox.set_text("Registre primero el permiso de trabajo")
				self.btMsgBoxAceptar.set_label("Cerrar")
			
		elif self.btAceptarEmpresaExtranj.get_label() == "Actualizar":
			tv = self.tvEmpleos
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				ideextranj = model[treeiter][2]
			
			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarEmpleoExtranj = "UPDATE EXTRANJERIA_EMPRESA SET NombreEEmpresa = \'" + empr + "\', FechaInicio = \'" + fInicioEmpresa + "\', DuracionContrato = \'" + dur + "\' WHERE IdEEmpresa = \'" + ideextranj + "\'"

			try:
				cursor.execute(queryActualizarEmpleoExtranj)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Empleo actualizado con éxito")
				self.btMsgBoxAceptar.set_label("         Cerrar         ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("         Cerrar         ")

			self.cargartvExtranjeria()
			
		cursor.close()

	def btDetalleEmpleoClick(self, widget):
		self.ventanaNuevoEmpleoExtranj.show()
		self.btAceptarEmpresaExtranj.set_label("Actualizar")
		self.fixed9.move(self.btAceptarEmpresaExtranj, 140, 0)
		self.btEliminarEmpresaExtranj.set_visible(True)
		self.fixed9.move(self.btEliminarEmpresaExtranj, 245, 0)

		tv = self.tvEmpleos
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			ideextranj = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleEmpleoExtranj = "SELECT * FROM EXTRANJERIA_EMPRESA WHERE IdEEmpresa = \'" + ideextranj + "\'"

		try:
			cursor.execute(queryDetalleEmpleoExtranj)
		except Exception, e:
			raise e

		resultadoDetalleEmpleoExtranj = cursor.fetchone()

		if resultadoDetalleEmpleoExtranj != None:
			self.tbEmpresa.set_text(resultadoDetalleEmpleoExtranj[1])

			dateFormat = resultadoDetalleEmpleoExtranj[2].strftime("%d/%m/%Y") 
			self.tbFechaInicioEmpresa.set_text(dateFormat)

			self.tbDuracion.set_text(resultadoDetalleEmpleoExtranj[3])
			
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarEmpresaExtranjClick(self, widget):
		tv = self.tvEmpleos
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			ideextranj = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarEmpleoExtranj = "DELETE FROM EXTRANJERIA_EMPRESA WHERE IdEEmpresa = \'" + ideextranj + "\'"
		
		try:
			cursor.execute(queryBorrarEmpleoExtranj)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminado con éxito")
			self.btMsgBoxAceptar.set_label("         Cerrar         ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("         Cerrar         ")

		self.cargartvExtranjeria()

		cursor.close()

	def empresaExtranjDelete(self, widget, data=None):
		self.ventanaNuevoEmpleoExtranj.hide()
		return True

	def btPropExtutClick(self, widget):
		self.ventanaPropExtut.show()
		self.btAceptarPropuesta.set_label("Aceptar")
		self.fixed11.move(self.btAceptarPropuesta, 135, 0)
		self.btEliminarPropuesta.set_visible(False)
		self.cargarcbxEntidadExtut()
		self.tbFechaEntidad.set_text("")
	
	def btAceptarPropuestaClick(self, widget):
		enti = self.cbxEntidadExtut.get_active_text()
		f = self.tbFechaEntidad.get_text()
		day = datetime.datetime.strptime(f, '%d/%m/%Y')
		fech = day.strftime('%Y-%m-%d')

		c = conexion.db
		cursor = c.cursor()

		if self.btAceptarPropuesta.get_label() == "Aceptar":	
			queryObtenerIdExTEntidad = "SELECT EXTUT_ENTIDADES.IdExTEntidad FROM EXTUT, EXTUT_ENTIDADES WHERE EXTUT_ENTIDADES.Nombre = \'" + enti + "\' AND EXTUT.IdMenor = \'" + idmenor + "\' AND EXTUT.IdExTEntidad = EXTUT_ENTIDADES.IdExTEntidad"

			try:
				cursor.execute(queryObtenerIdExTEntidad)
			except Exception, e:
				raise e
				
			comprobacion = cursor.fetchone()

			if comprobacion != None:
		
				queryObtenerIdExtut = "SELECT IdExtut FROM EXTUT WHERE IdMenor = \'" + idmenor + "\' AND IdExTEntidad = \'" + str(comprobacion[0]) + "\'" 

				try:
					cursor.execute(queryObtenerIdExtut)
				except Exception, e:
					raise e

				resultado = cursor.fetchone()

				if resultado != None:
					queryInsertarPropuestaExtut = "INSERT INTO EXTUT_PROPUESTAS (FechaPropuesta, IdExtut) VALUES (\'" + fech + "\', '" + str(resultado[0]) + "\')"
					try:
						cursor.execute(queryInsertarPropuestaExtut)
						c.commit()
						self.msgbox.show()
						self.lbMsgBox.set_text("Propuesta registrada con éxito")
						self.btMsgBoxAceptar.set_label("           Cerrar           ")
					except Exception, e:
						c.rollback()
						self.msgbox.show()
						self.lbMsgBox.set_text("Fallo en el registro")
						self.btMsgBoxAceptar.set_label("           Cerrar           ")
					
					self.cargartvPropuestasExtut()
				else:
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro.")
					self.btMsgBoxAceptar.set_label("           Cerrar           ")
		
			else:
				 queryObtenerIdExTEntidad = "SELECT IdExTEntidad FROM EXTUT_ENTIDADES WHERE Nombre = \'" + enti + "\'"
				 
				 try:
				 	cursor.execute(queryObtenerIdExTEntidad)
				 except Exception, e:
				 	raise e

				 comprobacion2 = cursor.fetchone()

				 if comprobacion2 != None:
				 	queryInsertarExTut = "INSERT INTO EXTUT (IdExTEntidad, IdMenor) VALUES (\'" + str(comprobacion2[0]) + "\', '" + idmenor + "\')" 
				 	try:
						cursor.execute(queryInsertarExTut)
						c.commit()
					except Exception, e:
						c.rollback()
						self.msgbox.show()
						self.lbMsgBox.set_text("Fallo en el registro")
						self.btMsgBoxAceptar.set_label("           Cerrar           ")

					queryObtenerIdExtut = "SELECT IdExtut FROM EXTUT WHERE IdMenor = \'" + idmenor + "\' AND IdExTEntidad = \'" + str(comprobacion2[0]) + "\'" 

					try:
						cursor.execute(queryObtenerIdExtut)
					except Exception, e:
						raise e

					resultado = cursor.fetchone()

					if resultado != None:
						queryInsertarPropuestaExtut = "INSERT INTO EXTUT_PROPUESTAS (FechaPropuesta, IdExtut) VALUES (\'" + fech + "\', '" + str(resultado[0]) + "\')"
						try:
							cursor.execute(queryInsertarPropuestaExtut)
							c.commit()
							self.msgbox.show()
							self.lbMsgBox.set_text("Propuesta registrada con éxito")
							self.btMsgBoxAceptar.set_label("           Cerrar           ")
						except Exception, e:
							c.rollback()
							self.msgbox.show()
							self.lbMsgBox.set_text("Fallo en el registro")
							self.btMsgBoxAceptar.set_label("           Cerrar           ")
						
						self.cargartvPropuestasExtut()
					else:
						self.msgbox.show()
						self.lbMsgBox.set_text("Fallo en el registro.")
						self.btMsgBoxAceptar.set_label("           Cerrar           ")

				 else:
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo al obtener la entidad")
					self.btMsgBoxAceptar.set_label("Cerrar")
				
		elif self.btAceptarPropuesta.get_label() == "Actualizar":
			tv = self.tvPropuestas
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idprop = model[treeiter][2]

			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarPropuesta = "UPDATE EXTUT_PROPUESTAS SET FechaPropuesta = \'" + fech + "\' WHERE IdProp = \'" + idprop + "\'"

			try:
				cursor.execute(queryActualizarPropuesta)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Fecha actualizada con éxito")
				self.btMsgBoxAceptar.set_label("           Cerrar           ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("           Cerrar           ")

			self.cargartvPropuestasExtut()

		cursor.close()

	def btDetallePropuestaClick(self, widget):
		self.ventanaPropExtut.show()
		self.btAceptarPropuesta.set_label("Actualizar")
		self.fixed11.move(self.btAceptarPropuesta, 135, 0)
		self.btEliminarPropuesta.set_visible(True)
		self.fixed11.move(self.btEliminarPropuesta, 240, 0)
		self.cargarcbxEntidadExtut()

		tv = self.tvPropuestas
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idprop = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetallePropuesta = "SELECT EXTUT_ENTIDADES.Nombre, EXTUT_PROPUESTAS.FechaPropuesta FROM EXTUT, EXTUT_ENTIDADES, EXTUT_PROPUESTAS WHERE EXTUT_PROPUESTAS.IdProp = \'" + idprop + "\' AND EXTUT.IdExtut = EXTUT_PROPUESTAS.IdExtut AND EXTUT.IdExTEntidad = EXTUT_ENTIDADES.IdExTEntidad"

		try:
			cursor.execute(queryDetallePropuesta)
		except Exception, e:
			raise e

		resultadoDetallePropuesta = cursor.fetchone()

		if resultadoDetallePropuesta != None:
		
			dateFormat = resultadoDetallePropuesta[1].strftime("%d/%m/%Y") 
			self.tbFechaEntidad.set_text(dateFormat)

			for posicion, elemento in enumerate(self.lsEntidadExtut):
				f = elemento[0]
				if f == str(resultadoDetallePropuesta[0]):
					self.cbxEntidadExtut.set_active(posicion)

		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarPropuestaClick(self, widget):
		tv = self.tvPropuestas
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idprop = model[treeiter][2]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarPropuesta = "DELETE FROM EXTUT_PROPUESTAS WHERE IdProp = \'" + idprop + "\'"
		
		try:
			cursor.execute(queryBorrarPropuesta)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("           Cerrar           ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("           Cerrar           ")

		self.cargartvPropuestasExtut()

		cursor.close()

	def propuestaExTutDelete(self, widget, data=None):
		self.ventanaPropExtut.hide()
		return True

	def btReunionExtutClick(self, widget):
		self.ventanaReunionesExtut.show()
		self.btAceptarReunion.set_label("Aceptar")
		self.fixed12.move(self.btAceptarReunion, 150, 0)
		self.btEliminarReunion.set_visible(False)
		self.cargarcbxEntidadExtut()
		self.tbFechaReunion.set_text("")
		textbuffer = self.tbAcuerdosReunion.get_buffer()
		textbuffer.set_text("")
		self.cbxTipoReunion.set_active(0)
		
	def btAceptarReunionExtutClick(self, widget):
		entid = self.cbxEntidadReunion.get_active_text()
		tip = self.cbxTipoReunion.get_active_text()
		f = self.tbFechaReunion.get_text()
		day = datetime.datetime.strptime(f, '%d/%m/%Y')
		fech = day.strftime('%Y-%m-%d')

		aR = self.tbAcuerdosReunion.get_buffer()
		acuerR = aR.get_text(*aR.get_bounds())

		c = conexion.db
		cursor = c.cursor()
		
		if self.btAceptarReunion.get_label() == "Aceptar":	
			queryObtenerIdExTEntidad = "SELECT EXTUT_ENTIDADES.IdExTEntidad FROM EXTUT, EXTUT_ENTIDADES WHERE EXTUT_ENTIDADES.Nombre = \'" + entid + "\' AND EXTUT.IdMenor = \'" + idmenor + "\' AND EXTUT.IdExTEntidad = EXTUT_ENTIDADES.IdExTEntidad"

			try:
				cursor.execute(queryObtenerIdExTEntidad)
			except Exception, e:
				raise e
				
			comprobacion = cursor.fetchone()

			if comprobacion != None:
		
				queryObtenerIdExtut = "SELECT IdExtut FROM EXTUT WHERE IdMenor = \'" + idmenor + "\' AND IdExTEntidad = \'" + str(comprobacion[0]) + "\'" 

				try:
					cursor.execute(queryObtenerIdExtut)
				except Exception, e:
					raise e

				resultado = cursor.fetchone()

				if resultado != None:
					queryInsertarReunionExtut = "INSERT INTO EXTUT_REUNIONES (TipoReunion, FechaReunion, AcuerdosReunion, IdExtut) VALUES (\'" + tip + "\', '" + fech + "\', '" + acuerR + "\', '" + str(resultado[0]) + "\')"
					try:
						cursor.execute(queryInsertarReunionExtut)
						c.commit()
						self.msgbox.show()
						self.lbMsgBox.set_text("Reunión registrada con éxito")
						self.btMsgBoxAceptar.set_label("            Cerrar            ")
					except Exception, e:
						c.rollback()
						self.msgbox.show()
						self.lbMsgBox.set_text("Fallo en el registro")
						self.btMsgBoxAceptar.set_label("            Cerrar            ")
					
					self.cargartvReunionesExtut()
				else:
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo en el registro.")
					self.btMsgBoxAceptar.set_label("            Cerrar            ")
		
			else:
				 queryObtenerIdExTEntidad = "SELECT IdExTEntidad FROM EXTUT_ENTIDADES WHERE Nombre = \'" + entid + "\'"
				 
				 try:
				 	cursor.execute(queryObtenerIdExTEntidad)
				 except Exception, e:
				 	raise e

				 comprobacion2 = cursor.fetchone()

				 if comprobacion2 != None:
				 	queryInsertarExTut = "INSERT INTO EXTUT (IdExTEntidad, IdMenor) VALUES (\'" + str(comprobacion2[0]) + "\', '" + idmenor + "\')" 
				 	try:
						cursor.execute(queryInsertarExTut)
						c.commit()
					except Exception, e:
						c.rollback()
						self.msgbox.show()
						self.lbMsgBox.set_text("Fallo en el registro")
						self.btMsgBoxAceptar.set_label("           Cerrar           ")

					queryObtenerIdExtut = "SELECT IdExtut FROM EXTUT WHERE IdMenor = \'" + idmenor + "\' AND IdExTEntidad = \'" + str(comprobacion2[0]) + "\'" 

					try:
						cursor.execute(queryObtenerIdExtut)
					except Exception, e:
						raise e

					resultado = cursor.fetchone()

					if resultado != None:
						queryInsertarReunionExtut = "INSERT INTO EXTUT_PROPUESTAS (TipoReunion, FechaReunion, AcuerdosReunion, IdExtut) VALUES (\'" + tip + "\', '" + fech + "\', '" + acuerR + "\', '" + str(resultado[0]) + "\')"
						try:
							cursor.execute(queryInsertarReunionExtut)
							c.commit()
							self.msgbox.show()
							self.lbMsgBox.set_text("Reunión registrada con éxito")
							self.btMsgBoxAceptar.set_label("            Cerrar            ")
						except Exception, e:
							c.rollback()
							self.msgbox.show()
							self.lbMsgBox.set_text("Fallo en el registro")
							self.btMsgBoxAceptar.set_label("            Cerrar            ")
						
						self.cargartvReunionesExtut()
					else:
						self.msgbox.show()
						self.lbMsgBox.set_text("Fallo en el registro.")
						self.btMsgBoxAceptar.set_label("            Cerrar            ")

				 else:
					self.msgbox.show()
					self.lbMsgBox.set_text("Fallo al obtener la entidad")
					self.btMsgBoxAceptar.set_label("Cerrar")
				
		elif self.btAceptarReunion.get_label() == "Actualizar":
			tv = self.tvReuniones
			selection = tv.get_selection()
			model, treeiter = selection.get_selected()
			if treeiter != None:
				idreunion = model[treeiter][3]

			c = conexion.db
			cursor = c.cursor()
		
			queryActualizarReunion = "UPDATE EXTUT_REUNIONES SET TipoReunion = \'" + tip + "\', FechaReunion = \'" + fech + "\', AcuerdosReunion = \'" + acuerR + "\' WHERE IdReunion = \'" + idreunion + "\'"

			try:
				cursor.execute(queryActualizarReunion)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Tipo, Fecha y Acuerdos de la reunión, actualizados con éxito")
				self.btMsgBoxAceptar.set_label("            Cerrar            ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("            Cerrar           ")

			self.cargartvReunionesExtut()

		cursor.close()

	def reunionesExTutDelete(self, widget, data=None):
		self.ventanaReunionesExtut.hide()
		return True

	def empresaExTutClick(self, widget):
		self.ventanaEmpresaExTut.show()
		self.btAceptarEntidadExtut.set_label("Aceptar")
		self.fixed10.move(self.btAceptarEntidadExtut, 140, 0)
		self.btEliminarEntidadExtut.set_visible(False)
		self.tbEntidad.set_text("")
		self.tbDireccionEntidad.set_text("")
		self.tbTelefonoEntidad.set_text("")
		self.tbMailEntidad.set_text("")

	def btAceptarEntidadExtutClick(self, widget):
		entity = self.tbEntidad.get_text()
		dirEntity = self.tbDireccionEntidad.get_text()
		tlfnEntity = self.tbTelefonoEntidad.get_text()
		mailEntity = self.tbMailEntidad.get_text()

		c = conexion.db
		cursor = c.cursor()


		if self.btAceptarEntidadExtut.get_label() == "Aceptar":
			
			queryInsertarEntidad = "INSERT INTO EXTUT_ENTIDADES (Nombre, Direccion, Telefono, Mail) VALUES (\'" + entity + "\', '" + dirEntity + "\', '" + tlfnEntity + "\', '" + mailEntity + "\')" 

			try:
				cursor.execute(queryInsertarEntidad)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Entidad grabada con éxito")
				self.btMsgBoxAceptar.set_label("          Cerrar          ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("El registro ha fallado")
				self.btMsgBoxAceptar.set_label("          Cerrar          ")
		
		elif self.btAceptarEntidadExtut.get_label() == "Actualizar":
			
			queryActualizarEntidad = "UPDATE EXTUT_ENTIDADES SET Nombre = \'" + entity + "\', Direccion = \'" + dirEntity + "\', Telefono = \'" + tlfnEntity + "\', Mail = \'" + mailEntity + "\' WHERE EXTUT_ENTIDADES.IdExTEntidad = \'" + self.tbIdEntidadExtut.get_text() + "\'" 

			try:
				cursor.execute(queryActualizarEntidad)
				c.commit()
				self.msgbox.show()
				self.lbMsgBox.set_text("Entidad actualizada con éxito")
				self.btMsgBoxAceptar.set_label("          Cerrar          ")
			except Exception, e:
				c.rollback()
				self.msgbox.show()
				self.lbMsgBox.set_text("La actualización ha fallado")
				self.btMsgBoxAceptar.set_label("          Cerrar          ")

			self.cargartvPropuestasExtut()
			self.cargartvReunionesExtut()
		cursor.close()

	def cargarcbxEntidadExtut(self):
		self.lsEntidadExtut.clear()

		queryEntidades = "SELECT Nombre FROM EXTUT_ENTIDADES ORDER BY Nombre ASC"

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryEntidades)
		except Exception, e:
			raise e

		resultado = cursor. fetchall()

		if len(resultado) > 0:
			for i in range(len(resultado)):
				self.lsEntidadExtut.append(resultado[i])
		else:
			self.lsEntidadExtut.append(row=None)


		cursor.close()

	def btDetalleReunionClick(self, widget):
		self.ventanaReunionesExtut.show()
		self.btAceptarReunion.set_label("Actualizar")
		self.fixed12.move(self.btAceptarReunion, 135, 0)
		self.btEliminarReunion.set_visible(True)
		self.fixed12.move(self.btEliminarReunion, 240, 0)
		self.cargarcbxEntidadExtut()

		tv = self.tvReuniones
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idreunion = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleReunion = "SELECT EXTUT_ENTIDADES.Nombre, EXTUT_REUNIONES.FechaReunion, EXTUT_REUNIONES.TipoReunion, EXTUT_REUNIONES.AcuerdosReunion FROM EXTUT, EXTUT_ENTIDADES, EXTUT_REUNIONES WHERE EXTUT_REUNIONES.IdReunion = \'" + idreunion + "\' AND EXTUT.IdExtut = EXTUT_REUNIONES.IdExtut AND EXTUT.IdExTEntidad = EXTUT_ENTIDADES.IdExTEntidad"

		try:
			cursor.execute(queryDetalleReunion)
		except Exception, e:
			raise e

		resultadoDetalleReunion = cursor.fetchone()

		if resultadoDetalleReunion != None:
		
			for posicion, elemento in enumerate(self.lsEntidadExtut):
				f = elemento[0]
				if f == str(resultadoDetalleReunion[0]):
					self.cbxEntidadReunion.set_active(posicion)

			dateFormat = resultadoDetalleReunion[1].strftime("%d/%m/%Y") 
			self.tbFechaReunion.set_text(dateFormat)
			
			for posicion, elemento in enumerate(self.lsTipoReunionExtut):
				f = elemento[0]
				if f == str(resultadoDetalleReunion[2]):
					self.cbxTipoReunion.set_active(posicion)

			textbuffer = self.tbAcuerdosReunion.get_buffer() 
 			textbuffer.set_text(str(resultadoDetalleReunion[3]))


		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarReunionClick(self, widget):
		tv = self.tvReuniones
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			idreunion = model[treeiter][3]
						
		c = conexion.db
		cursor = c.cursor()

		queryBorrarReunion = "DELETE FROM EXTUT_REUNIONES WHERE IdReunion = \'" + idreunion + "\'"
		
		try:
			cursor.execute(queryBorrarReunion)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("            Cerrar            ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La eliminación ha fallado")
			self.btMsgBoxAceptar.set_label("            Cerrar           ")

		self.cargartvReunionesExtut()

		cursor.close()

	def empresaExTutDelete(self, widget, data=None):
		self.ventanaEmpresaExTut.hide()
		return True

	def btDetalleEmpresaClick(self, widget):
		self.ventanaEmpresaExTut.show()
		self.btAceptarEntidadExtut.set_label("Actualizar")
		self.fixed10.move(self.btAceptarEntidadExtut, 120, 0)
		self.btEliminarEntidadExtut.set_visible(True)
		self.fixed10.move(self.btEliminarEntidadExtut, 225, 0)

		tv = self.tvPropuestas
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			presa = model[treeiter][0]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleEmpresa = "SELECT * FROM EXTUT_ENTIDADES WHERE EXTUT_ENTIDADES.Nombre = \'" + presa + "\'"

		try:
			cursor.execute(queryDetalleEmpresa)
		except Exception, e:
			raise e

		resultadoDetalleEmpresa = cursor.fetchone()

		if resultadoDetalleEmpresa != None:
			self.tbIdEntidadExtut.set_text(str(resultadoDetalleEmpresa[0]))
			self.tbEntidad.set_text(resultadoDetalleEmpresa[1])
			self.tbDireccionEntidad.set_text(resultadoDetalleEmpresa[2])
			self.tbTelefonoEntidad.set_text(str(resultadoDetalleEmpresa[3]))
			self.tbMailEntidad.set_text(resultadoDetalleEmpresa[4])

		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btDetalleEmpresa2Click(self, widget):
		self.ventanaEmpresaExTut.show()
		self.btAceptarEntidadExtut.set_label("Actualizar")
		self.fixed10.move(self.btAceptarEntidadExtut, 120, 0)
		self.btEliminarEntidadExtut.set_visible(True)
		self.fixed10.move(self.btEliminarEntidadExtut, 225, 0)

		tv = self.tvReuniones
		selection = tv.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			presa = model[treeiter][0]
						
		c = conexion.db
		cursor = c.cursor()

		queryDetalleEmpresa = "SELECT * FROM EXTUT_ENTIDADES WHERE EXTUT_ENTIDADES.Nombre = \'" + presa + "\'"

		try:
			cursor.execute(queryDetalleEmpresa)
		except Exception, e:
			raise e

		resultadoDetalleEmpresa = cursor.fetchone()

		if resultadoDetalleEmpresa != None:
			self.tbIdEntidadExtut.set_text(str(resultadoDetalleEmpresa[0]))
			self.tbEntidad.set_text(resultadoDetalleEmpresa[1])
			self.tbDireccionEntidad.set_text(resultadoDetalleEmpresa[2])
			self.tbTelefonoEntidad.set_text(str(resultadoDetalleEmpresa[3]))
			self.tbMailEntidad.set_text(resultadoDetalleEmpresa[4])

		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")
		
		cursor.close()

	def btEliminarEntidadExtutClick(self, widget):
		c = conexion.db
		cursor = c.cursor()

		queryBorrarEmpresa = "DELETE FROM EXTUT_ENTIDADES WHERE IdExTEntidad = \'" + self.tbIdEntidadExtut.get_text() + "\'"
		
		try:
			cursor.execute(queryBorrarEmpresa)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Eliminada con éxito")
			self.btMsgBoxAceptar.set_label("          Cerrar          ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("La empresa está en uso, no es posible su eliminación")
			self.btMsgBoxAceptar.set_label("          Cerrar          ")

		self.cargartvPropuestasExtut()
		self.cargartvReunionesExtut()

		cursor.close()

	def btSelecCentroClick(self, widget):
		self.ventanaSelecCentroEducativo.show()
		self.cargarCbxCentrosEducativos()
		
	def cargarCbxCentrosEducativos(self):
		self.lsCentrosEducativos.clear()

		queryCE = "SELECT NombreCE, IdCE FROM CENTRO_EDUCATIVO"

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryCE)
		except Exception, e:
			raise e

		centros = cursor.fetchall()

		if len(centros) > 0:
			for i in range(len(centros)):
				self.lsCentrosEducativos.append(centros[i])
		else:
			self.lsCentrosEducativos.append(row=None)

		cursor.close()

	def btNuevoCEClick(self, widget):
		self.centroEducativo.show()
		self.btEliminarCE.set_visible(False)
		self.btAceptarCE.set_label("Aceptar")
		self.fixed13.move(self.btAceptarCE, 180, 0)
		self.tbNombreCE.set_text("")
		self.tbDireccionCE.set_text("")
		self.tbTlfnoCE.set_text("")
		self.tbMailCE.set_text("")

	def btAceptarSelecCentroClick(self, widget):
		centroElegido = self.cbxCentroEducativo.get_active_text()
		self.ventanaSelecCentroEducativo.hide()
		self.tbCentroEducativo.set_text(centroElegido)
		#cargarmos el textbox con el Id del Centro Educativo elegido. El textbox no se muestra en pantalla.
		sitio = self.cbxCentroEducativo.get_active()
		for posicion, elemento in enumerate(self.lsCentrosEducativos):
			if posicion == sitio:
				self.tbCodCentEducativo.set_text(elemento[1])

	def btAceptarCEClick(self, widget):
		nombreCE = self.tbNombreCE.get_text()
		direccionCE = self.tbDireccionCE.get_text()
		tlfnoCE = self.tbTlfnoCE.get_text()
		mailCE = self.tbMailCE.get_text()

		queryInsertarCE = "INSERT INTO CENTRO_EDUCATIVO (NombreCE, DireccionCE, TelefonoCE, MailCE) VALUES (\'" + nombreCE + "\', '" + direccionCE + "\', '" +tlfnoCE + "\', '" + mailCE + "\')"

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryInsertarCE)
			c.commit()
			self.msgbox.show()
			self.lbMsgBox.set_text("Centro educativo registrado con éxito")
			self.btMsgBoxAceptar.set_label("             Cerrar             ")
		except Exception, e:
			c.rollback()
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo registrar el centro")
			self.btMsgBoxAceptar.set_label("             Cerrar             ")

		cursor.close()

		self.cargarCbxCentrosEducativos()

	def btEliminarCEClick(self, widget):
		pass

	def btDetalleCentroClick(self, widget):
		self.centroEducativo.show()
		self.btAceptarCE.set_label("Actualizar")
		self.fixed13.move(self.btAceptarCE, 120, 0)
		self.btEliminarCE.set_visible(True)
		self.fixed13.move(self.btEliminarCE, 225, 0)

		queryCE = "SELECT * FROM CENTRO_EDUCATIVO WHERE IdCE = \'" + self.tbCodCentEducativo.get_text() + "\'"

		c = conexion.db
		cursor = c.cursor()

		try:
			cursor.execute(queryCE)
		except Exception, e:
			raise e

		busqueda = cursor.fetchone()

		if len(busqueda) > 0:
			self.tbNombreCE.set_text(busqueda[1])
			self.tbDireccionCE.set_text(busqueda[2])
			self.tbTlfnoCE.set_text(str(busqueda[3]))
			self.tbMailCE.set_text(busqueda[4])
		else:
			self.msgbox.show()
			self.lbMsgBox.set_text("No se pudo recuperar el detalle")
			self.btMsgBoxAceptar.set_label("Cerrar")

		cursor.close()



	def centroEducativoDelete(self, widget, data=None):
		self.centroEducativo.hide()
		return True

	def selecCentroEducativoDelete(self, widget, data=None):
		self.ventanaSelecCentroEducativo.hide()
		return True

	def btFichaClick(self, widget):
		c = conexion.db
		cursor = c.cursor()

		try:
			query = "SELECT EXPEDIENTE.FechaApertura, EXPEDIENTE.EQM, ADMISION.FechaAdmision, MENOR.FechaNac, MENOR.Pasaporte, MENOR.Sexo, MENOR.Desamparo, MENOR.Direccion, MENOR.CP, MENOR.Localidad, MENOR.Provincia, MENOR.Telefono1, MENOR.Telefono2, MENOR.Mail, MENOR.Nacionalidad, MENOR.Empadronamiento, MENOR.NUSS, MENOR.NUSSA, MENOR.CIN, DNI.TipoDoc FROM EXPEDIENTE, ADMISION, MENOR, DNI WHERE EXPEDIENTE.IdExpdte= \"" + self.lbMostrarExpdte.get_text() + "\" AND EXPEDIENTE.IdExpdte = ADMISION.IdExpdte AND EXPEDIENTE.IdMenor = MENOR.IdMenor AND MENOR.DNI = DNI.DNI"
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
		fichaMenor.Ficha().cargarDatos(fechaAdm, self.lbMostrarExpdte.get_text(), fechaAper, eqm, self.lbMostrarNombre.get_text(), self.lbMostrarDNI.get_text(), pasaporte, fechaNac, direccion, cp, sexo, localidad, prov, tlfno, movil, mail, nacion, padron, nuss, nussa, cin, desamparo, tipodoc)
		self.ficha.hide()

		cursor.close()

	def fichaDelete(self, widget, data=None):
		self.ficha.hide()
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
		elif self.btMsgBoxAceptar.get_label() == "       Cerrar       ":
			self.msgbox.hide()
			self.ventanaCursoLabora.hide()
		elif self.btMsgBoxAceptar.get_label() == "        Cerrar        ":
			self.msgbox.hide()
			self.ventanaPracticaLabora.hide()
		elif self.btMsgBoxAceptar.get_label() == "         Cerrar         ":
			self.msgbox.hide()
			self.ventanaNuevoEmpleoExtranj.hide()
		elif self.btMsgBoxAceptar.get_label() == "          Cerrar          ":
			self.msgbox.hide()
			self.ventanaEmpresaExTut.hide()
			self.cargarcbxEntidadExtut()
		elif self.btMsgBoxAceptar.get_label() == "           Cerrar           ":
			self.msgbox.hide()
			self.ventanaPropExtut.hide()
		elif self.btMsgBoxAceptar.get_label() == "            Cerrar            ":
			self.msgbox.hide()
			self.ventanaReunionesExtut.hide()
		elif self.btMsgBoxAceptar.get_label() == "             Cerrar             ":
			self.msgbox.hide()
			self.centroEducativo.hide()


		