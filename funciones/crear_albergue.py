import csv
import tkinter as tk
from tkinter import messagebox as msgbox

def crear_albergue(nomb, coordX_str, coordY_str, cantP_str, MaxP_str,cantMedic_str, MaxM_str, dia):

    if nomb=='' or nomb==' ':
        msgbox.showinfo('ERROR!', "Ingrese un nombre para el albergue")
        return

    if coordX_str=='':
        coordX=0.0
    else:
        coordX = float(coordX_str)
    if coordY_str=='':
        coordY=0.0
    else:
        coordY = float(coordY_str)

    cantP = int(cantP_str)
    MaxP = int(MaxP_str)
    cantMedic = int(cantMedic_str)
    MaxM = int(MaxM_str)

    try:
        with open("albergues.csv", "r") as ar:
            if any(nomb == line.split(',')[0] for line in ar):  # Revisa si el nombre ya está en el archivo
                msgbox.showinfo('ERROR!', f'El archivo {nomb} ya existe.')
                return
    except FileNotFoundError:
        pass 

    if not (-56 <= coordY <= -17.5):
        msgbox.showinfo('ERROR!', f'Coordenadas {coordY} fuera del rango permitido (-56 <= coordY <= -17.5).')
        return
    if not (-75 <= coordX <= -66):
        msgbox.showinfo('ERROR!', f'Coordenadas {coordX} fuera del rango permitido (-75 <= coordX <= -66).')
        return

    if cantP > MaxP:
        msgbox.showinfo('ERROR!', f'Número de personas actual ({cantP}) mayor al máximo permitido ({MaxP}).')
        return
    if cantMedic > MaxM:
        msgbox.showinfo('ERROR!', f'Número de medicamentos actual ({cantMedic}) mayor al máximo permitido ({MaxM}).')
        return

    if cantP < 0 or cantMedic < 0 or MaxP < 0 or MaxM < 0:
        msgbox.showinfo('ERROR!', 'Las cantidades deben ser números enteros positivos.')
        return

    campos = [nomb, coordY, coordX, dia, MaxP, cantP, MaxM, cantMedic]
    
    try:
        with open("albergues.csv", "a") as ar:
            ar.write(", ".join(map(str, campos)) + "\n")
    except FileNotFoundError:
        with open("albergues.csv", "w") as ar:
            ar.write("#Nombre, Lat, Long, Dia_Creacion, Cap_Pers, Cant_Pers, Cap_Med, Cant_Med\n")
            ar.write(", ".join(map(str, campos)) + "\n")

    msgbox.showinfo(f'Albergue {nomb} agregado correctamente.')