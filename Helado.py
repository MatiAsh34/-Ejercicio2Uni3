from Sabor import *

class Helado(object):
	__sabor = []
	def __init__(self,gramos,precio):
		self.__gramos = gramos
		self.__precio = precio
		self.__sabor = []

	def getSabores(self):
		return self.__sabor

	def getGramos(self):
		return self.__gramos

	def getPrecio(self):
		return self.__precio

	def agregarSabores(self,sabores):
		for i in range(len(sabores)):
			self.__sabor.append(sabores[i])
