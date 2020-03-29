from math import sqrt
import sys

def construir(x, y=None):
    return (float(x), y)

def lista(*x):
    return construir(x[0], lista(*x[1:])) if x else None

def primero(x):
    return x[0]

def resto(x):
    return x[1]

def vacia(x):
    return x is None

def largo(x):
    return 1 + largo(resto(x)) if not vacia(x) else 0

def sumar(x):
    return primero(x) + sumar(resto(x)) if x else 0

def mapear(f, x):
    return construir(f(primero(x)), mapear(f, resto(x))) if x else None

def promedio(x):
    return sumar(x) / largo(x) if largo(x) > 0 else 0

def desviacion(x):
    if largo(x) < 2:
        return 0
    prom = promedio(x)
    restas = mapear(lambda y: y - prom, x)
    cuadrados = mapear(lambda y: y * y, restas)
    sumatoria = sumar(cuadrados)
    return sqrt(sumatoria / (largo(x) - 1))

def main(*x):
    try:
        l = lista(*x)
        print(f"El promedio es: {promedio(l)}")
        print(f"La desviación estándar es: {desviacion(l)}")
    except ValueError:
        print("ERROR: Todos los parámetros deben ser números reales o enteros.")
        sys.exit()

if __name__ == '__main__':
    main(*sys.argv[1:])
