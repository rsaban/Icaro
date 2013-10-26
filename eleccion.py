#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
from busqueda import ventanaBusqueda
from nuevoExpdte import nuevoExp

class ventanaEleccion:
	
	def __init__(self):
		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaEleccion = ruta + "Eleccion.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaEleccion)
		self.ventana = builder.get_object("eleccion")


		dict = {"on_btBusqueda_clicked": self.btBusquedaClick, 
				"on_btAltaUsuario_clicked": self.btNuevoExpdteClick}
		builder.connect_signals(dict)


	
	def btBusquedaClick (self, widget):
		ventanaBusqueda()
		#ventanaBusqueda().cambiarbotones("Ber", "Buskar") 
		self.ventana.hide()

	def btNuevoExpdteClick(self, widget):
		nuevoExp()
		self.ventana.hide()



	


			