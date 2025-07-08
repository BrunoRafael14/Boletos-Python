# Algoritmo para eu guardar boletos que são parcelados
import os

contagem = "sim"

enderecos = []
numero_boletos = []
data_boletos = []


while contagem == "sim":
	print("O que deseja fazer: ")
	print("1 - Adicionar Boleto")
	print("2 - Consultar Boletos")
	print("3 - Excluir Boletos")
	menu = int(input(""))

	if menu == 1:
		# os.system("cls")
		busca_endereco = input("Digite o endereço do Imóvel: ")
		busca_numero_boleto = input("Digite o número do Boleto: ")
		busca_data_boleto = input("Digite a data do vencimento do boleto (XX/XX/XXX) :")

		enderecos.append(busca_endereco)
		numero_boletos.append(busca_numero_boleto)
		data_boletos.append(busca_data_boleto)

		print("Boleto número {} cadastrado com sucesso!".format(numero_boletos))

	elif menu == 2:
		# os.system("cls")

		busca = input("Digite o número do Boleto para consulta: ")
		if busca in numero_boletos:
			position = numero_boletos.index(busca)
			print("Endereço é {}, o número do boleto é {} e a data de vencimento do boleto é {}".format(enderecos[position], numero_boletos[position], data_boletos[position]))
		else:
			print("Boleto não cadastrado")
	elif menu == 3:
		# os.system("cls")
		busca = input("Digite o número do Boleto para exclusão: ")


	contagem = input("Deseja fazer mais buscas ? ")
	contagem = contagem.lower()
