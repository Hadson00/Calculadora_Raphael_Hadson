from calculadora import CalculadoraCientifica
import unittest

class TesteCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraCientifica()

    def test_filtrar(self):
        self.assertTrue(self.calc.filtrar('a','b')) #Erro
        self.assertTrue(self.calc.filtrar(1,2))
        self.assertIsNotNone(self.calc.filtrar(2,1))
        with self.assertRaises(TypeError):
            self.calc.filtrar('a','b')
            self.calc.filtrar(1,'b')
            self.calc.filtrar('a',2)

    def test_adicao(self):
        self.assertEqual(self.calc.adicao(150,150),300)
        self.assertEqual(self.calc.adicao(123,432),555)
        self.assertNotEqual(self.calc.adicao(4,2),7)
        self.assertNotEqual(self.calc.adicao(20,10),31)
        self.assertEqual(self.calc.adicao(-1,-1),-2)
        self.assertIsNotNone(self.calc.adicao(20,30))
        with self.assertRaises(TypeError):
            self.calc.adicao('a',10)
            self.calc.adicao('a','b')
            self.calc.adicao(1,'a')

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(2,2),0)
        self.assertEqual(self.calc.subtracao(10,5),5)
        self.assertEqual(self.calc.subtracao(11,12),-1)
        self.assertNotEqual(self.calc.subtracao(50,40),11)
        self.assertIsNotNone(self.calc.subtracao(20,30))
        with self.assertRaises(TypeError):
            self.calc.subtracao('a',10)
            self.calc.subtracao('a','b')
            self.calc.subtracao(1,'a')
        
    def test_divisao(self):
        self.assertIsNotNone(self.calc.divisao(20,30))
        with self.assertRaises(ZeroDivisionError):
            self.calc.divisao(1,0)
        self.assertEqual(self.calc.divisao(10000,10),1000)
        self.assertEqual(self.calc.divisao(16,4),4)
        with self.assertRaises(TypeError):
            self.calc.divisao('a',10)
            self.calc.divisao('a','b')
            self.calc.divisao(1,'a')
    
    def test_raiz_quadrada(self):
        self.assertEqual(self.calc.raiz_quadrada(25),5)
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-25)
        self.assertNotEqual(self.calc.raiz_quadrada(100),1)
        with self.assertRaises(TypeError):
            self.calc.raiz_quadrada('a')
    
    def test_logaritimo(self):
        self.assertEqual(self.calc.logaritmo(10,10),1)
        self.assertEqual(self.calc.logaritmo(8,2),3)
        self.assertNotEqual(self.calc.logaritmo(20,10),1)
        self.assertTrue(self.calc.logaritmo(8,0),3) #Erro
        with self.assertRaises(ValueError):
            self.calc.logaritmo(0,2)
            self.calc.logaritmo(2,0)
        with self.assertRaises(TypeError):
            self.calc.logaritmo('a',10)
            self.calc.logaritmo('a','b')
            self.calc.logaritmo(1,'a')

    def test_potenciacao(self):
        self.assertEqual(self.calc.potenciacao(5,2),25)
        self.assertEqual(self.calc.potenciacao(10,3),1000)
        self.assertEqual(self.calc.potenciacao(10,0),1)
        self.assertNotEqual(self.calc.potenciacao(10,0),0)
        with self.assertRaises(TypeError):
            self.calc.potenciacao('a',10)
            self.calc.potenciacao('a','b')
            self.calc.potenciacao(1,'a')

    def test_seno(self):
        self.assertEqual(self.calc.seno(80),0.984807753012208)
        self.assertEqual(self.calc.seno(45),0.7071067811865476)
        self.assertEqual(self.calc.seno(90),1)
        self.assertEqual(self.calc.seno(0),0)
        self.assertNotEqual(self.calc.seno(90),2)
        self.assertNotEqual(self.calc.seno(30),0.51512154123154)
        with self.assertRaises(TypeError):
            self.calc.seno('a')

    def test_cosseno(self):
        self.assertEqual(self.calc.cosseno(30),0.8660254037844387)
        self.assertEqual(self.calc.cosseno(180),-1)
        self.assertEqual(self.calc.cosseno(0),1)
        self.assertNotEqual(self.calc.cosseno(270),1)
        self.assertNotEqual(self.calc.cosseno(30),0.51651321151231)
        with self.assertRaises(TypeError):
            self.calc.cosseno('a')

    def test_tangente(self):
        self.assertEqual(self.calc.tangente(30),0.5773502691896257)
        self.assertEqual(self.calc.tangente(45),0.9999999999999999)
        self.assertEqual(self.calc.tangente(90),0) #Erro
        self.assertNotEqual(self.calc.tangente(60),1)
        self.assertNotEqual(self.calc.tangente(0),1)
        with self.assertRaises(ValueError):
            self.calc.tangente(90)
            self.calc.tangente(270)
        with self.assertRaises(TypeError):
            self.calc.tangente('a')

if __name__ == '__main__':
    unittest.main()