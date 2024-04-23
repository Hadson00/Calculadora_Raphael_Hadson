import math

class CalculadoraCientifica:
    def __init__(self):
        self.ultimo_resultado = None

    
    def filtrar(self, n1, n2 = 0):
        if type(n1) == str or type(n2) == str:
            raise TypeError('Digite somente números')
        return True

    def adicao(self, n1:int, n2:int):
        self.filtrar(n1,n2)
        self.ultimo_resultado = n1 + n2
        return self.ultimo_resultado

    def subtracao(self, n1:int, n2:int):
        self.filtrar(n1,n2)
        self.ultimo_resultado = n1 - n2
        return self.ultimo_resultado
    
    def multiplicacao(self, n1:int, n2:int):
        self.filtrar(n1,n2)
        self.ultimo_resultado = n1 * n2
        return self.ultimo_resultado
    
    def divisao(self, n1:int, n2:int):
        self.filtrar(n1,n2)
        if n1 == 0 or n2 == 0:
            raise ZeroDivisionError('Divisão Por Zero')
        self.ultimo_resultado = n1 / n2
        return self.ultimo_resultado
    
    def potenciacao(self, base:int, expoente:int):
        self.filtrar(base, expoente)
        self.ultimo_resultado = base ** expoente
        return self.ultimo_resultado

    def raiz_quadrada(self, n1:int):
        self.filtrar(n1)
        if n1 < 0:
           raise ValueError('Número negativo inserido')
        self.ultimo_resultado = math.sqrt(n1)
        return self.ultimo_resultado
    
    def logaritmo(self, log, base):
        self.filtrar(log,base)
        if base <= 0 or log <= 0:
            raise ValueError('Número negativo inserido')
        self.ultimo_resultado = math.log(log,base)
        return self.ultimo_resultado
    
    def seno(self,angulo):
        self.filtrar(angulo)
        radianos = math.radians(angulo)
        self.ultimo_resultado = math.sin(radianos)
        return self.ultimo_resultado
    
    def cosseno(self,angulo):
        self.filtrar(angulo)
        radianos = math.radians(angulo)
        self.ultimo_resultado = math.cos(radianos)
        return self.ultimo_resultado 

    def tangente(self,angulo):
        self.filtrar(angulo)
        if angulo == 90 or angulo == 270:
            raise ValueError('Não Existe Tangente Com O Ângulo Inserido')
        radianos = math.radians(angulo)
        self.ultimo_resultado = math.tan(radianos)
        return self.ultimo_resultado
    
    def __str__(self):
        return f'Olá, Seja Bem-Vindo à Calculadora Científica'