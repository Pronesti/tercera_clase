#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:49:19 2019

@author: diego
"""

import random

res = random.randint(1,3)
def tirar_dado():
    return random.randint(1,6)

def tirar_varios_dados(cuantos):
    resultado =[]
    i=0
    while i <= cuantos:
        resultado.append(tirar_dado())
        i+=1
    return resultado

def tirar_hasta_sacar_todo():
    tirada=[]
    while estan_los_seis(tirada):
        tirada.append(tirar_dado())
    return tirada

def estan_los_seis(lista):
    i=0
    while i < len(lista):
        lista.index

def sumar(resultados):
    i=0
    suma=0
    while i < len(resultados):
        suma += resultados[i]
        i+=1
    return suma

def calcular_media(resultados):
    return (sumar(resultados) / len(resultados))
    

resultados = (12,11,13,15,8,14,30,16,14,8)
print(calcular_media(resultados))
print(calcular_media(tirar_varios_dados(50)))