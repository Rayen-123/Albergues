import tkinter as tk
from tkinter import messagebox as msgbox
def modificar_Albergue(nomb, cant, archivo="albergues.csv"):
    if cant < 0:
        print("Error: la cantidad debe ser un numero positivo.")
        msgbox.showinfo('ERROR!',"La cantidad debe ser un numero positivo. Archivo no modificado.")
        return

    # Leer el archivo completo en memoria
    try:
        with open("albergues.csv", "r") as ar:
            lineas = ar.readlines()
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
        return

    encabezado = lineas[0]
    datos = lineas[1:]
    albergue_encontrado = False

    # Actualizar la cantidad de personas en los datos
    for i in range(len(datos)):
        fila = datos[i].strip().split(", ")  # Dividir cada linea por comas y espacios
        if fila[0] == nomb:  # Buscar por nombre del albergue
            albergue_encontrado = True
            capacidad_maxima = int(fila[4])
            if cant > capacidad_maxima:
                print(f"Error: la nueva cantidad ({cant}) excede la capacidad maxima ({capacidad_maxima}).")
                msgbox.showinfo('ERROR!', f"La nueva cantidad ({cant}) excede la capacidad maxima ({capacidad_maxima}). Archivo no modificado.")
                return
            fila[5] = str(cant)  # Actualizar la cantidad actual de personas
            datos[i] = ", ".join(fila) + "\n"
            msgbox.showinfo('Guardado', f"Nueva cantidad ({cant}). Archivo modificado.")
            break

    if not albergue_encontrado:
        print(f"Error: no se encontro el albergue '{nomb}'.")
        return

    # Guardar los datos actualizados en el archivo
    try: 
        with open("albergues.csv", "w") as ar:
            ar.write(encabezado)  # Escribir el encabezado
            ar.writelines(datos)  # Escribir las lineas actualizadas
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
        return

    print(f"Albergue '{nomb}' actualizado con exito. Nueva cantidad de personas: {cant}.")