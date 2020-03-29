import unittest
import lector

class LectorTestCase(unittest.TestCase):

    def test_leer_archivos(self):
        esperado = 2
        observado = len(lector.leer_archivos("psp0", ".py"))
        self.assertEqual(esperado, observado)

        esperado = ['psp0_b.py', 'psp0_a.py']
        observado = list(lector.leer_archivos("psp0", ".py").keys())
        self.assertEqual(esperado, observado)

        self.assertRaises(FileNotFoundError, lector.leer_archivos, "xyz", ".py")
