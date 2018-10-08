class Derivada:
	"""Clase usada para calcular derivadas numéricas de una función
	Argumentos:
	f: Función a la que se le va a evaluar la derivada numérica
	metodo: Cadena de caracteres que contiene el método a usar para
	calcular la derivada numérica. Los valores validos son los
	siguientes:
	"adelante": Calcular la derivada usando el método de diferencias
	hacia adelante.
	"central": Calcula la derivada usando el método de la diferencia
	central.
	"extrapolada": Calcula la derivada usando el método de la
	diferencia extrapolada.
		"segunda": Calculo de la segunda derivada dx: Delta usado para el calculo de la derivada"""
		
	def __init__(self, f, metodo ="adelante", dx= 0.001):
		self.f = f
		self.metodo = metodo
		self.dx = dx
		self.derivada = 0

	""" Método que retorna el valor *numérico de la derivada de la función f evaluada en el punto x"""
	def calc(self,x):
		if self.metodo == "adelante":
			self.derivada = (self.f(x+self.dx)-self.f(x))/self.dx
		elif self.metodo == "central":
			self.derivada = (self.f(x+(self.dx/2))-self.f(x-(self.dx/2)))/self.dx
		elif self.metodo == "extrapolada":
			fmedio = (self.f(x+(self.dx/2))-self.f(x-(self.dx/2)))/self.dx
			fcuarto = (self.f(x+(self.dx/4))-self.f(x-(self.dx/4)))/(self.dx/2)
			self.derivada = ((4*fcuarto)-fmedio)/3
		elif self.metodo == "segunda":
			self.derivada = (self.f(x+self.dx)+self.f(x-self.dx)-(2*self.f(x)))/(self.dx*self.dx)
		return self.derivada
	def f (self,x):
		x*x*x
		
class Zeros:
	"""
	Clase que retorna el cero de una función
	Argumentos:
	f: 			Función a la que se le va a evaluar el cero
	metodo: 	Cadena de caracteres que contiene el método a usar para la
				búsqueda del cero. Los valores validos son los siguientes:
				"newton": Usa el método de newton para el calculo.
				"bisectriz": Usa el método de la bisectriz para el calculo.
				"interpolacion": Usa el método de la interpolación para el calculo
				"newton-sp": Usa la función newton definida en scipy para el calculo.
				"fsolve-sp": Usa la función fsolve definida en scipy para el calculo.
				"brentq-sp": Usa la función brentq definida en scipy para el calculo.
	error:		Valor máximo que puede tener f(x0) donde X0 es el cero encontrado numéricamente.
				Para las funciones de scipy, este es el valor pasado 			a xtol.
	max_iter: 	Numero máximo de iteraciones a usar en el calculo.
	"""
	def __init__(self, f, metodo, error=1e-4, max_iter=100):
		self.f = f
		self.metodo = metodo
		self.error = error
		self.max_iter = max_iter
		self.raiz = 0

	"""
	Método que retorna el valor del x0 encontrado
	Argumento:
	vi: 	Valor inicial a usar en la búsqueda del cero. Para los algoritmos
			que usen un solo punto, debe ser un flotante, para los algoritmos
			que usen 2 puntos, debe ser una tupla (a, b) de flotantes. """
			
	def newton (vi):
		iterator = 0
		x0 = vi
		df = Derivada(self.f,"extrapolada",0.00001)
		while(iterator < self.max_iter and df.calc(x0) != 0):
			x0=x0 - (self.f(x0)/df.calc(x0))
		return x0
			
	def bisectriz (vi):
		a = 0
		b = 0
		p = 0
		if(vi[0] < vi[1]):
			a = vi[0]
			b = vi[1]
		else:
			a = vi[1]
			b = vi[0]
			
		iterator = 0
		while( iterator < self.max_iter ):
			p = a +  ((b-a)/2)
			if self.f(p) == 0 or (b-a)/2 < self.error:
				return p
			iterator += 1
			if self.f(a)*self.f(p) > 0:
				a = p
			else:
				b = p
		return p

	def zero(self,vi):
		if self.metodo == "newton":
			#self.raiz = newton(vi)
			iterator = 0
			x0 = vi
			df = Derivada(self.f,"extrapolada",0.00001)
			while(iterator < self.max_iter):
				x0=x0 - (self.f(x0)/df.calc(x0))
			return x0
		elif self.metodo == "bisectriz":
			self.raiz = bisectriz(vi)
		elif self.metodo == "interpolacion":
			self.raiz = interpolacion(vi)
		elif self.metodo == "newton-sp":
			self.raiz = optimize.newton(self.f,vi)
		elif self.metodo == "fsolve-sp":
			self.raiz = optimize.fsolve(self.f,vi)
		elif self.metodo == "brentq-sp":
			self.raiz = optimize.brentq(self.f,vi[0],vi[1])
		return self.raiz			
if __name__ == "__main__":
	import math as math
	import numpy as np
	import pylab as plb
	from scipy import optimize
	
	f1 = math.sin
	derivada1 = Derivada(f1,"adelante",0.001)
	derivada2 = Derivada(f1,"central")
	derivada3 = Derivada(f1,"segunda")
	derivada4 = Derivada(f1,"extrapolada")
	#raiz1 = Zeros(f1,"newton",1e-4,10)
	raiz2 = Zeros(f1,"newton-sp",1e-4,1000)
	raiz3 = Zeros(f1,"fsolve-sp",1e-4,1000)
	raiz4 = Zeros(f1,"brentq-sp",1e-4,1000)
	print(derivada1.calc(0))
	print(derivada2.calc(0))
	print(derivada3.calc(0))
	print(derivada4.calc(0))
	#print(raiz1.zero(1))
	print(raiz2.zero(1))
	print(raiz3.zero(1))
	print(raiz4.zero(1))
		
