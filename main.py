import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def main():
    global root
    root = tk.Tk()
    root.title("Tarea 3")
    titulo = "Elije un juego"
    canvas = tk.Canvas(root, width=512, height=512)
    canvas.pack(fill="both", expand=True)
    logo_juego = Image.open("imagenes/menu.jpeg").resize((512,512))
    logo_juego_photo = ImageTk.PhotoImage(logo_juego)
    canvas.create_image(0, 0, image=logo_juego_photo, anchor="nw")
    canvas.create_text(256, 60, font=("Arial", 40), fill="white", text=titulo)

    botonJuego1 = ttk.Button(root, text="Piedra Papel o Tijera", command=juego1)
    canvas.create_window(256, 200, anchor="center", width="200", window=botonJuego1)

    botonJuego2 = ttk.Button(root, text="Palabras en Inglés", command=juego2)
    canvas.create_window(256, 235, anchor="center", width="200", window=botonJuego2)

    botonJuego3 = ttk.Button(root, text="Adivina el número", command=juego3)
    canvas.create_window(256, 270, anchor="center", width="200", window=botonJuego3)

    root.mainloop()


def juego1():
    root.destroy()
    juego1Pantalla = tk.Tk()
    juego1Pantalla.title("Piedra Papel y Tijera")
    titulo = "Piedra Papel y Tijera"
    label_titulo = tk.Label(text=titulo, font=("Arial", 20))
    label_titulo.pack(padx=20, pady=20)

    # ESTO ES CON RADIOBUTTON
    opcionJugador = tk.IntVar(value=0)  # Como StrinVar pero en entero
    piedra = tk.Radiobutton(
        juego1Pantalla,
        text="Piedra",
        variable=opcionJugador,
        value=0
    )
    piedra.pack()
    papel = tk.Radiobutton(
        juego1Pantalla,
        text="Papel",
        variable=opcionJugador,
        value=1
    )
    papel.pack()
    tijera = tk.Radiobutton(
        juego1Pantalla,
        text="Tijera",
        variable=opcionJugador,
        value=2
    )
    tijera.pack()

    def jugar(opcionJugador):
        opcionMaquina = random.randint(0, 2)
        if opcionJugador.get() == opcionMaquina:
            imprimirResultado.set(f"Máquina eligió lo mismo. Empate")
        elif opcionJugador.get() == 0 and opcionMaquina == 1:
            imprimirResultado.set(f"Máquina elige papel. Jugador Pierde")
        elif opcionJugador.get() == 0 and opcionMaquina == 2:
            imprimirResultado.set(f"Máquina elige tijera. Jugador Gana")
        elif opcionJugador.get() == 1 and opcionMaquina == 0:
            imprimirResultado.set(f"Máquina elige piedra. Jugador Gana")
        elif opcionJugador.get() == 1 and opcionMaquina == 2:
            imprimirResultado.set(f"Máquina elige tijera. Jugador Pierde")
        elif opcionJugador.get() == 2 and opcionMaquina == 0:
            imprimirResultado.set(f"Maquina elige piedra. Jugador Pierde")
        elif opcionJugador.get() == 2 and opcionMaquina == 1:
            imprimirResultado.set(f"Maquina elige papel. Jugador Gana")

    botonJugar = ttk.Button(juego1Pantalla, text="Jugar", command=lambda:jugar(opcionJugador))
    botonJugar.pack()
    imprimirResultado = tk.StringVar()
    etiquetaResultado = tk.Label(juego1Pantalla, textvariable=imprimirResultado)
    etiquetaResultado.pack()

def juego2():
    root.destroy()
    juego2Pantalla = tk.Tk()
    juego2Pantalla.title("Palabras en Inglés")
    palabras = {
        "Car": "Coche",
        "House": "Casa",
        "Laptop": "Portátil",
        "Table": "Mesa",
        "Chair": "Silla",
        "Love": "Amor",
        "Sky": "Cielo",
        "Hair": "Pelo",
        "Red": "Rojo",
        "Blue": "Azul",
        "Green": "Verde",
        "Dog": "Perro",
        "Cat": "Gato",
        "Bear": "Oso",
        "One": "Uno",
        "Ten": "Diez",
        "Mouse": "Ratón",
        "Water": "Agua",
        "Drink": "Beber",
        "Eat": "Comer",
    }
    titulo = "Traduce las palabras al español:"
    label_titulo = tk.Label(text=titulo, font=("Arial", 20))
    label_titulo.pack(padx=20, pady=20)

    respuesta = tk.Entry(juego2Pantalla)
    respuesta.pack()
    resultadoRespuesta = respuesta.get()

    imprimirResultado = tk.StringVar()
    etiquetaResultado = tk.Label(juego2Pantalla, textvariable=imprimirResultado)
    etiquetaResultado.pack()

    imprimirPuntos = tk.StringVar()
    etiquetaPuntos = tk.Label(juego2Pantalla, textvariable=imprimirPuntos)
    etiquetaPuntos.pack()

    imprimirPalabras = tk.StringVar()
    etiquetaPalabras = tk.Label(juego2Pantalla, textvariable=imprimirPalabras)
    etiquetaPalabras.pack()

    def jugar(resultadoRespuesta):
        puntos = 0
        for palabra in range(5):
            palabrasAleatorias = random.choice(list(palabras.keys()))
            imprimirPalabras.set(palabrasAleatorias)
            if resultadoRespuesta == palabras[palabrasAleatorias]:
                imprimirResultado.set(f"Correcto")
                puntos += 1
            else:
                imprimirResultado.set(f"Incorrecto")

        imprimirPuntos.set(f"Tus puntos: {puntos}/5")
    botonJugar = ttk.Button(juego2Pantalla, text="Jugar", command=lambda: jugar(resultadoRespuesta))
    botonJugar.pack()




def juego3():
    root.destroy()
    juego3Pantalla = tk.Tk()
    juego3Pantalla.title("Adivina el Número")
    opcion = tk.Entry(juego3Pantalla)
    opcion.pack()
    numero = random.randint(0, 201)
    print(numero)
    intentos = 3


    def comprobarJuego3():
        nonlocal intentos
        respuesta = opcion.get()
        try:
            respuesta = int(respuesta)
        except ValueError:
            resultado.set("Por favor, introduce un número válido.")
            return
        if intentos > 0 :
            if respuesta > numero:
                intentos -= 1
                resultado.set(f"Incorrecto. Tu número es mayor. Intentos restantes: {intentos}")
            elif respuesta < numero:
                intentos -= 1
                resultado.set(f"Incorrecto. Tu número es menor. Intentos restantes: {intentos}")
            else:
                resultado.set(f"¡Correcto! El número era: {numero}")
                botonComprobar["state"] = tk.DISABLED
                return
        else:
            resultado.set(f"Te quedaste sin intentos. El número era: {numero}")
            botonComprobar["state"] = tk.DISABLED


    resultado = tk.StringVar()
    etiquetaResultado = tk.Label(juego3Pantalla, textvariable=resultado)
    etiquetaResultado.pack()

    botonComprobar = ttk.Button(juego3Pantalla, text="Comprobar", command=comprobarJuego3)
    botonComprobar.pack()
    juego3Pantalla.mainloop()


main()