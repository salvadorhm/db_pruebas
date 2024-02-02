""" Libreria para el manejo de los hilos """
import threading


def funcion_hilo(hilo, numero):
    """
    Función que se ejecuta en un hilo independiente
    """
    for i in range(numero):
        print(f"Hilo {hilo}: {i}")


def main():
    """
    Función principal que crea e inicia los hilos
    """
    no_hilos = 5
    hilos = []
    for i in range(no_hilos):
        hilos.append(threading.Thread(target=funcion_hilo, args=(i, 5)))

    # Iniciar los hilos
    for i in range(no_hilos):
        hilos[i].start()

    # Esperar a que los hilos terminen
    for i in range(no_hilos):
        hilos[i].join()


if __name__ == "__main__":
    main()
