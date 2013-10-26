#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import MySQLdb

varglob = 'administrador'

db_host = 'localhost'
usuario = 'root'
clave= 'toor'
base_de_datos= 'Icaro'
	

db = MySQLdb.connect(host=db_host, user=usuario, passwd=clave, db=base_de_datos)

#, charset='utf8', init_command='set names utf8')