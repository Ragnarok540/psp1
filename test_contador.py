import unittest
import contador

class ContadorTestCase(unittest.TestCase):

    def setUp(self):
        self.prog_0 = """print("hello world")"""
        self.prog_1 = """
def fun1():
    pass

def fun2():
    pass
"""
        self.prog_2 = """print 'hello world'"""

    def test_contar_lineas(self):
        esperado = 1
        observado = contador.contar_lineas(self.prog_0)
        self.assertEqual(esperado, observado)

        esperado = 4
        observado = contador.contar_lineas(self.prog_1)
        self.assertEqual(esperado, observado)

    def test_contar_funciones(self):
        esperado = 0
        observado = contador.contar_funciones(self.prog_0)
        self.assertEqual(esperado, observado)

        esperado = 2
        observado = contador.contar_funciones(self.prog_1)
        self.assertEqual(esperado, observado)

        self.assertRaises(SyntaxError, contador.contar_funciones, self.prog_2)
