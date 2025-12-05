import os

def cierre_dia(dia):
    if os.stat("albergues.csv").st_size == 0:
        print("Vacío")
        return -1
    # Leer y actualizar los datos de albergues
    try:
        with open("albergues.csv", "r") as ar:
            lineas = ar.readlines()
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
        return
    
    dia += 1  # Incrementamos el dia

    # Actualizamos el archivo de dias
    try:
        with open("dias.txt", "w") as ar:
            ar.write(str(dia))
    except FileNotFoundError:
        print("El archivo 'dias.txt' no existe.")
        return

    encabezado = lineas[0].strip()
    datos = lineas[1:]
    datos_actualizados = []

    for linea in datos:
        fila = linea.strip().split(", ")
        nombre = fila[0]
        cant_personas = int(fila[5])
        cant_medicamentos = float(fila[7])

        # Calcular el consumo diario de medicamentos
        consumo_diario = (1 / 10) * cant_personas
        nueva_cantidad_medicamentos = max(0, cant_medicamentos - consumo_diario)

        # Actualizar la fila con la nueva cantidad de medicamentos
        fila[7] = f"{nueva_cantidad_medicamentos:.2f}"  # Formato con dos decimales
        datos_actualizados.append(", ".join(fila))

    # Guardar los datos actualizados en el archivo CSV
    try:
        with open("albergues.csv", "w") as ar:
            ar.write(encabezado+"\n")  # Escribir el encabezado
            for line in datos_actualizados:
                ar.writelines([line + "\n"])  # Escribir datos actualizados
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
        return

    print(f"Dia {dia} actualizado. Inventario de medicamentos ajustado.")
    return dia
