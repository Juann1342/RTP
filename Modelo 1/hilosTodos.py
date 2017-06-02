import time
import threading
from Procesos import*


def main():			
	t1=threading.Thread(target=insumo,args=())	  #Creo el hilo para insumo
		
	t2=threading.Thread(target=maquina,args=("Envasadora",6,))  #Creo los hilos para las maquinas
	
	t3=threading.Thread(target=maquina,args=("Cortadora",7,))
	
	t4=threading.Thread(target=maquina,args=("Etiquetadora",6,))
	
	t5=threading.Thread(target=maquina,args=("Empaquetadora",8,))
	
	t6=threading.Thread(target=maquina,args=("Transportadora",3,))
	
	t7=threading.Thread(target=maquina,args=("Mezcladora",8,))
	
	t8=threading.Thread(target=maquina,args=("Inyectora",10,))
	
	t1.start()   #Inicializo todos los hilos
	time.sleep(1)
	t2.start()
	time.sleep(1)
	t3.start()
	time.sleep(1)
	t4.start()
	time.sleep(1)
	t5.start()
	time.sleep(1)
	t6.start()
	time.sleep(1)
	t7.start()
	time.sleep(1)
	t8.start()

	
	
main()
