import serial
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
#import statistics as stats
#DATOS BEACON 3
A0=-55.519
m=22.8955
"""
DATOS BEACON 2
m=15.617
A0=-58.9235
"""
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
RSSIlist=[]
A=True
while A:
	RSSIstr= ser.readline()
	RSSI=float(RSSIstr)
	d=10**((A0-RSSI)/m)
	RSSIlist.append(RSSI)
	print d
	counter += 1
	if counter%10 == 0 and counter != 0 and counter :
		RSSIprom=mean(RSSIlist)
		dprom=10**((A0-RSSIprom)/m)
		print(" distancia Promedio:")
		print dprom
		#print("std:")
		#print(stats.pstdev(RSSIlist))
		print("END")
	if counter==10:
		A=False
