import time
import threading
from Clases import*


Semaforo=0
maximo=2
Reponer=[]
LSInsumo=[]
LSFallas=[]
LMant=[]
pantalla=[]
def imprimir():
    global pantalla
    print "Comienzo del hilo para mostrar datos por pantalla"
    print "################################################################ \n"
    while True:
        for t in pantalla:
            print t
            pantalla.pop(pantalla.index(t))
            
def insumo(nombre,ca):
	insumo=Insumo(ca, nombre)
        Fa=[nombre,[],0]
        LSFallas.append(Fa)
	global semaforo, maximo,LSInsumo,LMant
        ins=[nombre,ca,ca,0,0]
        LSInsumo.append(ins)
	while True:
                while not Fa[1]==[]:
                    time.sleep(random.randint(1,5))
                    pantalla.append("Esperando reparacion de "+ Fa[0]+" \n")
                    time.sleep(random.randint(12,16))
                    
                    
def mantenimiento(nombre):
    mant=Mantenimiento(nombre)
    global Semaforo,LSFallas,Reponer
    pantalla.append(nombre+ " comienza a trabajar  \n")
    Fa = [nombre, [], 0]
    LSFallas.append(Fa)
    while True:
        if Fa[1]==[]:
            if Semaforo>0:
                for i in LSFallas:
                    if not i[1]==[] and i[2]==0:
                        i[2]=1
                        pantalla.append(nombre + " empezo a reparar " + i[0] + " \n")
                        i=mant.Reparar(i)
                        pantalla.append(nombre+ " reparo "+i[0]+" \n")
                        Semaforo-=1
                        i[2]=0
                        break
            else:
                for x in Reponer:
                    if x[4]==0:
                        x[4] = 1
                        pantalla.append(nombre + " empezo a reponer insumo " + x[0] + " \n")
                        x=mant.Reponer(x)
                        pantalla.append(nombre+ " repuso insumo "+x[0]+" \n")
                        x[4]=0
                        Reponer.pop(Reponer.index(x))
                        break

                for i in LMant:
                    if i[3]==0:
                        i[3]=1
                        pantalla.append(nombre + " comenzo mantenimiento en " + i[0] + " \n")
                        i=mant.Mantener(i)
                        pantalla.append(nombre+ " aplico mantenimiento en "+i[0]+" \n")
                        i[3]=0
                        LMant.pop(LMant.index(i))
                        break
        else:
            pantalla.append(nombre +" Fallando a la espera de reparacion\n")
            time.sleep(5)


    
def fallar():
    global LSFallas,Semaforo
    pantalla.append( "Comienzo de fallas \n")
    while True:
        time.sleep(random.randint(5,20))
        if random.randint(0,5) == 3:
            x= random.randint(0,18)
            s= Falla("Fallando","Random",True)
            LSFallas[x][1].append(s)
            pantalla.append( "Aplicando falla a "+  LSFallas[x][0]+ " \n")
            Semaforo+=1
            
        
def maquina(nombre,mantenimiento,ins):
	global Semaforo, maximo, Reponer, LSInsumo,LMant,LSFallas
	maquina=Maquina(mantenimiento,nombre)
        Fa=[nombre,[],0]
        LSFallas.append(Fa)
        fallouso=0
        pantalla.append("Maquina "+nombre+ " En Marcha\n")
	while True:
                maquina.marcha()
                if maquina.autochek():
                    m=[nombre,maquina.horas,mantenimiento,0]
                    LMant.append(m)
                    pantalla.append("Maquina "+nombre+ " Necesita Mantenimiento\n")
                    if random.randint(0,7) == 4:
                        Fa[1]= Falla("FALLA USO","No efectuar manteninto",True)
                        Semaforo += 1

		if not Fa[1]==[]:
                    while not Fa[1]==[]:
                        time.sleep(random.randint(1,5))
                        for t in Fa[1]:
                            pantalla.append("Maquina "+nombre+ " esperando reparacion tipo de falla "+t[0]+" por "+t[1]+"\n")
                        time.sleep(random.randint(1,5))
                else:
                    for i in ins:
                        for x in LSInsumo:#zona critica
                            if x[0]==i[0] and x[3]== 0:
                                x[3]=1 # me apodero del insumo
                                for t in LSFallas:
                                    if t[0]==x[0] and t[1]==[]:
                                        break
                                    else:
                                        while not t[1]==[]:
                                            pantalla.append(nombre+" Esperando a que se repare el insumo "+ t[0])
                                            time.sleep(5)
                                        break
                                if x[1]<i[1]:
                                    Reponer.append(x)
                                    while x[1]<i[1]:
                                        time.sleep(random.randint(1,5))
                                        pantalla.append("Maquina "+nombre+" esperando a que se reponga el insumo "+x[0]+"\n")
                                        time.sleep(random.randint(10,15))
                                x=maquina.Consumir(x,i[1])
                                time.sleep(random.randint(1,10))
                                pantalla.append("Maquina "+nombre +" consumio "+str(i[1])+ " Unidades de "+x[0]+ " quedan "+str(x[1])+"\n")
                                
                                x[3]=0
                        
                        


