from calculadora import CalculadoraCientifica
import pytest

cal = CalculadoraCientifica()
a = 'calculadora'
b = ['escola','aluno']
class Test_py():

    def test_adicao(self):
        assert cal.adicao(4,2) == 6
        with pytest.raises(TypeError):
            cal.adicao('a',1)
        assert cal.adicao(1,4) != 4
    
    def test_subtracao(self):
        assert cal.subtracao(30,28) == 2
        with pytest.raises(TypeError):
            cal.subtracao('a',1)
        assert cal.subtracao(1,4) != 4

    def test_multiplicacao(self):
        assert cal.multiplicacao(3,2) == 6
        with pytest.raises(TypeError):
            cal.multiplicacao('a',1)
        assert cal.multiplicacao(1,4) != 8
    

    def test_divisao(self):
        with pytest.raises(ZeroDivisionError):
            cal.divisao(1,0)
        cal.divisao(10000,10) == 1000
        cal.divisao(16,4) == 4
        with pytest.raises(TypeError):
            cal.divisao('a',10)
            cal.divisao('a','b')
            cal.divisao(1,'a')

    def test_raiz_quadrada(self):
        cal.raiz_quadrada(25) == 5
        with pytest.raises(ValueError):
            cal.raiz_quadrada(-25)
        cal.raiz_quadrada(100) == 1
        with pytest.raises(TypeError):
            cal.raiz_quadrada('a')
    
    def test_logaritimo(self):
        cal.logaritmo(10,10) == 1
        cal.logaritmo(8,2) == 3
        cal.logaritmo(20,10) == 1
        with pytest.raises(ValueError):
            cal.logaritmo(0,2)
            cal.logaritmo(2,0)
        with pytest.raises(TypeError):
            cal.logaritmo('a',10)
            cal.logaritmo('a','b')
            cal.logaritmo(1,'a')


    def test_seno(self):
        assert cal.seno(30) == 0.49999999999999994
        assert cal.seno(1) != 4

    def test_cosseno(self):
        assert cal.cosseno(30) == 0.8660254037844387
        assert cal.cosseno(1) != 4

    def test_tangente(self):
        assert cal.tangente(30) == 0.5773502691896257
        with pytest.raises(ValueError):
            cal.tangente(90)
        assert cal.tangente(1) != 4