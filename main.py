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
    juego1 = tk.Tk()
    juego1.title("Piedra Papel y Tijera")
    titulo = "Piedra Papel y Tijera"
    label_titulo = tk.Label(text=titulo, font=("Arial", 20))
    label_titulo.pack(padx=20, pady=20)

    # ESTO ES CON RADIOBUTTON
    # opcionJugador =

    opcionJugador = int(input())
    if opcionJugador >= 0 and opcionJugador <= 2:
        opcionMaquina = random.randint(0, 2)
        resultadoJuego = jugar(opcionJugador, opcionMaquina)
        imprimirResultado(opcionJugador, opcionMaquina, resultadoJuego)
    else:
        print("Error, debe elegir entre 0 y 2.")


def jugar(opcionJugador, opcionMaquina):
    resultado = 0
    # calculo el resultado y luego lo devuelvo
    if opcionJugador == opcionMaquina:
        resultado = 1
    elif opcionJugador == 0 and opcionMaquina == 1:
        resultado = 2
    elif opcionJugador == 0 and opcionMaquina == 2:
        resultado = 0
    elif opcionJugador == 1 and opcionMaquina == 0:
        resultado = 0
    elif opcionJugador == 1 and opcionMaquina == 2:
        resultado = 2
    elif opcionJugador == 2 and opcionMaquina == 0:
        resultado = 2
    elif opcionJugador == 2 and opcionMaquina == 1:
        resultado = 0
    return resultado


def obtenerOpcionMedianteNumero(numeroOpcion):
    # 0 es piedra, 1 es papel, 2 es tijera
    if numeroOpcion == 0:
        return "piedra"
    elif numeroOpcion == 1:
        return "papel"
    else:
        return "tijera"


def obtenerResultadoMedianteNumero(resultado):
    if resultado == 0:
        return "jugador gana"
    elif resultado == 1:
        return "empate"
    else:
        return "jugador pierde"



def imprimirResultado(opcionJugador, opcionMaquina, resultadoJuego):
    print(f"Jugador elige: {obtenerOpcionMedianteNumero(opcionJugador)}")
    print(f"Máquina elige: {obtenerOpcionMedianteNumero(opcionMaquina)}")
    print(f"Resultado: {obtenerResultadoMedianteNumero(resultadoJuego)}")


def juego2():
    root.destroy()
    juego2 = tk.Tk()
    juego2.title("Palabras en Inglés")
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
    respuesta = tk.Entry(juego2)
    respuesta.pack()


    puntos = 0
    for palabra in range(5):
        palabrasAleatorias = random.choice(list(palabras.keys()))
        respuesta = input(f"{palabrasAleatorias}: ")
        if respuesta == palabras[palabrasAleatorias]:
            print("Correcto")
            puntos += 1
        else:
            print("Incorrecto")

    print(f"Tus puntos: {puntos}/5")


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