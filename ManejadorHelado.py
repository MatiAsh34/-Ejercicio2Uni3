from Helado import *
from Sabor import *
from ManejadorSabor import *

class ManejadorHelado(object):
	def __init__(self):
		self.__lista = []

	def IngresarSabor(self, ManejadorSabores):
		print('''
		Sabores de Helado\n
		Vainilla Crunch
		Fresa Delicia
		Choco Avellana
		Menta Chip
		Café Mocca
		Tropical Splash
		Bananacream
		Lemon Pie
		Caramelo Salado
		Coco Crunch\n''')
		i = 0
		sabor = ''
		sabores = []
		while i < 4 and sabor != '0':
			sabor = input("Ingrese sabor: ")
			UnSabor = ManejadorSabores.Compara(sabor)
			if UnSabor != None:
				sabores.append(UnSabor)
				i+=1
				print("Siguiente sabor...")

		return sabores

	def RegistrarHelado (self, gramos, ManejadorSabores):
		if gramos == 250:
			UnHelado = Helado(gramos,700)
			sabores = self.IngresarSabor(ManejadorSabores)
			UnHelado.agregarSabores(sabores)
			self.__lista.append(UnHelado)

		elif gramos == 500:
			UnHelado = Helado(gramos,1300)
			sabores = self.IngresarSabor(ManejadorSabores)
			UnHelado.agregarSabores(sabores)
			self.__lista.append(UnHelado)

		elif gramos == 1000:
			UnHelado = Helado(gramos,2500)
			sabores = self.IngresarSabor(ManejadorSabores)
			UnHelado.agregarSabores(sabores)
			self.__lista.append(UnHelado)

		else:
			print("Gramos incorrectos! ")


	def CalcularGramos(self,numero):
		i = 0 
		total = 0
		while i < len(self.__lista):
			j = 0
			sabores = self.__lista[i].getSabores()
			while j < len(sabores):
				if numero == sabores[j].getId():
					total = (self.__lista[i].getGramos()/4) + total
				j += 1
			i += 1
		return total

	def Busqueda(self,gramos):
		i = 0
		saboresGramos = []
		while i < len(self.__lista):
			j = 0
			sabores = []
			if gramos == self.__lista[i].getGramos():
				sabores = self.__lista[i].getSabores()
				while j < len(sabores):
					saboresGramos.append(sabores[j].getNombre())
					j += 1
			i += 1
		return saboresGramos

	def CalcularTotalRecaudado(self):
		total = [0,0,0]
		for i in range(len(self.__lista)):
			if self.__lista[i].getGramos() == 250:
				total[0] += self.__lista[i].getPrecio()
			elif self.__lista[i].getGramos() == 500:
				total[1] += self.__lista[i].getPrecio()
			elif self.__lista[i].getGramos() == 1000:
				total[2] += self.__lista[i].getPrecio()
		return total