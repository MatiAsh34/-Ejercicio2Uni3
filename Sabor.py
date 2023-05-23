class Sabor(object):
	def __init__(self,idSabor,ingredientes,nombre):
		self.__idSabor = idSabor
		self.__ingredientes = ingredientes
		self.__nombre = nombre	
		self.__cant_pedidos = 0

	def getNombre(self):
		return self.__nombre

	def getId(self):
		return self.__idSabor

	def getPedidos(self):
		return self.__cant_pedidos

	def AumentaCant(self):
		self.__cant_pedidos += 1

	def __gt__(self,otro):
		return self.__cant_pedidos<otro.getPedidos()