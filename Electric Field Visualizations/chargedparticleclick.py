
#En esta visualizacion proyectamos como se veria el campo electrico debido a una particula cargada, cuya carga esta 
#indicada en Coulomb. Nota: En cargas muy grandes o cercanas a la carga, la flecha aparecería muy grande.

#Author(s): Hector Mejia & Andrea MR

from vpython import *
#Definimos la carga puntual
def E(rq,ro,q):
  r=ro-rq
  k=9e9
  return(k*q*norm(r)/mag(r)**2)
k=9e9  
ro1=vector(0.05,0,0)
rq1=vector(0,0,0)
q1=3e-9

#Dibujamos el objeto
qq1=sphere(pos=rq1, radius=0.01, color=color.red)
placeholder=sphere(pos=vector(0.09,0,0),radius=0.0001)
Escala=0.02/1e4

#Definimos la funcion que al hacer click, nos arrojará como se ve el campo en ese punto.
def verCampo(evt):
    loc = evt.pos
    rt=loc-rq1
    Et=k*q1*norm(rt)/mag(rt)**2
    arrow(pos=loc, axis=Escala*Et, color=color.white)

scene.bind('click', verCampo)