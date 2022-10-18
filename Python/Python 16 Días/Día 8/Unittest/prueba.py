# UNITTEST
'''
Es un modulo utilizado en programacion para determinar si un modulo o conjunto de modulos 
funcionan correctamente. Dicha evaluacion se realiza en un archivo independiente.
'''


import unittest
import cambia_text

class ProbarCambiarTexto(unittest.TestCase):
    
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_text.todo_mayusculas(palabra)
        self.assertEqual(resultado, "Buen Dia")


if __name__ == '__main___':
    unittest.main()
