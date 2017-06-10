import time
import threading
from Procesos import*


def main():	
    	t0=threading.Thread(target=imprimir,args=())
	t1=threading.Thread(target=insumo,args=("Papel",190))	
		
	t2=threading.Thread(target=maquina,args=("Envasadora",random.randint(50,300),[["Plastico",random.randint(1,30)],["Aceite",random.randint(1,30)]]))
	
	t3=threading.Thread(target=maquina,args=("Cortadora",random.randint(50,300),[["Carton",random.randint(1,30)]]))
	
	t4=threading.Thread(target=maquina,args=("Etiquetadora",random.randint(50,300),[["Etiquetas",random.randint(1,30)]]))
	
	t5=threading.Thread(target=maquina,args=("Empaquetadora",random.randint(50,300),[["Papel",3],["Aceite",random.randint(1,30)]]))
	
	t6=threading.Thread(target=maquina,args=("Transportadora",random.randint(50,300),[["Aceite",random.randint(1,30)]]))
	
	t7=threading.Thread(target=maquina,args=("Mezcladora",random.randint(50,300),[["Aceite",random.randint(1,30)]]))
	
	t8=threading.Thread(target=maquina,args=("Inyectora",random.randint(50,300),[["Plastico",random.randint(1,30)],["Aceite",random.randint(1,30)]]))
        
        t9=threading.Thread(target=insumo,args=("Carton",random.randint(50,150)))
        
        t10=threading.Thread(target=insumo,args=("Aceite",random.randint(50,400)))
        
        t11=threading.Thread(target=insumo,args=("Etiquetas",random.randint(50,300)))
        
        t12=threading.Thread(target=insumo,args=("Plastico",random.randint(30,300)))
	
        t13=threading.Thread(target=fallar,args=())
        t14=threading.Thread(target=mantenimiento,args=("Operador 1",))
	t15 = threading.Thread(target=mantenimiento, args=("Operador 2",))
	t16 = threading.Thread(target=mantenimiento, args=("Operador 3",))
	t17 = threading.Thread(target=mantenimiento, args=("Operador 4",))
	t18 = threading.Thread(target=mantenimiento, args=("Operador 5",))
	t19 = threading.Thread(target=mantenimiento, args=("Operador 6",))
	t20 = threading.Thread(target=mantenimiento, args=("Operador 7",))


	t0.start()
	t1.start()
	time.sleep(1)
	t14.start()
	time.sleep(1)
	t15.start()
	time.sleep(1)
	t16.start()
	time.sleep(1)
	t17.start()
	time.sleep(1)
	t18.start()
	time.sleep(1)
	t19.start()
	time.sleep(1)
	t20.start()
	time.sleep(1)
	
	t9.start()
    	time.sleep(1)
	t10.start()
        time.sleep(1)
	t11.start()
        time.sleep(1)
	t12.start()
	time.sleep(1)
        t8.start()
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

	t13.start()
main()
