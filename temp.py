# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal para el proyecto de astrofísica.
"""

from PIL import Image, ImageFilter, ImageStat
import numpy
import imageio
from scipy import ndimage

im = imageio.imread('sol1.jpg')
im = im.astype('int32')
dx = ndimage.sobel(im, 1)  # horizontal derivative
dy = ndimage.sobel(im, 0)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
mag=mag.astype(numpy.uint8)
imageio.imwrite('sobel.jpg', mag)

sol1=Image.open("sol1.jpg")  
sol1c=sol1.copy() #Para no modificar la imagen original
sol1min=sol1c.filter(ImageFilter.MinFilter) #De una matriz 3x3 toma el valor más bajo
#bordes=sol1c.filter(ImageFilter.MedianFilter)
#bordes=bordes.filter(ImageFilter.RankFilter(3,8))
#bordes=bordes.filter(ImageFilter.SHARPEN)
sol1p=sol1.load()
ancho, alto=sol1.size

#============================================================================#
#============================================================================#
#=====================OBTENCIÓN DEL RANGO A ESTUDIAR=========================#
#============================================================================#
#============================================================================#

lista1si=[]
lista1sj=[]
lista1ii=[]
lista1ij=[]
lista2ii=[]
lista2ij=[]
lista2ia=[]
lista2di=[]
lista2dj=[]
lista2da=[]
"""
#Busca el promedio de toda la imagen
colores=sol1.getcolors()
suma=0
cuenta=0
for i in range(len(colores)):
    mult=colores[i][0]*colores[i][1] #Multiplica la cantidad de pixeles por el color
    cuenta=colores[i][0]+cuenta #Suma estos valores multiplicados
    suma=suma+mult #Cuenta los pixeles
umbral=int(suma/cuenta) #Se toma el promedio como umbral
"""
umbral=0
#Decide el rango en el cual se encuentra el sol
#Extremo superior
for j in range(ancho):
    for i in range(256):
        b=sol1min.getpixel((i,j))
        if b>umbral:
            lista1si.insert(len(lista1si),i)
            lista1sj.insert(len(lista1sj),j)
            break
    if b>umbral:
        break
#Extremo inferior
for j in range(ancho)[::-1]:
    for i in range(256,ancho)[::-1]: #Se define así para evitar conflicto con los créditos
        b=sol1min.getpixel((i,j))
        if b>umbral:
            lista1ii.insert(len(lista1ii),i)
            lista1ij.insert(len(lista1ij),j)
            break
    if b>umbral:
        break
#Extremo izquierdo
for j in range(lista1sj[0], lista1ij[0]):
    for i in range(ancho):
        #if pixelmap[i,j]!=(0,0,0):
        #    listai.insert(len(listai),i)
        #    listaj.insert(len(listai),j)
        #    break        
        a=sol1min.getpixel((i,j))
        if a>umbral:
            lista2ii.insert(len(lista2ii),i)
            lista2ij.insert(len(lista2ij),j)
            lista2ia.insert(len(lista2ia),a)
            sol1p[i,j]=(255)
            break
#Extremo derecho
for j in range(lista1sj[0], lista1ij[0]):
    for i in range(ancho)[::-1]:
        #if pixelmap[i,j]!=(0,0,0):
        #    listai.insert(len(listai),i)
        #    listaj.insert(len(listai),j)
        #    break        
        a=sol1min.getpixel((i,j))
        if a>umbral:
            lista2di.insert(len(lista2di),i)
            lista2dj.insert(len(lista2dj),j)
            lista2da.insert(len(lista2da),a)
            sol1p[i,j]=(255)
            break
        
#============================================================================#
#============================================================================#
#======================ESTUDIANDO EL SOL EN EL RANGO=========================#
#============================================================================#
#============================================================================#
#Declaro las nuevas listas
listava=[]
listavai=[]
listavaj=[]
#Analiza dentro del rango
#Convierte los pixeles con valor mayor al umbral en pixeles negros
#Esto permite usar crop y bbox para delimitar las regiones.
sobel=Image.open("sobel.jpg")
#sobel=sobel.filter(ImageFilter.MedianFilter)

for i in range(0,lista1ij[0]-lista1sj[0]):
    listava.insert(i,[])
    for j in range(lista2ii[i]+1,lista2di[i]-1):
        aa=sobel.getpixel((j,i+lista1sj[0]))
        if aa>umbral:
            listava[i].insert(len(listava[i]),aa)
            listavai.insert(len(listavai),i)
            listavaj.insert(len(listavaj),j)
           #sol1p[j,i+lista1sj[0]]=(0)

mag.Stat
#sobelp=sobel.load()
#sobelp[89,209]=(255)
#sobel.show()
#sobel=numpy.asarray(sobel)

#sol1min.show()
#bordes.show()
#sol1.show()

        
        
        
        








        
        
        
        
        
        
        
        
        
        