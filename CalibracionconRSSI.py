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
RSSIlist=[]
A=True
while A:
	RSSIstr= ser.readline()
	RSSI=float(RSSIstr)
	RSSIlist.append(RSSI)
	print RSSI
	counter += 1
	if counter%20 == 0 and counter != 0 and counter :
		RSSIprom=mean(RSSIlist)
		print("Promedio:")
		print RSSIprom
		print("END")
	if counter==20:
		A=False

	





