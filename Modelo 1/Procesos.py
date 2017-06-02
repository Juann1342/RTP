import time
import threading
from Clases import*


semaforo=0
maximo=2    #variable que define la concurrencia maxima que queremos tener
consumiendo=False  #Al ponerse en True se consumen insumos


def insumo():					#Gestiona los insumos
	insumo=Insumo(10)
	global semaforo, maximo
	while True:
		time.sleep(1)
		if consumiendo:
			insumo.consumir()
			if insumo.cantidad_disponible()<=0:
				semaforo+=2
				insumo.reponer()
				time.sleep(10)
				print "Insumos listos \n"
				print " .\n"
				semaforo-=2
		
def maquina(nombre,mantenimiento):				#Gestiona las maquinas recibe:
	global semaforo, maximo, consumiendo          #(Nombre de maquina, cantidad de horas hasta efectuar el mantenimiento)
	maquina=Maquina(mantenimiento,nombre)
	maquina.marcha()
	while True:
		time.sleep(2)
		if  not maquina.estado_optimo():
			if maquina.romper():
				print "Maquina ",nombre, "averiada, a la espera de mantenimiento \n"
			if semaforo < maximo:
				semaforo +=1   #Comienzo de la zona critica
				maquina.parar()
				maquina.efectuar_mantenimiento()
				consumiendo=True
				time.sleep(1)
				consumiendo=False
				time.sleep(7)
				semaforo-=1   #Fin de la zona critica
				maquina.marcha()		
			else:
				print "Maquina ",nombre, "esperando \n"
				
