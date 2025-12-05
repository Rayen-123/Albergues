from tabulate import tabulate #nota si no les funciona coloquen esto en terminal:  pip3 install tabulate

def crear_predicciones(dia):
    try:
        with open("albergues.csv", "r") as ar:
            lineas = ar.readlines()
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
        return

    encabezado = lineas[0].strip().split(", ")
    datos = []
    # Recorremos cada linea del archivo, omitiendo la primera (encabezado)
    for line in lineas[1:]:
        elementos = line.strip().split(", ")
        datos.append(elementos)

    proyecciones = []
    for fila in datos:
        nombre = fila[0]
        lat = fila[1]
        lon = fila[2]
        cant_personas = int(fila[5])
        cant_medicamentos = float(fila[7])

        consumo_diario = (1 / 10) * cant_personas
        existencias_diarias = []
        for dia in range(1, 8): # Iteramos para calcular las existencias para cada dia
            # Calculamos las existencias restantes para el dia actual
            existencias = max(0, cant_medicamentos - consumo_diario * dia)
            existencias_diarias.append(existencias)

        proyecciones.append([nombre, lat, lon] + existencias_diarias)

    # Imprimir tabla usando tabulate
    print(tabulate(proyecciones, headers=encabezado))
    return proyecciones