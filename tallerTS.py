#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import conexion


class taller_ts:
	
	def __init__(self):

		#Obtenemos la ruta de la carpeta donde se encuentra el glade
		pathname = os.path.dirname(sys.argv[0])
		ruta = os.path.abspath(pathname) + "/UI/"
		pantallaTallerTS = ruta + "tallerTS.glade"

		builder= gtk.Builder()
		builder.add_from_file(pantallaTallerTS)

		#dict = {				}
		#builder.connect_signals(dict)


