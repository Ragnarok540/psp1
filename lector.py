from os import listdir
from os.path import join, dirname, realpath

def leer_archivos(ruta, ext):
    r = join(dirname(realpath(__file__)), ruta)
    archivos = [a for a in listdir(r) if a.endswith(ext)]
    result = {}
    for archivo in archivos:
        with open(join(r, archivo)) as a:
            result[archivo] = a.read()
    return result
