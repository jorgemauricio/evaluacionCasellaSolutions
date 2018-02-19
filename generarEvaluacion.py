#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Script que genera un archivo acumulado
# de los datos que se reciben de Casella
# Solutions
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################
"""
# librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
	# lista de estaciones
	arrayEstaciones = ['AgricolaElSocorro', 'CampoSanJuan','RanchoElMexicano','RanchoJesusArmida']

	# ciclo de procesamiento
	for i in arrayEstaciones:
		# ruta para archivos de estaciones
		rutaDeArchivosEstacion = 'data/{}'.format(i)
		# numero de archivos de la estacion
		listaDeArchivos = [x for x in os.listdir(rutaDeArchivosEstacion) if x.endswith('.csv')]

		# ciclo de generacion de un solo archivo por Estación
		frames = []

		for j in listaDeArchivos:
			nombreTemporalDelArchivo = "data/{}/{}".format(i,j)
			dataTemp = pd.read_csv(nombreTemporalDelArchivo)
			frames.append(dataTemp)

		# concatenar información
		data = pd.concat(frames)

		# generar csv
		nombreTemporalParaGuardarArchivo = 'data/{}/{}.csv'.format(i,i)
		data.to_csv(nombreTemporalParaGuardarArchivo)

if __name__ == '__main__':
	main()
