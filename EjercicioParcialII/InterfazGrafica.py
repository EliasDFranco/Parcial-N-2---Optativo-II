import tkinter as tk

window = tk.Tk()
window.title("Intefaz Gráfica de Elias D. Franco Duarte")
window.geometry("600x600")

nombreLabel = tk.Label(window, text="Ingrese su nombre completo por favor!")
nombreLabel.pack()
nombre = tk.Entry(window, font=("Arial", 12))
nombre.insert(0, "")
nombre.pack()

correoLabel = tk.Label(window, text="Ingrese su correo eléctronico por favor!!")
correoLabel.pack()
correo = tk.Entry(window, font=("Arial", 12))
correo.insert(0, "")
correo.pack()

comentarioLabel = tk.Label(window, text="Comente acerca sobre el parcial 3!")
comentarioLabel.pack()
comentarioBox = tk.Text(window, height= 5, width= 80)
comentarioBox.pack()

menuLabel = tk.Label(window, text="Menú Selección de Servicio")
menuLabel.pack()
opciones = ["Internet", "Telefonía", "TV", "Otros servicios..."]
seleccionOpciones = tk.StringVar(value=opciones[0])
menu = tk.OptionMenu(window, seleccionOpciones, *opciones)
menu.pack()

varAceptar= tk.IntVar()
aceptaTerminos = tk.Checkbutton(window, text="Aceptar los términos y condiciones...", variable=varAceptar)
aceptaTerminos.pack()

labelResultados = tk.Label(window, text="",height=10, width=100, justify="center")
labelResultados.pack()

def mostrarResultados():
    name = nombre.get()
    email = correo.get()
    comentario = comentarioBox.get("1.0", tk.END).strip()
    servicios = seleccionOpciones.get()
    condicionesAceptar = 'SI' if varAceptar.get() == 1 else 'NO'
    
    msj = (
        f"Hola!! {name}\n"
        f"Tu correo electrónico es: {email}\n"
        f"Tu comentario es: {comentario}\n"
        f"Has seleccionado el servicio: {servicios}\n"
        f"Aceptó los términos: {condicionesAceptar}"
    )
    labelResultados.config(text=msj)
    
def limpiarTexto():
    nombre.delete(0, tk.END)
    correo.delete(0, tk.END)
    comentarioBox.delete("1.0", tk.END)
    seleccionOpciones.set(opciones[0])
    varAceptar.set(0)
    
    labelResultados.config(text="")

botonMostrarResultados = tk.Button(window, text="Mostrar los resultados impresos: ", command=mostrarResultados, bg="green", fg="whitesmoke")
botonMostrarResultados.pack()

botonLimpiar = tk.Button(window, text="Limpiar todo", command=limpiarTexto )
botonLimpiar.pack()

botonSalir = tk.Button(window, text="Salir del programa",  command=window.destroy, bg="red", fg="whitesmoke")
botonSalir.pack()
window.mainloop()