#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:29:27 2019

@author: diego
"""

import random
import numpy as np

def crear_album(n):
    i=0
    album = []
    while i < n:
        album.append(0)
        i+=1
    return album

def esta_completo(unAlbum):
    i=0
    while i < len(unAlbum):
        if unAlbum[i] == 0:
            return False
        i+=1
    return True

def comprar_figurita(n):
    return random.randint(0,n)

def comprar_paquete_figuritas(fig_por_paquete, n):
    paquete=[]
    i=0
    while i < fig_por_paquete:
        paquete.append(comprar_figurita(n))
        i+=1
    return paquete

def esta_figurita(figurita, unAlbum):
    if unAlbum[figurita] == 1:
        return True
    return False

def pegar_figurita(figurita, unAlbum):
    unAlbum[figurita] = 1
    return unAlbum

def llenar_album(unAlbum):
    total= len(unAlbum)
    repetidas=[]
    while not(esta_completo(unAlbum)):
        fig = comprar_figurita(total-1)
        if esta_figurita(fig, unAlbum) == True:
            repetidas.append(fig)
        else:
            unAlbum = pegar_figurita(fig, unAlbum)
    print("Figuritas compradas: ", (len(unAlbum)+len(repetidas)))
    return (len(unAlbum)+len(repetidas))

def llenar_varios_albumes(cantidad_albumes, cantidad_figuritas):
    i=0
    lista=[]
    while i < cantidad_albumes:
        lista.append(llenar_album(crear_album(cantidad_figuritas)))
        i+=1
    return lista

def llenar_album_con_paquetes(unAlbum):
    total= len(unAlbum)
    repetidas=[]
    while not(esta_completo(unAlbum)):
        paquete = comprar_paquete_figuritas(5,total-1)
        i=0
        while i < len(paquete):
            fig = paquete[i]
            if esta_figurita(fig, unAlbum) == True:
                repetidas.append(fig)
            else:
                unAlbum = pegar_figurita(fig, unAlbum)
            i+=1
    print("Figuritas compradas: ", (len(unAlbum)+len(repetidas)))
    print("Paquetes comprados: ", (len(unAlbum)+len(repetidas))/5)
    return (len(unAlbum)+len(repetidas))/5

def llenar_varios_albumes_con_paquetes(cantidad_albumes, cantidad_figuritas):
    i=0
    lista=[]
    while i < cantidad_albumes:
        lista.append(llenar_album_con_paquetes(crear_album(cantidad_figuritas)))
        i+=1
    return lista
    
#resultado = llenar_album(crear_album(6))
resultado2 = llenar_varios_albumes_con_paquetes(100,669)
print(np.mean(resultado2))



