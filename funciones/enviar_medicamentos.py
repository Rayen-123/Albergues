import os

def enviar_medicamentos(num, albergue, cantMedic, Albergues, diaAct):
    if num <= 0 or cantMedic <= 0:
        print("El número de vuelo y la cantidad de medicamentos deben ser positivos.")
        return

    if albergue not in Albergues["Nombre"]:
        print(f"Error: el albergue '{albergue}' no existe.")
        return

    # Cargar albergues desde archivo
    try:
        with open("albergues.csv", "r") as ar:
            lineas = ar.readlines()
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
        return
    #informar a usuario
    """
    Envío número 327, día 21, destino: A, cantidad: 100 
    A pasa de 10/40 a 40/40 
    B pasa de 50/70 a 70/70 
    D pasa de 70/90 a 90/90 
    Se reporta la pérdida de 30 paquetes de medicamentos
    """    
    print(f"Envio numero: {num}, dia: {diaAct}, destino: {albergue}, cantidad: {cantMedic}")

    encabezado = lineas[0].strip().split(", ")
    datos = []
    # Recorremos cada linea del archivo, omitiendo la primera (encabezado)
    envio = cantMedic
    perdida = -1
    for line in lineas[1:]:
        elementos = line.strip().split(", ")
        datos.append(elementos) #matriz
    for lista in datos:
        #lista[6] = capacidad
        #lista[7] = cantidad
        estado = float(lista[6]) - float(lista[7])
        if estado != 0 and envio != 0:
            if envio < estado:
                envio = 0
                print(f"{lista[0]} pasa de {lista[7]}/{lista[6]} a {float(lista[7]) + envio}/{lista[6]}")
                lista[7] = str(float(lista[7]) + envio)
            else: 
                envio = envio - estado
                print(f"{lista[0]} pasa de {lista[7]}/{lista[6]} a {lista[6]}/{lista[6]}")
                lista[7] = lista[6] #guardar nueva cantidad de medicamentos
    
    perdida = envio
    print(f"Se reporta la perdida de {perdida} paquetes de medicamentos")
    if perdida == 0 or envio <= 0:
        print("No se reportó ninguna perdida")

    # Guardar cambios
    try:
        with open("albergues.csv", "w") as ar:
            ar.write(", ".join(encabezado) + "\n")
            for fila in datos:
                ar.write(", ".join(fila) + "\n")
    except FileNotFoundError:
        print("Error al guardar los cambios.")
        return

    try:
        # Verificar si el archivo existe antes de abrir en modo 'a'
        archivo_envios_existe = os.path.exists("envíos.csv")
        with open("envíos.csv", "a") as ar:
            if not archivo_envios_existe:
                # Si el archivo no existe, escribir el encabezado
                ar.write("#NumeroEnvio, Albergue, CantMedicamentos, Perdidos\n")
            # Escribir el registro del envío
            ar.write(f"{num}, {albergue}, {cantMedic}, {perdida}\n")
    except Exception as e:
        print(f"Error al escribir en 'envíos.csv': {e}")
