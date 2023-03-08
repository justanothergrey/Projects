#Visualizing the electric field due to a charged particle inside a gaussian surface
#Author(s): Hector Mejia & Andrea MR

from vpython import *
import numpy as np

#Creamos la escena para visualizar
scene = canvas(title='Campo Electrico', width = 800, height = 600)

#Creamos la particula cargada (En Coulombs)
particula = sphere(radius = 0.1, pos = vector(0,0,0), carga = 1e-6, color = color.yellow)

#Creamos la superficie Gaussiana
superficie_gaussiana = box(size=vector(1,1,1), pos = vector(0,0,0), color = color.white, opacity = 0.2)

#Definimos una funcion para calcular el campo electrico usando ley de Coulomb
def campo_electrico(particula, pos):
    k = 9e9 #Constante de Coulomb en Nm^2/C^2
    r = mag(pos - particula.pos)
    direccion = norm(pos - particula.pos)
    campo = k * particula.carga /r**2 *direccion
    return campo


def mostrar_campo():
    for x in range(-10,11):
        for y in range(-10,11):
            for z in range(-10,11):
                pos = vector(x, y, z)
    if pos != vector(0,0,0):
        campo = campo_electrico(particula, pos)
        arrow(pos=pos, axis=campo, color=color.white)
mostrar_campo()

def mover_particula(evt):
    pos = scene.mouse.pos
    particula.pos = pos
    scene.center = particula.pos
    for obj in scene.objects:
        obj.visible = False
mostrar_campo()

scene.bind('mousedown', mover_particula)

while True:
    rate(30)