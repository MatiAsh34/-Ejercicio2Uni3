import csv
from Helado import *
from Sabor import *
from ManejadorHelado import *

class ManejadorSabor(object):
	def __init__(self):
		self.__lista = []

	def CargaSabores(self):
		archivo = open('sabores.csv',encoding='utf8')
		reader = csv.reader(archivo,delimiter=';')

		for fila in reader:
			sabor = Sabor(int(fila[0]),fila[1],fila[2])
			self.__lista.append(sabor)

	def Compara(self,sabor):
		i = 0
		UnSabor = None
		band = False
		while i < len(self.__lista) and band != True:
			if sabor == self.__lista[i].getNombre():
				self.__lista[i].AumentaCant()
				UnSabor = self.__lista[i]
				band = True
			i += 1
		return UnSabor

	def Mostrar_HeladosMasPedidos(self):
		lista_ordenada = sorted(self.__lista)
		print ("Helados mas pedidos: ")
		for i in range(5):
			if lista_ordenada[i].getPedidos() != 0:
				print ("\t-{}".format(lista_ordenada[i].getNombre()))