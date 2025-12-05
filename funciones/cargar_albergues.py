def cargar_albergues(): #Para volver a cargar albergues del archivo al diccionario
    Albergues = {
        "Nombre": [],
        "Lat": [],
        "Long": [],
        "Dia_Creacion": [],
        "Cap_Pers": [],
        "Cant_Pers": [],
        "Cap_Med": [],
        "Cant_Med": [],
    }
    try:
        with open("albergues.csv", "r") as ar:
            lineas = ar.readlines()[1:]  # Saltar el encabezado
            for linea in lineas:
                nombre, lat, lon, dia, cap_pers, cant_pers, cap_med, cant_med = linea.strip().split(", ")
                Albergues["Nombre"].append(nombre)
                Albergues["Lat"].append(float(lat))
                Albergues["Long"].append(float(lon))
                Albergues["Dia_Creacion"].append(int(dia))
                Albergues["Cap_Pers"].append(int(cap_pers))
                Albergues["Cant_Pers"].append(int(cant_pers))
                Albergues["Cap_Med"].append(float(cap_med))
                Albergues["Cant_Med"].append(float(cant_med))
    except FileNotFoundError:
        print("El archivo 'albergues.csv' no existe.")
    return Albergues

    
