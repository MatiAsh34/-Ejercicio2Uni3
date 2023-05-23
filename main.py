from ManejadorHelado import *
from ManejadorSabor import *

if __name__ == '__main__':
	ManejadorSabores = ManejadorSabor()
	ManejadorSabores.CargaSabores()
	ManejadorHelado = ManejadorHelado()

	opcion = None
	while opcion != '0':
		print("\n---- Menu opciones ----")
		print("1- Registrar un helado.")
		print("2- Mostrar el nombre de los 5 sabores de helado más pedidos.")
		print("3- Ingrese un número de sabor y estimar el total de gramos vendidos.")
		print("4- Ingrese por teclado un tamaño de helado para mostrar los sabores vendidos en ese tamaño.")
		print("5- Mostrar importe total recaudado por la Heladería.")
		print("0- Salir")

		opcion = input("\nIngrese opcion: ")

		if opcion == '1':
			print('''
	250g  - $700
	500g  - $1300
	1000g - $2500\n''')
			gramos = float(input("Ingrese gramos: "))
			ManejadorHelado.RegistrarHelado(gramos,ManejadorSabores)

		if opcion == '2':
			ManejadorSabores.Mostrar_HeladosMasPedidos()

		if opcion == '3':
			numero = int(input("Ingrese numero de sabor: "))
			total = ManejadorHelado.CalcularGramos(numero)
			if total == 0:
				print ("No se ha pedido ese helado! ")
			else:
				print("El total de gramos vendidos de ese helado es: {}g".format(total))

		if opcion == '4':
			print('''
	250g  - $700
	500g  - $1300
	1000g - $2500\n''')
			gramos = float(input("Ingrese gramos: "))
			sabores = ManejadorHelado.Busqueda(gramos)
			print("Sabores vendidos: ")
			print(sabores)

		if opcion == '5':
			total_recaudado = ManejadorHelado.CalcularTotalRecaudado()
			print("El helado de 250g recaudó {}".format(total_recaudado[0]))
			print("El helado de 500g recaudó {}".format(total_recaudado[1]))
			print("El helado de 1000g recaudó {}".format(total_recaudado[2]))

		if opcion == '0':
			print("Saliendo...")