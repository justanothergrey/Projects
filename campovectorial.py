from vpython import *
#Web VPython 3.2


"""
Creado por Andrea Morales Rodriguez y Hector Mejia-Diaz


Queremos dibujar el campo vectorial A = (x,y,-z)

Cuidado: el problema queda definido intercambiando a "y" y "z" porque para 
vpython el eje x es positivo a la derecha, el y hacia aarriba y el z saliendo 
de la pantalla. De esta manera la geometria corresponde a la que usamos en
el pizarron.
"""


# dibujamos el plano XY (que en vpython es en realidad XZ) para fines de visualizacion
planoXY = mybox = box(pos=vector(0,0,0),length=30, height=0, width=30,opacity=0.8)


# dibujamos nuestro cilindro
cilindro = cylinder(pos=vector(0,0,0),axis=vector(0,10,0), radius=5, color=color.cyan,opacity=0.8)


# agregamos las "flechas" de campo electrico
for x in range(-10,10,2):
    for y in range(-6,20,2):
        for z in range(-10,10,2):
            norma = sqrt(x*x+y*y+z*z)                             # para que las flechas queden del mismo tamano
            arrow(radius=0.1,shaftwidth=0.1,pos=vector(x,y,z),    # estas seran las lineas de campo
            axis=vector(x/norma,y/norma,-z/norma),round=True)
