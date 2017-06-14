import time
import random

class Insumo():
	def __init__(self, Cantidad = 5,Nombre ="Sin Nombre"):
		 self.Cantidad=Cantidad
                 self.Nombre = Nombre
		 falla=Falla()
	def consumir(self,mq,cuanto):
		self.Cantidad = self.Cantidad - cuanto
		print "Maquina",mq,"  consumido: ", self.Nombre, "Cantidad: ",cuanto," cantidad restante: ", self.cantidad_disponible(),"\n"
	def reponer(self,cant):
		self.Cantidad = cant
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
		return "Algo esta fallando \n"
	def fallar(self):
		self.estaFallando=True
		print "Esta fallando la maquina: " + self.nombreMaquina + ", Causa:" + self.causa + "\n"

class Maquina():
	def __init__(self, MantenimEn=10, Nombre ="Sin Nombre", cant_chances=3):
		
		self.MantenimEn=MantenimEn
		self.fallas=[]
		self.Nombre = Nombre
		self.Inicial=MantenimEn
		self.Estado=self.Nombre," funcionando \n"
		self.horasUso=0
		self.cant_chances=cant_chances
		funcionando=False
		self.tiempoRuptura=0

	def parar(self):
		if self.funcionando:
			self.funcionando = False
			print self.Nombre, "detenida\n"	
        def horas(self):
            return self.horasUso
	def marcha(self):
		if self.fallas==[]:
                    self.funcionando = True
                    self.horasUso+=1
                    time.sleep(10)
        def autochek(self):
            if self.MantenimEn<self.horasUso:
                return True
            else:
                return False
        def Consumir(self,ins,cant):
            ins[1]-=cant
            return ins

class Mantenimiento():
    def __init__(self,Nombre ="Sin Nombre"):
        self.Nombre=Nombre
    def Reparar(self,m):
        m[1]=[]
	time.sleep(random.randint(5,10))
        return m
    def Reponer(self,x):
        x[1]=x[2]
	time.sleep(random.randint(5, 10))
        return x
    def Mantener(self,i):
        i[1]=i[2]
	time.sleep(random.randint(5, 10))
        return i
        

