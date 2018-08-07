#!/usr/bin/python
# -*- coding: utf-8 -*-
#print("hola")
import serial
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
def mean(unaLista):
	prom =0
	for x in range(0,len(unaLista)):
		prom += unaLista[x]
	return (prom*1.0)/(len(unaLista))
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB0'
ser.open()
counter = 0
ld1 = []
ld2 = []
ld3 = []
ld4 = []

while True:
	#v=raw_input('Introduce distancia :')
	#if v=="close":
		#ser.close()
	#d= float(v)
	#values = bytearray([d])
	#ser.write(values)
	#print ser.readline()
	ldstr=ser.readline().split(",")
	if len(ldstr)==4:
		ld = []
		for item in ldstr:
    			ld.append(float(item))

		ld1.append(ld[0])
		ld2.append(ld[1])
		ld3.append(ld[2])
		ld4.append(ld[3])
		print ld

		counter += 1
	
	if counter%5 == 0 and counter != 0:
		d1 =mean(ld1)
		d2 =mean(ld2)
		d3 =mean(ld3)
		d4 =mean(ld4)
		print d1
		print d2
		print d3 
		print d4
		#modificar puntos de beacons
		o1=(0,0)
		o2=(0,5)
		o3=(5,0)
		o4=(5,5)
		#atento
		circle1 = plt.Circle(o1, d1,alpha=0.5, color='r')
		circle2 = plt.Circle(o2, d2,alpha=0.5, color='blue')
		circle3 = plt.Circle(o3, d3,alpha=0.5, color='g')
		circle4 = plt.Circle(o4, d4,alpha=0.5, color='blue')
		point1=plt.Circle(o1, 0.1, alpha=1, lw=1,color='#000000')
		point2=plt.Circle(o2, 0.1, alpha=1, lw=1,color='#000000')
		point3=plt.Circle(o3, 0.1, alpha=1, lw=1,color='#000000')
		point4=plt.Circle(o4, 0.1, alpha=1, lw=1,color='#000000')
		fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
		# (or if you have an existing figure)
		# fig = plt.gcf()
		# ax = fig.gca()
		#cambiamos tamaño por defecto ejes
		ax.set_xlim((-20, 20))
		ax.set_ylim((-20, 20))
		#añadimos circulos al grafico
		ax.add_artist(circle1)
		ax.add_artist(circle2)
		ax.add_artist(circle3)
		ax.add_artist(circle4)
		#añadimos centros de los circulos al grafico
		ax.add_artist(point1)
		ax.add_artist(point2)
		ax.add_artist(point3)
		ax.add_artist(point4)
		plt.show()

		
		
ser.close()


