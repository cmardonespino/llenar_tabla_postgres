# -- coding: utf-8 --

import sys, os
import psycopg2
import pandas

conn = psycopg2.connect(dbname='', user='', host='', password='')
cur = conn.cursor()

path_ubicado = os.getcwd()
path_excel = path_ubicado+'/codigos_fonasa/4_MLE_2018.xlsx'
df = pandas.read_excel(path_excel, sheet_name='ANEXO LIMPIO(2018valor)')


for i in df.index:
	codigo_fonasa = df[u'CÓDIGO'][i]
	pab = df[u'PAB.'][i]
	denominacion = df[u'DENOMINACIÓN'][i] 
	eq = df[u'EQ.'][i]
	precio_cirjuano_1 = df[u'CIRUJANO 1'][i]
	precio_cirjuano_2 = df[u'CIRUJANO 2'][i]
	precio_cirjuano_3 = df[u'CIRUJANO 3'][i]
	precio_anestesista = df[u'ANESTESISTA'][i]

	query = """
		INSERT INTO bonos_fonasa_bonos_fonasa 
		(codigo_fonasa, pab, denominacion, eq, precio_cirjuano_1, 
		precio_cirjuano_2, precio_cirjuano_3, precio_anestesista) 
		VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
		"""
	

	data = (
		codigo_fonasa, 
		pab, 
		denominacion, 
		eq, 
		precio_cirjuano_1, 
		precio_cirjuano_2, 
		precio_cirjuano_3, 
		precio_anestesista
	)
	cur.execute(query, data)
	conn.commit()
cur.close()
conn.close()