import funciones.crear_albergue as crear_albergue
import funciones.crear_albergue as CRE_A
import funciones.modificar_albergue as M_A
import funciones.crear_predicciones as C_P
import funciones.cierre_dia as C_D
import funciones.enviar_medicamentos as E_M
import funciones.cargar_albergues as CARG_A

import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox as msgbox
from io import StringIO
import sys

datos=["Alberge","cordenadas X", "cordenadas Y", "Cantidad de personas","Max. personas", "MedicActual", "MedicMax"]

def ReiniciarArchivos(root):
    with open('envios.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        fieldnames = ['num_vuelo', 'destino', 'carga', 'dia']
        writer.writerow(fieldnames)
    with open('albergues.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        fieldnames = ['Nombre', 'lat', 'long', 'dia_creacion', 'cap_pers', 'cant_pers', 'cap_med', 'cant_med']
        writer.writerow(fieldnames)

    dias = open('dias.txt','w')
    dias.write("0 \n ")
    dias.close()
    
    pantallaDefinitiva(root)

def pantallaDefinitiva(root):
    try:
        with open("albergues.csv","r") as ar:
            pass
    except FileNotFoundError:
        with open("albergues.csv","w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            fieldnames = ['Nombre', 'lat', 'long', 'dia_creacion', 'cap_pers', 'cant_pers', 'cap_med', 'cant_med']
            writer.writerow(fieldnames)

    try:
        with open("envios.csv","r") as ar:
            pass
    except FileNotFoundError:
        with open('envios.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            fieldnames = ['num_vuelo', 'destino', 'carga', 'dia']
            writer.writerow(fieldnames)
        
    try: 
        with open("dias.txt","r") as ar:
            diaAct = int(ar.read())
    except FileNotFoundError:
        with open("dias.txt","x") as ar:
            diaAct = 0
            ar.write(str(diaAct))
    
    def actualizar_albergues(listbox1):

        # Borrar todos los elementos del Listbox antes de agregar los nuevos
        listbox1.delete(0, tk.END)  # Esto debe borrar el Listbox

        
            # Leer los albergues del archivo y cargarlos en el listbox
        with open('albergues.csv', 'r') as archivo:
            listaalbergues = csv.reader(archivo)
            root.update() 
                # Iterar sobre las filas del archivo
            for row in listaalbergues:
                if row[0] != "Nombre":  # Ignorar la cabecera
                    listbox1.insert(tk.END, row[0])
        
    
    def crearalbergue(listbox, listbox2, dia):
        
        root = tk.Tk()
        root.geometry('250x310')
        root.title("Crear Albergues")
        tk.Label(root,text=datos[0], padx=30).pack()
        nombre = tk.Entry(root)
        nombre.pack()
        tk.Label(root,text=datos[1], padx=30).pack()
        cordenadasX = tk.Entry(root)
        cordenadasX.pack()
        tk.Label(root,text=datos[2], padx=30).pack()
        cordenadasY = tk.Entry(root)
        cordenadasY.pack()
        tk.Label(root,text=datos[3], padx=30).pack()
        cantPersonas = tk.Entry(root)
        cantPersonas.pack()
        tk.Label(root,text=datos[4], padx=30).pack()
        MaxPersonas = tk.Entry(root)
        MaxPersonas.pack()
        tk.Label(root,text=datos[5], padx=30).pack()
        MedicActual = tk.Entry(root)
        MedicActual.pack()
        tk.Label(root,text=datos[6], padx=30).pack()
        MedicMax = tk.Entry(root)
        MedicMax.pack()
        
        
    
        

        boton = tk.Button(root, text="Crea Albergue",
                          command=lambda: [CRE_A.crear_albergue(nombre.get(), cordenadasX.get(), cordenadasY.get(),
                                                                         cantPersonas.get() ,
                                                                         MaxPersonas.get(), MedicActual.get(), MedicMax.get(), dia),
                                           actualizar_albergues(listbox),actualizar_albergues(listbox2)])
        boton.pack()  

    def cierredia(diaAct):
        resultado = C_D.cierre_dia(diaAct)

        if resultado > -1:
            diaAct = resultado
            ventana = tk.Toplevel()
            ventana.title("Cerrar dia")
        else:
            ventana = tk.Toplevel()
            ventana.title("dia")
            tk.Label(ventana, text="Error, no existen albergues", padx=100, pady=60).pack()
    def actualizar(ventana, row):
        ventana.destroy()
        info_un_albergue (row)
        
    def info_un_albergue (row):
        def handler_btn(delta):
            valor = int(lbl_valor["text"])
            lbl_valor["text"] = str(valor + delta)
        #Nombre,lat,long,dia_creacion,cap_pers,cant_pers,cap_med,cant_med
        ventana = tk.Toplevel()
        ventana.title(row[0])
        cantPersonas= int(row[5])
        tk.Label(ventana, text=("Latitud ", row[1]), width=50, height=2,bg = 'SkyBlue2').grid(columnspan=4)
        tk.Label(ventana, text=("Longitud ", row[2]), width=50, height=2,bg = 'SkyBlue2').grid(columnspan=4)
        tk.Label(ventana, text=("Dia creacion ", row[3]), width=50, height=2,bg = 'SkyBlue2').grid(columnspan=4)
        tk.Label(ventana, text=("Capacidad máxima de personas: ", row[4]), width=50,height=2, bg = 'SkyBlue2').grid(columnspan=4)   
        tk.Label(ventana, text=("Cantidad inicial de personas : ", row[5]), width=50,height=2, bg = 'SkyBlue2').grid(columnspan=4)
        tk.Button(ventana, text=("-"), width=3, height=1, bg = 'DeepSkyBlue4',relief= tk.RAISED, command= lambda cantPersonas = cantPersonas-1: [
                                                                                                                    handler_btn(-1)]).grid(column=1,row=5)
        lbl_valor= tk.Label(ventana, text=(cantPersonas), width=10, height=2,bg = 'SkyBlue2')
        lbl_valor.grid(column=2,row=5)
        tk.Button(ventana, text=("+"), width=3, height=1, bg = 'DeepSkyBlue4',relief= tk.RAISED, command= lambda cantPersonas = cantPersonas: [
                                                                                                         handler_btn(1)]).grid(column=3,row=5)
        tk.Label(ventana, text=("Capacidad máxima de medicamentos: ", row[6]), width=50,height=2, bg = 'SkyBlue2').grid(columnspan=4)
        tk.Label(ventana, text=("Cantidad actual de medicamentos: ", row[7]),width=50, height=2, bg = 'SkyBlue2').grid(columnspan=4)
        tk.Button(ventana, text=("Guardar Cambios"), width=50, height=1, bg = 'DeepSkyBlue4', relief= tk.RAISED, command= lambda cantPersonas = cantPersonas: [M_A.modificar_Albergue(row[0],int(lbl_valor["text"])),
                                                                                                                    ]).grid(columnspan=4)   
    def revisar_albergue():
        seleccionado = listbox1.curselection()  
        if seleccionado:
            index = seleccionado[0]
    
            with open('albergues.csv', 'r') as archivo:
                listaalbergues = list(csv.reader(archivo))
                row = listaalbergues[index + 1]
                info_un_albergue(row)

    
    envios = open('envios.csv','a')
    envios.close()
    albergues = open('albergues.csv','a')
    albergues.close()
    
    root.destroy()
    root = tk.Tk()
    root.configure(background='DarkSeaGreen3')
        
    def informacionPredicciones(diaAct):
        # Encabezados para la tabla
        encabezado_fijo = ["Albergue", "Latitud", "Longitud"]
        encabezado_dias = [] 
        for i in range(diaAct, diaAct + 7):
            encabezado_dias.append(f"Dia {i}")
        encabezado = encabezado_fijo + encabezado_dias
        ventana = tk.Toplevel()
        ventana.title("Proyecciones")

        datos = C_P.crear_predicciones(diaAct)

        # Crear un Treeview
        tree = ttk.Treeview(ventana, columns=encabezado, show="headings")
        tree.grid(row=0, column=0, sticky="nsew")

        # Configurar encabezados
        for col in encabezado:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        # Agregar filas
        for fila in datos:
            tree.insert("", "end", values=fila)

        # Configurar el scroll
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        ventana.mainloop()

    def enviar_medicamentos_gui(diaAct):
        def procesar_envio():
            try:
                num = int(entry_num.get())
                albergue = entry_albergue.get().strip()
                cantMedic = int(entry_cant_medic.get())
                Albergues = {"Nombre": [albergue]}  # Esto debería reemplazarse con la lectura real de los albergues

                # Redirigir stdout para capturar el texto de salida
                buffer = StringIO()
                sys.stdout = buffer

                E_M.enviar_medicamentos(num, albergue, cantMedic, Albergues, diaAct)

                # Restaurar stdout
                sys.stdout = sys.__stdout__

                # Obtener el resultado capturado y mostrarlo en un cuadro de mensaje
                resultado = buffer.getvalue()
                msgbox.showinfo("Resultado del Envío", resultado)
                ventana.destroy()
            except ValueError:
                msgbox.showerror("Error", "Por favor, introduce valores válidos en todos los campos.")
            except Exception as e:
                msgbox.showerror("Error", f"Ha ocurrido un error: {e}")
            finally:
                # Restaurar stdout en caso de error
                sys.stdout = sys.__stdout__

        # Crear ventana emergente
        ventana = tk.Toplevel()
        ventana.title("Enviar Medicamentos")
        ventana.geometry("400x300")

        # Campos para los datos de envío
        tk.Label(ventana, text="Número de Envío:").pack(pady=5)
        entry_num = tk.Entry(ventana)
        entry_num.pack(pady=5)

        tk.Label(ventana, text="Albergue de destino:").pack(pady=5)
        entry_albergue = tk.Entry(ventana)
        entry_albergue.pack(pady=5)

        tk.Label(ventana, text="Cantidad de Medicamentos:").pack(pady=5)
        entry_cant_medic = tk.Entry(ventana)
        entry_cant_medic.pack(pady=5)

        # Botón para procesar el envío
        boton_procesar = tk.Button(ventana, text="Enviar", command=procesar_envio, bg="green", fg="white")
        boton_procesar.pack(pady=20)

        ventana.mainloop()


    # Crear el scrollbar
    scroll = tk.Scrollbar(root, orient=tk.VERTICAL)

    # Crear el listbox para datos
    listbox1 = tk.Listbox(root, selectmode=tk.SINGLE, yscrollcommand=scroll.set, bg='SkyBlue2')
    listbox1.grid(row=1, column=2, sticky='NSWE')
    
    # Crear el listbox para predicciones
    listbox2 = tk.Listbox(root, selectmode=tk.SINGLE, yscrollcommand=scroll.set, bg='thistle2')
    listbox2.grid(row=1, column=0, sticky='NSWE')

    root.columnconfigure([0, 1, 2] , weight = 1,minsize=40)
    root.rowconfigure([0, 1, 2], weight = 1)
    
    root.title('Pantalla Inicial')

    #Predicciones
    PREDICCIONES = tk.Label(root, relief = tk.RAISED, text = 'Predicciones', bg = 'orchid4', width = 8, height = 2, )
    PREDICCIONES.grid(row = 0, column = 0,rowspan = 1, sticky="new")

    #Mapa
    MAPA = tk.Label(root, relief = tk.RAISED, text = 'Mapa', bg = 'orange', width = 40, height = 2)
    MAPA.grid(row = 0, column = 1, rowspan = 1, sticky="new")
    v=tk.Label(root, text='Dia actual: '+ str(diaAct), bg = 'DarkSeaGreen3').grid(row = 2, column = 1, rowspan = 1)
    
    #Alberges
    ALBERGUES = tk.Label(root, relief = tk.RAISED, text = 'Albergues', bg = 'DeepSkyBlue4', width = 20, height = 2)
    ALBERGUES.grid(row = 0, column = 2, rowspan =1,sticky="new")

    actualizar_albergues(listbox1)
    boton_selec = tk.Button(root, text="Revisar albergue", bg = 'DeepSkyBlue4',command= revisar_albergue)
    boton_selec.grid(row=2, column=2)
    
    botoncrear = tk.Button(root, text="Nuevo albergue",bg = 'DeepSkyBlue4', command= lambda: crearalbergue(listbox1, listbox2, diaAct))
    botoncrear.grid(row=3, column=2)

    actualizar_albergues(listbox2)
    boton_pro = tk.Button(root, text="Proyecccion",bg = 'orchid4', command= lambda: informacionPredicciones(diaAct))
    boton_pro.grid(row=3, column=0)

    boton_envi = tk.Button(root, text="Envios",bg = 'orchid4', command= lambda: enviar_medicamentos_gui(diaAct))
    boton_envi.grid(row=2, column=0)

    boton_dia = tk.Button(root, text="Cierre del Día", bg = 'firebrick3' ,command= lambda: [cierredia(diaAct),pantallaDefinitiva(root)])
    boton_dia.grid(row=3, column=1)
            
    #imagen de mapa
    image = tk.PhotoImage(file="mapa3.png")# Cargar imagen del disco.
    mapa = tk.Label(root, relief = tk.RAISED,image=image)# Insertarla en una etiqueta.
    mapa.grid(row = 1, column = 1,rowspan =1)

    root.mainloop()


def pantallaInicial():
    root = tk.Tk() # crea una nueva ventana
    root.title('Pantalla Inicial')
    etiqueta = tk.Label(root, text = 'Bienvenido al Programa de superviviencia ante emergencias')
    etiqueta.pack() # posiciona etiqueta en la ventana (con pack)
    etiqueta2 = tk.Label(root, text = '¿Desea continuar con la partida anterior o iniciar un nuevo programa?')
    etiqueta2.pack() # posiciona etiqueta 2 en la ventana 
    frame_opciones = tk.Frame(root, relief = tk.RAISED, borderwidth = 1) #crea frame
    botonContinuar = tk.Button(frame_opciones, text = "Continuar partida anterior", pady = 10, padx = 30,
                               command=lambda:pantallaDefinitiva(root))
    #crea boton en frame
    botonReiniciar = tk.Button(frame_opciones, text = "Reiniciar programa", pady = 10, padx = 30, bg = 'orange red',
                               command=lambda:ReiniciarArchivos(root))
    #crea boton en frame
    botonContinuar.grid(row = 1, column = 1)
    #ubica boton en grilla
    botonReiniciar.grid(row = 1, column = 2)
    #ubica boton en grilla
    frame_opciones.pack() #ubica grilla
    
    root.mainloop() # loop infinito que espera eventos (event loop)
    
def main():
    pantallaInicial()
    
if __name__ == "__main__":
    main()
