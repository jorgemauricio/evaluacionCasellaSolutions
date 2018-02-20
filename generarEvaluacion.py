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
			dataTemp['PM10_1H'] = dataTemp['PM10_15M']
			dataTemp['PM10_15M'] = dataTemp['PM10_5M']
			dataTemp['PM10_5M'] = dataTemp['PM10_1M']
			dataTemp['PM10_1M'] = dataTemp['PM2P5_1H']
			dataTemp['PM2P5_1H'] = dataTemp['PM2P5_15M']
			dataTemp['PM2P5_15M'] = dataTemp['PM2P5_5M']
			dataTemp['PM2P5_5M'] = dataTemp['PM2P5_1M']
			dataTemp['PM2P5_1M'] = dataTemp['PM1_1H']
			dataTemp['PM1_1H'] = dataTemp['PM1_15M']
			dataTemp['PM1_15M'] = dataTemp['PM1_5M']
			dataTemp['PM1_5M'] = dataTemp['PM1_1M']
			dataTemp['PM1_1M'] = dataTemp['Time']
			dataTemp['Time'] = dataTemp.index
			dataTemp.index = range(len(dataTemp['Time']))
			dataTemp2 = dataTemp.filter(['Time', 'PM1_1M', 'PM1_5M', 'PM1_15M', 'PM1_1H', 'PM2P5_1M', 'PM2P5_5M','PM2P5_15M', 'PM2P5_1H', 'PM10_1M', 'PM10_5M', 'PM10_15M', 'PM10_1H'])
			frames.append(dataTemp2)
			print("***** {}".format(i))
			print(dataTemp2.head(20))

		# concatenar información
		data = pd.concat(frames,ignore_index=True)
		print(i)
		print(data.head())

		# generar csv
		nombreTemporalParaGuardarArchivo = 'data/{}.csv'.format(i,i)
		data.to_csv(nombreTemporalParaGuardarArchivo)

		# ciclo para generar gráficas
		for k in data.columns[2:]:
			plt.clf()
			plt.figure(figsize=(80,10))
			print(data["Time"].head())
			xValues = data['Time']
			y = data[k]
			x = range(len(xValues))
			plt.plot(x,y)
			plt.title(k)
			plt.xlabel('Fecha')
			plt.ylabel('Valor')
			plt.xticks(x, xValues, rotation='vertical')
			nombreTemporalGrafica = "data/{}/{}-{}.png".format(i,i,k)
			plt.savefig(nombreTemporalGrafica, dpi=300)
			print(nombreTemporalGrafica)

if __name__ == '__main__':
	main()
