import time
import random

class Insumo():  #Insumos que son cunsumidos por las maquinas al efectuar mantenimiento
	def __init__(self, Cantidad = 5):
		 self.Cantidad=Cantidad
		 self.Inicial= Cantidad
		 falla=Falla()
	def consumir(self):
		self.Cantidad = self.Cantidad -1
		print "Consumiendo insumos, cantidad disponible", self.cantidad_disponible(),"\n\n"
	def reponer(self):
		print "Reponiendo insumos"
		self.Cantidad = self.Inicial
	def cantidad_disponible(self):
		return self.Cantidad
	def __str__(self):
		return self.Cantidad
	
class Falla():
	def __init__(self, nombreMaquina="Desconocida", causa="Desconocida", estaFallando=False):
		self.nombreMaquina=nombreMaquina
		self.estaFallando=estaFallando
		self.causa=causa
	def alerta():
		return "Algo esta fallando"
	def fallar(self):
		self.estaFallando=True
		print "Esta fallando la maquina: " + self.nombreMaquina + ", Causa:" + self.causa + "\n"

class Maquina():
	def __init__(self, MantenimEn=10, Nombre ="Sin Nombre", cant_chances=3):
		
		self.MantenimEn=MantenimEn
		self.fallas=[]
		self.Nombre = Nombre
		self.Inicial=MantenimEn
		self.Estado=self.Nombre," funcionando"
		self.horasUso=0
		self.cant_chances=cant_chances
		funcionando=False
		self.tiempoRuptura=0

	def fallaRandom(self):
		if random.randint(0,1) == 1:
			if self.cant_chances == 0:
				self.fallar()
				self.cant_chances = 3
			else:
				self.cant_chances-=1
	
	def fallar(self):
		falla = Falla(self.Nombre, "Rotura")
		self.fallas.append(falla)
	
	def parar(self):
		if self.funcionando:
			self.funcionando = False
			print self.Nombre, "detenida\n"	
		
	def sacarFallas(self):
		while self.fallas!=[]:
			self.parar()
			aux = self.fallas.pop()
			aux.fallar()

	def tieneFallas(self):
		if self.fallas == []:
			return False
		return True
		
	def __str__(self):
		return str(self.MantenimEn)+" "+self.Nombre

	def marcha(self):               #Utiliza un bucle while para simular el funcionamiento de la maquina
		if not self.tieneFallas():
			self.funcionando = True
			print self.Nombre, "en marcha \n"
			while self.MantenimEn!=self.horasUso and self.funcionando == True:
				self.fallaRandom()
				self.horasUso = self.horasUso+1
			#	print self.Nombre," Funcionando hace ",self.horasUso," horas \n"
				time.sleep(5)
			if self.MantenimEn == self.horasUso:
				self.Estado=self.Nombre," Necesita mantenimiento"
			else:
				self.estado=self.Nombre," funcionando"
		else:
			self.sacarFallas()
			print self.Nombre + " no puede arrancar debido a fallas"


	def efectuar_mantenimiento(self):  #Al efectuar mantenimiento reinicia el contador de horas
		self.horasUso=0
		self.estado=self.Nombre," En mantenimiento"
		print "Efectuando mantenimiento a maquina ",self.Nombre,"\n \n"
		
	def estado_optimo(self):     # Devuelve true o false dependiendo si esta en estado optimo o necesita matenimiento
		if self.tieneFallas():
			self.sacarFallas()
			return False
			
		elif self.horasUso < self.MantenimEn:
			self.tiempoRuptura=0
			return True
		else:
			self.tiempoRuptura+=1
			return False
	def romper(self):        #Cuando esta mucho tiempo sin mantenimiento, se rompe
		if self.tiempoRuptura==10:
			self.horasUso=self.MantenimEn
			return True
		else:
			return False
