from contador import contar_lineas, contar_funciones
from lector import leer_archivos
import sys

def main(ruta):

    try:
        archivos = leer_archivos(ruta, ".py")
    except FileNotFoundError:
        print("ERROR: La ruta no es válida.")
        sys.exit()

    print("Archivo,LOC,Funciones")

    total_lineas = 0

    for nombre, texto in archivos.items():

        total_lineas += contar_lineas(texto)

        try:
            print(f"{nombre},{contar_lineas(texto)},{contar_funciones(texto)}")
        except SyntaxError:
            print(f"ERROR: El archivo '{nombre}' no es código fuente de Python 3 válido.")
            sys.exit()

    print(f"El total de líneas es: {total_lineas}")

if __name__ == '__main__':
    main(sys.argv[1])
