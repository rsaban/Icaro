#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
from controlUsuarios import users
from centroTrabajo import working_center

class tools:
	
	def __init__(self):
		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaHerramientas = ruta + "Herramientas.glade"
		
		builder= gtk.Builder()
		builder.add_from_file(pantallaHerramientas)


			
		dict = {"on_btUsuarios_clicked": self.ControlUsuariosClick,
				"on_btNuevoCentro_clicked": self.btNuevoCentroClick,
				}
		builder.connect_signals(dict)

	def ControlUsuariosClick(self, widget):
		users()

	def btNuevoCentroClick(self, widget):
		working_center()