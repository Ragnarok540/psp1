import ast

def contar_lineas(texto):
    lineas = sum(1 for linea in texto.splitlines() if linea != '')
    return lineas

def contar_funciones(texto):
    arbol = ast.parse(texto)
    fns = sum(1 for nodo in ast.walk(arbol) if type(nodo) == ast.FunctionDef)
    return fns 
