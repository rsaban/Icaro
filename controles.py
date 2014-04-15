#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion
from tallerTS import taller_ts


class controls:
	
	def __init__(self):

		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaControles = ruta + "Controles.glade"

		builder= gtk.Builder()
		builder.add_from_file(pantallaControles)

		dict = {"on_btTallerTS_clicked": self.btTallerTSClick
				}
		builder.connect_signals(dict)

	def btTallerTSClick(self, widget):
		taller_ts()
