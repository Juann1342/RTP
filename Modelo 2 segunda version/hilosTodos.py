import time
import threading
from Procesos import*

class cola():
	lista=[]
	def push(self,elemento):
		self.lista.append(elemento)
	def pop(self):
		temp=self.lista[0]
		del self.lista[0]
		return temp
	def isEmpty(self):
		if self.lista== []:
			return True
		else:
			return False

		
def main():	
	c=cola()
		
	#Creo los hilos y los meto en cola
	t0=threading.Thread(target=imprimir,args=())
	c.push(t0)
	t1=threading.Thread(target=insumo,args=("Papel",190))
	c.push(t1)		
	t2=threading.Thread(target=maquina,args=("Envasadora",random.randint(50,300),[["Plastico",random.randint(1,30)],["Aceite",random.randint(1,30)]]))
	c.push(t2)	
	t3=threading.Thread(target=maquina,args=("Cortadora",random.randint(50,300),[["Carton",random.randint(1,30)]]))
	c.push(t3)	
	t4=threading.Thread(target=maquina,args=("Etiquetadora",random.randint(50,300),[["Etiquetas",random.randint(1,30)]]))
	c.push(t4)	
	t5=threading.Thread(target=maquina,args=("Empaquetadora",random.randint(50,300),[["Papel",3],["Aceite",random.randint(1,30)]]))
	c.push(t5)	
	t6=threading.Thread(target=maquina,args=("Transportadora",random.randint(50,300),[["Aceite",random.randint(1,30)]]))
	c.push(t6)	
	t7=threading.Thread(target=maquina,args=("Mezcladora",random.randint(50,300),[["Aceite",random.randint(1,30)]]))
	c.push(t7)	
	t8=threading.Thread(target=maquina,args=("Inyectora",random.randint(50,300),[["Plastico",random.randint(1,30)],["Aceite",random.randint(1,30)]]))
	c.push(t8)	
	t9=threading.Thread(target=insumo,args=("Carton",random.randint(50,150)))
	c.push(t9)	
	t10=threading.Thread(target=insumo,args=("Aceite",random.randint(50,400)))
	c.push(t10)
	t11=threading.Thread(target=insumo,args=("Etiquetas",random.randint(50,300)))
	c.push(t11)	
	t12=threading.Thread(target=insumo,args=("Plastico",random.randint(30,300)))
	c.push(t12)	
	t13=threading.Thread(target=mantenimiento,args=("Operador 1",))
	c.push(t13)	
	t14 = threading.Thread(target=mantenimiento, args=("Operador 2",))
	c.push(t14)	
	t15 = threading.Thread(target=mantenimiento, args=("Operador 3",))
	c.push(t15)	
	t16 = threading.Thread(target=mantenimiento, args=("Operador 4",))
	c.push(t16)	
	t17 = threading.Thread(target=mantenimiento, args=("Operador 5",))
	c.push(t17)	
	t18 = threading.Thread(target=mantenimiento, args=("Operador 6",))
	c.push(t18)
	t19 = threading.Thread(target=mantenimiento, args=("Operador 7",))
	c.push(t19)
	t20=threading.Thread(target=fallar,args=())
	c.push(t20)	

	#mientras haya elementos en la cola, saco un hilo, lo inicio, espero un tiempo random para el siguiente
	while not c.isEmpty():
		th=c.pop()
		th.start()
		time.sleep(random.randint(1,4))

	

main()
